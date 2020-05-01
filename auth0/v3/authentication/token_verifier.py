import json

from ..exceptions import Auth0Error
import jwt
import time
import requests

# TODO: Have a custom exception class
TOKEN_VERIFIER_ERROR = 'a0.sdk.internal.token_verification'

JWKS_CACHE_TTL = 60  # In seconds

DISABLE_JWT_CHECKS = {
    "verify_signature": True,
    "verify_exp": False,
    "verify_nbf": False,
    "verify_iat": False,
    "verify_aud": False,
    "verify_iss": False,
    "require_exp": False,
    "require_iat": False,
    "require_nbf": False,
}


class SignatureVerifier():

    def __init__(self, algorithm):
        if not algorithm or type(algorithm) != str:
            raise Exception("The algorithm value is invalid")
        self.algorithm = algorithm

    def _fetch_key(self, key_id=None):
        raise NotImplementedError

    def verify_signature(self, token):
        try:
            header = jwt.get_unverified_header(token)
        except jwt.exceptions.DecodeError:
            raise Exception("ID token could not be decoded.")

        alg = header.get('alg', None)
        if alg != self.algorithm:
            raise Exception('Signature algorithm of "{}" is not supported. Expected the ID token to be signed with "{}"'.format(alg, self.algorithm))

        kid = header.get('kid', None)
        secret_or_certificate = self._fetch_key(key_id=kid)

        try:
            decoded = jwt.decode(jwt=token, key=secret_or_certificate, algorithms=[self.algorithm], options=DISABLE_JWT_CHECKS)
        except jwt.exceptions.InvalidSignatureError:
            raise Exception("Invalid token signature.")
        return decoded


class SymmetricSignatureVerifier(SignatureVerifier):

    def __init__(self, shared_secret, algorithm="HS256"):
        SignatureVerifier.__init__(self, algorithm)
        self.shared_secret = shared_secret

    def _fetch_key(self, key_id=None):
        return self.shared_secret


class AsymmetricSignatureVerifier(SignatureVerifier):

    def __init__(self, jwks_url, algorithm="RS256", _jwks_fetcher=None):
        SignatureVerifier.__init__(self, algorithm)
        self.fetcher = _jwks_fetcher or JwksFetcher(jwks_url)

    def _fetch_key(self, key_id=None):
        return self.fetcher.get_key(key_id)


class JwksFetcher():

    def __init__(self, jwks_url, cache_ttl=JWKS_CACHE_TTL):
        self.jwks_url = jwks_url
        self._init_cache(cache_ttl)
        return

    def _init_cache(self, cache_ttl):
        # FIXME: Are these and other properties suppose to be private?
        self.cache_value = {}
        self.cache_date = 0
        self.cache_ttl = cache_ttl
        self.cache_is_fresh = False

    def _fetch_jwks(self, force=False):
        has_expired = self.cache_date + self.cache_ttl < time.time()

        if not force and not has_expired:
            # Return from cache
            self.cache_is_fresh = False
            return self.cache_value

        # Invalidate cache and fetch fresh data
        self.cache_value = {}
        response = requests.get(self.jwks_url)

        if response.ok:
            # Update cache
            jwks = response.json()
            self.cache_value = self._parse_jwks(jwks)
            self.cache_is_fresh = True
            self.cache_date = time.time()
        return self.cache_value

    def _parse_jwks(self, jwks):
        keys = {}

        for key in jwks['keys']:
            # noinspection PyUnresolvedReferences
            # requirement already includes cryptography -> pyjwt[crypto]
            rsa_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
            keys[key["kid"]] = rsa_key
        return keys

    def get_key(self, key_id):
        keys = self._fetch_jwks()

        if keys and key_id in keys:
            return keys[key_id]

        if not self.cache_is_fresh:
            keys = self._fetch_jwks(force=True)
            if keys and key_id in keys:
                return keys[key_id]
        raise Exception('RSA Public Key with ID "{}" was not found.'.format(key_id))


