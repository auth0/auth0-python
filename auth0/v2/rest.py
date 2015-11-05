import json
import requests
from .exceptions import Auth0Error


class RestClient(object):

    """Provides simple methods for handling all RESTful api endpoints. """

    def __init__(self, endpoint, jwt):
        self.endpoint = endpoint
        self.jwt = jwt

    def get(self, params={}, id=None):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
        }

        url = self.endpoint
        if id is not None:
            url += '/%s' % id

        response = requests.get(url, params=params, headers=headers)

        text = json.loads(response.text) if response.text else {}

        if 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text

    def post(self, data={}, id=None):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        }

        url = self.endpoint
        if id is not None:
            url += '/%s' % id

        response = requests.post(url, data=json.dumps(data), headers=headers)

        text = json.loads(response.text) if response.text else {}

        if 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text

    def patch(self, data={}, id=None):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        }

        url = self.endpoint
        if id is not None:
            url += '/%s' % id

        response = requests.patch(url, data=json.dumps(data), headers=headers)

        text = json.loads(response.text) if response.text else {}

        if 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text

    def delete(self, id):
        headers = {
            'Authorization': 'Bearer %s' % self.jwt,
        }

        url = self.endpoint
        if id is not None:
            url += '/%s' % id

        response = requests.delete(url, headers=headers)

        text = json.loads(response.text) if response.text else {}

        if 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text
