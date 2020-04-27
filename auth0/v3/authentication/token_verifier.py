from ..exceptions import Auth0Error
import jwt
import time

# TODO: Have a custom exception class
TOKEN_VERIFIER_ERROR = 'a0.sdk.internal.token_verification'

class SignatureVerifier():

    def __init__(self, algorithm, secret=None, certificate=None):
        if (algorithm not in ['HS256', 'RS256'] or type(algorithm) != str):
            # This checks that it was set up correctly
            raise 'Signature algorithm of "%{}" is not supported. Expected the ID token to be signed with "%{}"'.format(algorithm, "RS256")
        self.algorithm = algorithm
        self.secret = secret
        self.certificate = certificate

    def verifySignature(self, token):
        disabledClaimsCheck = {
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
        try:
            #TODO: Make this take the algorithm from self and fetch the keys
            decoded = jwt.decode(jwt=token, key=self.certificate or self.secret, algorithms=[self.algorithm], options=disabledClaimsCheck)
        except jwt.exceptions.InvalidSignatureError:
            raise Exception("Invalid token signature.")
        except jwt.exceptions.DecodeError:
            raise Exception("ID token could not be decoded.")
        except jwt.exceptions.InvalidAlgorithmError:
            # This is raised when the token's algorithm is not one of the expected
            raise Exception('Signature algorithm of "{}" is not supported. Expected the ID token to be signed with "{}"'.format(self.algorithm, "RS256"))
        return decoded

    # def _getSecretOrCertificate(self, token):
    #     if (self.options.client_secret and self.algorithm == 'HS256'):
    #         return self.options.client_secret
    #     if (self.algorithm == 'RS256'):
    #         _fetchPublicKey(self.options.issuer)

    #     key = 'secret'
    #     header = jwt.get_unverified_header(encoded)


class TokenVerifier():

    def __init__(self, signatureVerifier, issuer, audience, leeway=0, _clock=None):
        if (not signatureVerifier or type(signatureVerifier) is not SignatureVerifier):
            raise Exception("Signature verified not specified.")
        if (not issuer or type(issuer) != str):
            raise Exception("Issuer not specified.")
        if (not audience or type(audience) != str):
            raise Exception("Audience not specified.")
        if (type(leeway) != int):
            raise Exception("Invalid leeway value.")

        self.options = {
            'signatureVerifier': signatureVerifier,
            'iss': issuer,
            'aud': audience,
            'leeway': leeway,
            '_clock': _clock
        }

    def verify(self, token, nonce=None, maxAge=-1):
        # Verify token presence
        if (not token or type(token) != str):
            raise Exception("ID token is required but missing.")
        if (nonce and type(nonce) != str):
            raise Exception("Nonce not specified.")
        if (maxAge and type(maxAge) != int):
            raise Exception("Max Age not specified.")

        opt = self.options.copy()
        opt['nonce'] = nonce
        opt['maxAge'] = maxAge

        # Verify algorithm and signature
        payload = opt['signatureVerifier'].verifySignature(token)

        #Verify claims
        ##Issuer

        if ('iss' not in payload or type(payload['iss']) != str):
            raise Exception('Issuer (iss) claim must be a string present in the ID token')
        if (payload['iss'] != opt['iss']):
            raise Exception('Issuer (iss) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['iss'], payload['iss']))

        ##Subject
        if ('sub' not in payload or type(payload['sub']) != str):
            raise Exception('Subject (sub) claim must be a string present in the ID token')


        ##Audience
        if ('aud' not in payload or not (type(payload['aud']) == str or type(payload['aud']) is list)):
            raise Exception('Audience (aud) claim must be a string or array of strings present in the ID token')

        if (type(payload['aud']) is list and not opt['aud'] in payload['aud']):
            payloadAudiences = ", ".join(payload['aud'])
            raise Exception('Audience (aud) claim mismatch in the ID token; expected "{}" but was not one of "{}"'.format(opt['aud'], payloadAudiences))
        elif (type(payload['aud']) == str and payload['aud'] != opt['aud']):
            raise Exception('Audience (aud) claim mismatch in the ID token; expected "{}" but found "{}"'.format(opt['aud'], payload['aud']))

        ##--Time validation (epoch)--
        realClock = time.time()
        now = opt['_clock'] or time.time()
        print("Real clock: {}".format(realClock))
        print("Using now: {}".format(now))
        leeway = opt['leeway']
        print("Leeway: {}".format(leeway))

        ##Expires at
        if ('exp' not in payload or type(payload['exp']) != int):
            raise Exception('Expiration Time (exp) claim must be a number present in the ID token')

        expTime = payload['exp'] + leeway
        if (now > expTime):
            raise Exception('Expiration Time (exp) claim error in the ID token; current time ({}) is after expiration time ({})'.format(now, expTime))

        ##Issued at
        if ('iat' not in payload or type(payload['iat']) != int):
            raise Exception('Issued At (iat) claim must be a number present in the ID token')

        iatTime = payload['iat'] - leeway
        print("Found iat+leeway: {}".format(iatTime))
        print("now - iat claim: {}".format(now - iatTime))
        if (now < iatTime):
            raise Exception('Issued At (iat) claim error in the ID token; current time ({}) is before issued at time ({})'.format(now, iatTime))

        ##Nonce
        if ( 'nonce' in opt and opt['nonce']):
            if ('nonce' not in payload or type(payload['nonce']) != str):
                raise Exception('Nonce (nonce) claim must be a string present in the ID token')
            if (payload['nonce'] != opt['nonce']):
                raise Exception('Nonce (nonce) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['nonce'], payload['nonce']))

        ##Authorized party
        if (type(payload['aud']) is list and len(payload['aud']) > 1):
            if ('azp' not in payload or type(payload['azp']) != str):
                raise Exception('Authorized Party (azp) claim must be a string present in the ID token when Audience (aud) claim has multiple values')
            if (payload['azp'] != opt['aud']):
                raise Exception('Authorized Party (azp) claim mismatch in the ID token; expected "{}", found "{}"'.format(opt['aud'], payload['azp']))

        ##Authentication time
        if ('maxAge' in opt and opt['maxAge']):
            if ('auth_time' not in payload or type(payload['auth_time']) != int):
                raise Exception('Authentication Time (auth_time) claim must be a number present in the ID token when Max Age (max_age) is specified')

            authValidUntil = payload['auth_time'] + opt['maxAge'] + leeway
            if (now > authValidUntil):
                raise Exception('Authentication Time (auth_time) claim in the ID token indicates that too much time has passed since the last end-user authentication. Current time ({}) is after last auth at ({})'.format(now, authValidUntil))