class TokenVerifier():

    def __init__(self, signature_verifier, issuer, audience, leeway=0, _clock=None):
        # TODO: See if these checks are OK
        # TODO: init JWKS / cache
        if not signature_verifier or not isinstance(signature_verifier, SignatureVerifier):
            raise Exception("Signature verified not specified.")
        if not issuer or type(issuer) != str:
            raise Exception("Issuer not specified.")
        if not audience or type(audience) != str:
            raise Exception("Audience not specified.")
        if type(leeway) != int:
            raise Exception("Invalid leeway value.")

        self.options = {
            'signature_verifier': signature_verifier,
            'iss': issuer,
            'aud': audience,
            'leeway': leeway,
            '_clock': _clock
        }

    def verify(self, token, nonce=None, max_age=None):
        # Verify token presence
        if not token or type(token) != str:
            raise Exception("ID token is required but missing.")
        if nonce and type(nonce) != str:
            raise Exception("Nonce not specified.")
        if max_age and type(max_age) != int:
            raise Exception("Max Age not specified.")

        opt = self.options.copy()
        opt['nonce'] = nonce
        opt['max_age'] = max_age

        # Verify algorithm and signature
        payload = opt['signature_verifier'].verify_signature(token)

        # Verify claims
        # Issuer

        if 'iss' not in payload or type(payload['iss']) != str:
            raise Exception('Issuer (iss) claim must be a string present in the ID token')
        if payload['iss'] != opt['iss']:
            raise Exception('Issuer (iss) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['iss'], payload['iss']))

        # Subject
        if 'sub' not in payload or type(payload['sub']) != str:
            raise Exception('Subject (sub) claim must be a string present in the ID token')

        # Audience
        if 'aud' not in payload or not (type(payload['aud']) == str or type(payload['aud']) is list):
            raise Exception('Audience (aud) claim must be a string or array of strings present in the ID token')

        if type(payload['aud']) is list and not opt['aud'] in payload['aud']:
            payload_audiences = ", ".join(payload['aud'])
            raise Exception('Audience (aud) claim mismatch in the ID token; expected "{}" but was not one of "{}"'.format(opt['aud'], payload_audiences))
        elif type(payload['aud']) == str and payload['aud'] != opt['aud']:
            raise Exception('Audience (aud) claim mismatch in the ID token; expected "{}" but found "{}"'.format(opt['aud'], payload['aud']))

        # --Time validation (epoch)--
        now = opt['_clock'] or time.time()
        leeway = opt['leeway']

        # Expires at
        if 'exp' not in payload or type(payload['exp']) != int:
            raise Exception('Expiration Time (exp) claim must be a number present in the ID token')

        exp_time = payload['exp'] + leeway
        if now > exp_time:
            raise Exception('Expiration Time (exp) claim error in the ID token; current time ({}) is after expiration time ({})'.format(now, exp_time))

        # Issued at
        if 'iat' not in payload or type(payload['iat']) != int:
            raise Exception('Issued At (iat) claim must be a number present in the ID token')

        iat_time = payload['iat'] - leeway
        if now < iat_time:
            raise Exception('Issued At (iat) claim error in the ID token; current time ({}) is before issued at time ({})'.format(now, iat_time))

        # Nonce
        if 'nonce' in opt and opt['nonce']:
            if 'nonce' not in payload or type(payload['nonce']) != str:
                raise Exception('Nonce (nonce) claim must be a string present in the ID token')
            if payload['nonce'] != opt['nonce']:
                raise Exception('Nonce (nonce) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['nonce'], payload['nonce']))

        # Authorized party
        if type(payload['aud']) is list and len(payload['aud']) > 1:
            if 'azp' not in payload or type(payload['azp']) != str:
                raise Exception('Authorized Party (azp) claim must be a string present in the ID token when Audience (aud) claim has multiple values')
            if payload['azp'] != opt['aud']:
                raise Exception('Authorized Party (azp) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['aud'], payload['azp']))

        # Authentication time
        if 'max_age' in opt and opt['max_age']:
            if 'auth_time' not in payload or type(payload['auth_time']) != int:
                raise Exception('Authentication Time (auth_time) claim must be a number present in the ID token when Max Age (max_age) is specified')

            auth_valid_until = payload['auth_time'] + opt['max_age'] + leeway
            if now > auth_valid_until:
                raise Exception('Authentication Time (auth_time) claim in the ID token indicates that too much time has passed since the last end-user authentication. Current time ({}) is after last auth at ({})'.format(now, auth_valid_until))



