import json
import requests
from ..exceptions import Auth0Error


class AuthenticationBase(object):

    def post(self, url, data={}, headers={}):
        response = requests.post(url=url, data=json.dumps(data),
                                 headers=headers)
        return self._process_response(response)

    def get(self, url, params={}, headers={}):
        return requests.get(url=url, params=params, headers=headers).text

    def _process_response(self, response):
        text = json.loads(response.text) if response.text else {}

        if 'error' in text:
            raise Auth0Error(status_code=text['error'],
                             error_code=text['error'],
                             message=text['error_description'])
        return text
