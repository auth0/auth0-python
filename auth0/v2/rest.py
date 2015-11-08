import json
import requests
from .exceptions import Auth0Error


class RestClient(object):

    """Provides simple methods for handling all RESTful api endpoints. """

    def __init__(self, jwt):
        self.jwt = jwt

    def get(self, url, params={}):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
        }

        response = requests.get(url, params=params, headers=headers)
        return self._process_response(response)

    def post(self, url, data={}):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)
        return self._process_response(response)

    def patch(self, url, data={}):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        }

        response = requests.patch(url, data=json.dumps(data), headers=headers)
        return self._process_response(response)

    def delete(self, url):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
        }

        response = requests.delete(url, headers=headers)
        return self._process_response(response)

    def _process_response(self, response):
        text = json.loads(response.text) if response.text else {}

        if isinstance(text, dict) and 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text
