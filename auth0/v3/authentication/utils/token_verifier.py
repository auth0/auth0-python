import requests
from ...exceptions import TokenVerificationError
from jose import jwt
from jose.utils import base64url_decode
from jose.exceptions import ExpiredSignatureError, JWTClaimsError

class TokenVerifier(object):
    """Token Verifier

    Args:
        jwk_provider (JwkProvider): An instance of the JWK provider to use to obtain the public keys
    """

    def __init__(self, jwk_provider):
        self._jwk_provider = jwk_provider

    def verify(self, token, issuer, audience):
        header = jwt.get_unverified_header(token)
        if header['alg'].lower()=='hs256':
            #Compatibility with HS256 (legacy tokens)
            return None
        jwk = self._jwk_provider.get_jwk(header['kid'])
        try:
            payload = jwt.decode(token=token, key=jwk, algorithms='RS256', issuer=issuer, audience=audience)
        except (ExpiredSignatureError):
            raise TokenVerificationError('The token has expired')
        except (JWTClaimsError) as e:
            raise TokenVerificationError('Some of the claims in the token are not valid') from e
        except:
            raise TokenVerificationError('The token signature could not be verified')