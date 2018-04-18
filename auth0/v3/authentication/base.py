import json
import requests
from ..exceptions import Auth0Error


class AuthenticationBase(object):

    def post(self, url, data=None, headers=None):
        response = requests.post(url=url, data=json.dumps(data),
                                 headers=headers)
        return self._process_response(response)

    def get(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers).text

    def _process_response(self, response):
        try:
            text = json.loads(response.text) if response.text else {}
        except ValueError:
            return response.text
        else:
            if response.status_code is None or response.status_code >= 400:
                raise Auth0Error(status_code=response.status_code,
                                 error_code=text.get('error', ''),
                                 message=text.get('error_description', ''))
        return text
