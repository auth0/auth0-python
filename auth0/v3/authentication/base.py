import json
import requests
from ..exceptions import Auth0Error, TokenVerificationError
from jose import jwk
from jose import jwt
from jose.utils import base64url_decode

UNKNOWN_ERROR = 'a0.sdk.internal.unknown'


class AuthenticationBase(object):

    def post(self, url, data=None, headers=None):
        response = requests.post(url=url, data=json.dumps(data),
                                 headers=headers)
        return self._process_response(response)

    def get(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers).text

    def _process_response(self, response):
        return self._parse(response).content()

    def _parse(self, response):
        if not response.text:
            return EmptyResponse(response.status_code)
        try:
            return JsonResponse(response)
        except ValueError:
            return PlainResponse(response)

    def _fetch_jwk(domain, kid):
        print('Fetching jwks. Looking for kid: ' + kid)
        if not domain.startsWith("http"):
            domain = "https://{}".format(domain)
        if not domain.endswith("/"):
            domain = "{}/".format(domain)
        jwks_url = "{}.well-known/jwks.json".format(domain)
        keysRequest = requests.get(jwks_url)
        jwks = keys.json()['keys']
        #TODO: See how to cache/save this result
        for key in jwks:
            if key['kid']==kid
                return key
        raise TokenVerificationError('Could not obtain the Json Web Key from {}'.format(jwks_url))
        
    def verify_id_token(self, id_token, domain, client_id):
        header = jwt.get_unverified_header(id_token)
        if header['alg'].lower!='rs256': return #Compatibility with HS256 (legacy tokens)
        jwk = self._fetch_jwk(domain, header['kid'])
        try:
            key = jwk.construct(jwk)
            content, encoded_signature = token.rsplit('.', 1)
            decoded_signature = base64url_decode(encoded_signature)
            payload = key.verify(message, decoded_sig)
        except: 
            raise TokenVerificationError('Signature is invalid')
        if payload['iss']!=domain or not client_id in payload['aud']:
            raise TokenVerificationError("The 'aud' or 'iss' claims don't match the expected values")


class Response(object):
    def __init__(self, status_code, content):
        self._status_code = status_code
        self._content = content

    def content(self):
        if self._is_error():
            raise Auth0Error(status_code=self._status_code,
                             error_code=self._error_code(),
                             message=self._error_message())
        else:
            return self._content

    def _is_error(self):
        return self._status_code is None or self._status_code >= 400

    # Adding these methods to force implementation in subclasses because they are references in this parent class
    def _error_code(self):
        raise NotImplementedError

    def _error_message(self):
        raise NotImplementedError


class JsonResponse(Response):
    def __init__(self, response):
        content = json.loads(response.text)
        super(JsonResponse, self).__init__(response.status_code, content)

    def _error_code(self):
        if 'error' in self._content:
            return self._content.get('error')
        elif 'code' in self._content:
            return self._content.get('code')
        else:
            return UNKNOWN_ERROR

    def _error_message(self):
        return self._content.get('error_description', '')


class PlainResponse(Response):
    def __init__(self, response):
        super(PlainResponse, self).__init__(response.status_code, response.text)

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return self._content


class EmptyResponse(Response):
    def __init__(self, status_code):
        super(EmptyResponse, self).__init__(status_code, '')

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return ''
