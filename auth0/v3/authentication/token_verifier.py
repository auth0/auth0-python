from abc import ABC

from ..exceptions import Auth0Error
import jwt
import time

# TODO: Have a custom exception class
TOKEN_VERIFIER_ERROR = 'a0.sdk.internal.token_verification'

RSA_PUBLIC_KEY = b"""-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuGbXWiK3dQTyCbX5xdE4\nyCuYp0AF2d15Qq1JSXT/lx8CEcXb9RbDddl8jGDv+spi5qPa8qEHiK7FwV2KpRE9\n83wGPnYsAm9BxLFb4YrLYcDFOIGULuk2FtrPS512Qea1bXASuvYXEpQNpGbnTGVs\nWXI9C+yjHztqyL2h8P6mlThPY9E9ue2fCqdgixfTFIF9Dm4SLHbphUS2iw7w1JgT\n69s7of9+I9l5lsJ9cozf1rxrXX4V1u/SotUuNB3Fp8oB4C1fLBEhSlMcUJirz1E8\nAziMCxS+VrRPDM+zfvpIJg3JljAh3PJHDiLu902v9w+Iplu1WyoB2aPfitxEhRN0\nYwIDAQAB\n-----END PUBLIC KEY-----"""

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

    def __init__(self, jwks_url, algorithm="RS256"):
        SignatureVerifier.__init__(self, algorithm)
        self.jwks_url = jwks_url

    def _fetch_key(self, key_id=None):
        # TODO: Delegate this to some jwks fetching code
        # e.g. https://pypi.org/project/simple-memory-cache/
        return RSA_PUBLIC_KEY


class TokenVerifier():

    def __init__(self, signature_verifier, issuer, audience, leeway=0, _clock=None):
        # TODO: See if these checks are OK
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



