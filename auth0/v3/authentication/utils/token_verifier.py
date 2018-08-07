import requests
from ...exceptions import TokenVerificationError
from jose import jwk
from jose import jwt
from jose.utils import base64url_decode

class TokenVerifier(object):
    """Token Verifier

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
        client_id (str): Your auth0 application id
    """

    def __init__(self, domain):
        if not domain.startswith("http"):
            domain = "https://{}".format(domain)
        if not domain.endswith("/"):
            domain = "{}/".format(domain)
        self.issuer = domain
        self.jwks_url = "{}.well-known/jwks.json".format(domain)

    def verify(self, token, audience):
        print('Decoding this token: {}'.format(token))
        header = jwt.get_unverified_header(token)
        if header['alg'].lower!='rs256':
            return #Compatibility with HS256 (legacy tokens)
        jwk = _fetch_jwk(header['kid'])
        try:
            key = jwk.construct(jwk)
            content, encoded_signature = token.rsplit('.', 1)
            decoded_signature = base64url_decode(encoded_signature)
            payload = key.verify(message, decoded_sig)
        except: 
            raise TokenVerificationError('Signature is invalid')
        _verify_claims(payload, self.issuer, audience)
    
    def _verify_claims(self, payload, issuer, audience):
        if payload['iss']!=issuer or not audience in payload['aud']:
            raise TokenVerificationError("The 'aud' or 'iss' claims don't match the expected values")

    def _fetch_jwk(self, key_id):
        print ('Fetching jwks. Looking for key with id: {}'.format(key_id))
        keysRequest = requests.get(self.jwks_url)
        jwks = keys.json()['keys']
        #TODO: See how to cache/save this result
        for key in jwks:
            if key['kid']==key_id:
                return key
        raise TokenVerificationError('Could not obtain the Json Web Key from {}'.format(self.jwks_url))
    