import json
import time

import jwt
import requests

from auth0.v3.exceptions import TokenValidationError

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
            raise ValueError("algorithm must be specified.")
        self._algorithm = algorithm

    def _fetch_key(self, key_id=None):
        raise NotImplementedError

    def verify_signature(self, token):
        try:
            header = jwt.get_unverified_header(token)
        except jwt.exceptions.DecodeError:
            raise TokenValidationError("ID token could not be decoded.")

        alg = header.get('alg', None)
        if alg != self._algorithm:
            raise TokenValidationError('Signature algorithm of "{}" is not supported. Expected the ID token to be signed with "{}"'.format(alg, self._algorithm))

        kid = header.get('kid', None)
        secret_or_certificate = self._fetch_key(key_id=kid)

        try:
            decoded = jwt.decode(jwt=token, key=secret_or_certificate, algorithms=[self._algorithm], options=DISABLE_JWT_CHECKS)
        except jwt.exceptions.InvalidSignatureError:
            raise TokenValidationError("Invalid token signature.")
        return decoded


class SymmetricSignatureVerifier(SignatureVerifier):

    def __init__(self, shared_secret, algorithm="HS256"):
        SignatureVerifier.__init__(self, algorithm)
        self._shared_secret = shared_secret

    def _fetch_key(self, key_id=None):
        return self._shared_secret


class AsymmetricSignatureVerifier(SignatureVerifier):

    def __init__(self, jwks_url, algorithm="RS256", _jwks_fetcher=None):
        SignatureVerifier.__init__(self, algorithm)
        self._fetcher = _jwks_fetcher or JwksFetcher(jwks_url)

    def _fetch_key(self, key_id=None):
        return self._fetcher.get_key(key_id)


class JwksFetcher():

    def __init__(self, jwks_url, cache_ttl=JWKS_CACHE_TTL):
        self._jwks_url = jwks_url
        self._init_cache(cache_ttl)
        return

    def _init_cache(self, cache_ttl):
        self._cache_value = {}
        self._cache_date = 0
        self._cache_ttl = cache_ttl
        self._cache_is_fresh = False

    def _fetch_jwks(self, force=False):
        has_expired = self._cache_date + self._cache_ttl < time.time()

        if not force and not has_expired:
            # Return from cache
            self._cache_is_fresh = False
            return self._cache_value

        # Invalidate cache and fetch fresh data
        self._cache_value = {}
        response = requests.get(self._jwks_url)

        if response.ok:
            # Update cache
            jwks = response.json()
            self._cache_value = self._parse_jwks(jwks)
            self._cache_is_fresh = True
            self._cache_date = time.time()
        return self._cache_value

    @staticmethod
    def _parse_jwks(jwks):
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

        if not self._cache_is_fresh:
            keys = self._fetch_jwks(force=True)
            if keys and key_id in keys:
                return keys[key_id]
        raise TokenValidationError('RSA Public Key with ID "{}" was not found.'.format(key_id))


class TokenVerifier():

    def __init__(self, signature_verifier, issuer, audience, leeway=0, _clock=None):
        if not signature_verifier or not isinstance(signature_verifier, SignatureVerifier):
            raise TypeError("signature_verifier must be an instance of SignatureVerifier.")

        self._options = {
            'signature_verifier': signature_verifier,
            'iss': issuer,
            'aud': audience,
            'leeway': leeway,
            '_clock': _clock
        }

    def verify(self, token, nonce=None, max_age=None):
        # Verify token presence
        if not token or type(token) != str:
            raise TokenValidationError("ID token is required but missing.")
        if nonce and type(nonce) != str:
            raise TokenValidationError("Nonce not specified.")
        if max_age and type(max_age) != int:
            raise TokenValidationError("Max Age not specified.")

        opt = self._options.copy()
        opt['nonce'] = nonce
        opt['max_age'] = max_age

        # Verify algorithm and signature
        payload = opt['signature_verifier'].verify_signature(token)

        # Verify claims
        # Issuer

        if 'iss' not in payload or type(payload['iss']) != str:
            raise TokenValidationError('Issuer (iss) claim must be a string present in the ID token')
        if payload['iss'] != opt['iss']:
            raise TokenValidationError('Issuer (iss) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['iss'], payload['iss']))

        # Subject
        if 'sub' not in payload or type(payload['sub']) != str:
            raise TokenValidationError('Subject (sub) claim must be a string present in the ID token')

        # Audience
        if 'aud' not in payload or not (type(payload['aud']) == str or type(payload['aud']) is list):
            raise TokenValidationError('Audience (aud) claim must be a string or array of strings present in the ID token')

        if type(payload['aud']) is list and not opt['aud'] in payload['aud']:
            payload_audiences = ", ".join(payload['aud'])
            raise TokenValidationError('Audience (aud) claim mismatch in the ID token; expected "{}" but was not one of "{}"'.format(opt['aud'], payload_audiences))
        elif type(payload['aud']) == str and payload['aud'] != opt['aud']:
            raise TokenValidationError('Audience (aud) claim mismatch in the ID token; expected "{}" but found "{}"'.format(opt['aud'], payload['aud']))

        # --Time validation (epoch)--
        now = opt['_clock'] or time.time()
        leeway = opt['leeway']

        # Expires at
        if 'exp' not in payload or type(payload['exp']) != int:
            raise TokenValidationError('Expiration Time (exp) claim must be a number present in the ID token')

        exp_time = payload['exp'] + leeway
        if now > exp_time:
            raise TokenValidationError('Expiration Time (exp) claim error in the ID token; current time ({}) is after expiration time ({})'.format(now, exp_time))

        # Issued at
        if 'iat' not in payload or type(payload['iat']) != int:
            raise TokenValidationError('Issued At (iat) claim must be a number present in the ID token')

        iat_time = payload['iat'] - leeway
        if now < iat_time:
            raise TokenValidationError('Issued At (iat) claim error in the ID token; current time ({}) is before issued at time ({})'.format(now, iat_time))

        # Nonce
        if 'nonce' in opt and opt['nonce']:
            if 'nonce' not in payload or type(payload['nonce']) != str:
                raise TokenValidationError('Nonce (nonce) claim must be a string present in the ID token')
            if payload['nonce'] != opt['nonce']:
                raise TokenValidationError('Nonce (nonce) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['nonce'], payload['nonce']))

        # Authorized party
        if type(payload['aud']) is list and len(payload['aud']) > 1:
            if 'azp' not in payload or type(payload['azp']) != str:
                raise TokenValidationError('Authorized Party (azp) claim must be a string present in the ID token when Audience (aud) claim has multiple values')
            if payload['azp'] != opt['aud']:
                raise TokenValidationError('Authorized Party (azp) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['aud'], payload['azp']))

        # Authentication time
        if 'max_age' in opt and opt['max_age']:
            if 'auth_time' not in payload or type(payload['auth_time']) != int:
                raise TokenValidationError('Authentication Time (auth_time) claim must be a number present in the ID token when Max Age (max_age) is specified')

            auth_valid_until = payload['auth_time'] + opt['max_age'] + leeway
            if now > auth_valid_until:
                raise TokenValidationError('Authentication Time (auth_time) claim in the ID token indicates that too much time has passed since the last end-user authentication. Current time ({}) is after last auth at ({})'.format(now, auth_valid_until))



