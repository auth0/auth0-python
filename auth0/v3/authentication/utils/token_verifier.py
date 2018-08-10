import requests
from ...exceptions import TokenVerificationError
from jose import jwt
from jose.utils import base64url_decode
from jose.exceptions import ExpiredSignatureError, JWTClaimsError

class TokenVerifier(object):
    """TokenVerifier. A JWT signature and claims verifier, designed for Auth0 service. Follows https://auth0.com/docs/tokens/id-token#validate-an-id-token

    Args:
        jwk_provider (JwkProvider): An instance of the JWK provider to use to obtain the public keys
    """

    def __init__(self, jwk_provider):
        self._jwk_provider = jwk_provider

    def verify(self, token, issuer, audience):
        """Verifies a given token's signature and claims.

        Args:
            token (str): The token to verify. Must be signed using the RS256 algorithm. Will deem tokens signed with HS256 as valid.
            issuer (str): The issuer to expect. Matches the auth0 domain in this form 'https://username.auth0.com/'.
            audience (str): The audience expected to be contained in this token. Matches the auth0 client id.

        Returns:
            None
        
        Raises:
            TokenVerificationError: when the token has expired, or the claims don't match or the signature could not be verified.
            JwkProviderError: if the public key is not found
        """

        header = jwt.get_unverified_header(token)
        if header['alg'].lower()=='hs256':
            #Compatibility with HS256 (legacy tokens)
            return None
        jwk = self._jwk_provider.get_jwk(header['kid'])
        try:
            payload = jwt.decode(token=token, key=jwk, algorithms='RS256', issuer=issuer, audience=audience)
        except (ExpiredSignatureError):
            raise TokenVerificationError('The token has expired')
        except (JWTClaimsError):
            raise TokenVerificationError('Some of the claims in the token are not valid')
        except:
            raise TokenVerificationError('The token signature could not be verified')