import sys
import json
import base64
import requests
from ..exceptions import Auth0Error


class RestClient(object):

    """Provides simple methods for handling all RESTful api endpoints. """

    def __init__(self, jwt, telemetry=True):
        self.jwt = jwt

        if telemetry:
            py_version = '%i.%i.%i' % (sys.version_info.major,
                                       sys.version_info.minor,
                                       sys.version_info.micro)

            # FIXME: is there a nicer way to do this?
            from ... import __version__ as version

            auth0_client = json.dumps({
                'name': 'auth0-python', 'version': version,
                'dependencies': [
                    {
                        'name': 'requests',
                        'version': requests.__version__,
                    }
                ],
                'environment': [
                    {
                        'name': 'python',
                        'version': py_version,
                    }
                ]
            }).encode('utf-8')

            self.base_headers = {
                'User-Agent': 'Python/%s' % py_version,
                'Auth0-Client': base64.b64encode(auth0_client),
                'Content-Type': 'application/json'
            }
        else:
            self.base_headers = {}

    def get(self, url, params={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        response = requests.get(url, params=params, headers=headers)
        return self._process_response(response)

    def post(self, url, data={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        })

        response = requests.post(url, data=json.dumps(data), headers=headers)
        return self._process_response(response)

    def file_post(self, url, data={}, files={}):
        headers = self.base_headers.copy()
        headers.pop('Content-Type', None)
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        response = requests.post(url, data=data, files=files, headers=headers)
        return self._process_response(response)

    def patch(self, url, data={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        })

        response = requests.patch(url, data=json.dumps(data), headers=headers)
        return self._process_response(response)

    def delete(self, url):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        response = requests.delete(url, headers=headers)
        return self._process_response(response)

    def _process_response(self, response):
        text = json.loads(response.text) if response.text else {}

        if isinstance(text, dict) and 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text
