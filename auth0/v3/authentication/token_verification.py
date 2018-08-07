import requests
from ..exceptions import TokenVerificationError
from jose import jwk
from jose import jwt
from jose.utils import base64url_decode

def token_verification(request_function):
    def verification(*args, **kwargs):
        print("Called with args: {} and kwards: {}".format(args, kwargs))
        result = request_function(*args, **kwargs)
        id_token = result and result['id_token']
        if id_token:
            client_id = kwargs['client_id'] or args[1]
            _verify_id_token(id_token, args[0].domain, client_id)
        return result
    return verification

if __name__ == "__main__":
    verification()

def _verify_id_token(id_token, domain, client_id):
    print ('Attempting to verify the token using domain {} and client id {}'.format(domain, client_id))
    header = jwt.get_unverified_header(id_token)
    if header['alg'].lower!='rs256': return #Compatibility with HS256 (legacy tokens)
    jwk = _fetch_jwk(domain, header['kid'])
    try:
        key = jwk.construct(jwk)
        content, encoded_signature = token.rsplit('.', 1)
        decoded_signature = base64url_decode(encoded_signature)
        payload = key.verify(message, decoded_sig)
    except: 
        raise TokenVerificationError('Signature is invalid')
    if payload['iss']!=domain or not client_id in payload['aud']:
        raise TokenVerificationError("The 'aud' or 'iss' claims don't match the expected values")

def _fetch_jwk(domain, key_id):
    print ('Fetching jwks. Looking for key with id: {}'.format(key_id))
    if not domain.startsWith("http"):
        domain = "https://{}".format(domain)
    if not domain.endswith("/"):
        domain = "{}/".format(domain)
    jwks_url = "{}.well-known/jwks.json".format(domain)
    keysRequest = requests.get(jwks_url)
    jwks = keys.json()['keys']
    #TODO: See how to cache/save this result
    for key in jwks:
        if key['kid']==key_id:
            return key
    raise TokenVerificationError('Could not obtain the Json Web Key from {}'.format(jwks_url))
    