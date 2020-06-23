import unittest
import sys
import json
import base64

import mock
import requests

from ...management.rest import RestClient
from ...exceptions import Auth0Error, RateLimitError


class TestRest(unittest.TestCase):

    def test_get_can_timeout(self):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            rc.get('http://google.com')

    def test_post_can_timeout(self):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            rc.post('http://google.com')

    def test_put_can_timeout(self):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            rc.put('http://google.com')

    def test_patch_can_timeout(self):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            rc.patch('http://google.com')

    def test_delete_can_timeout(self):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            rc.delete('http://google.com')

    @mock.patch('requests.get')
    def test_get_custom_timeout(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=(10, 2))
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }
        mock_get.return_value.text = '["a", "b"]'
        mock_get.return_value.status_code = 200

        rc.get('the-url')
        mock_get.assert_called_with('the-url', params=None, headers=headers, timeout=(10, 2))

    @mock.patch('requests.post')
    def test_post_custom_timeout(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=(10, 2))
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }
        mock_post.return_value.text = '["a", "b"]'
        mock_post.return_value.status_code = 200

        rc.post('the-url')
        mock_post.assert_called_with('the-url', json=None, headers=headers, timeout=(10, 2))

    @mock.patch('requests.put')
    def test_put_custom_timeout(self, mock_put):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=(10, 2))
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }
        mock_put.return_value.text = '["a", "b"]'
        mock_put.return_value.status_code = 200

        rc.put('the-url')
        mock_put.assert_called_with('the-url', json=None, headers=headers, timeout=(10, 2))

    @mock.patch('requests.patch')
    def test_patch_custom_timeout(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=(10, 2))
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }
        mock_patch.return_value.text = '["a", "b"]'
        mock_patch.return_value.status_code = 200

        rc.patch('the-url')
        mock_patch.assert_called_with('the-url', json=None, headers=headers, timeout=(10, 2))

    @mock.patch('requests.delete')
    def test_delete_custom_timeout(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False, timeout=(10, 2))
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }
        mock_delete.return_value.text = '["a", "b"]'
        mock_delete.return_value.status_code = 200

        rc.delete('the-url')
        mock_delete.assert_called_with('the-url', params={}, json=None, headers=headers, timeout=(10, 2))

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }

        mock_get.return_value.text = '["a", "b"]'
        mock_get.return_value.status_code = 200

        response = rc.get('the-url')
        mock_get.assert_called_with('the-url', params=None, headers=headers, timeout=5.0)

        self.assertEqual(response, ['a', 'b'])

        response = rc.get(url='the/url', params={'A': 'param', 'B': 'param'})
        mock_get.assert_called_with('the/url', params={'A': 'param',
                                                       'B': 'param'},
                                    headers=headers, timeout=5.0)
        self.assertEqual(response, ['a', 'b'])

        mock_get.return_value.text = ''
        response = rc.get('the/url')
        self.assertEqual(response, '')

    @mock.patch('requests.get')
    def test_get_errors(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_get.return_value.text = '{"statusCode": 999,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'
        mock_get.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.get('the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.get')
    def test_get_rate_limit_error(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_get.return_value.text = '{"statusCode": 429,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'
        mock_get.return_value.status_code = 429
        mock_get.return_value.headers = {
            'x-ratelimit-limit': '3',
            'x-ratelimit-remaining': '6',
            'x-ratelimit-reset': '9',
        }

        with self.assertRaises(Auth0Error) as context:
            rc.get('the/url')

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, 9)

    @mock.patch('requests.get')
    def test_get_rate_limit_error_without_headers(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_get.return_value.text = '{"statusCode": 429,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'
        mock_get.return_value.status_code = 429
        
        mock_get.return_value.headers = {}
        with self.assertRaises(Auth0Error) as context:
            rc.get('the/url')

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, -1)

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_post.return_value.text = '{"a": "b"}'

        data = {'some': 'data'}

        mock_post.return_value.status_code = 200
        response = rc.post('the/url', data=data)
        mock_post.assert_called_with('the/url', json=data,
                                     headers=headers, timeout=5.0)

        self.assertEqual(response, {'a': 'b'})

    @mock.patch('requests.post')
    def test_post_errors(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = '{"statusCode": 999,' \
                                      ' "errorCode": "code",' \
                                      ' "message": "message"}'
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post_errors_with_no_message_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code",
            "error": "error"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'error')

    @mock.patch('requests.post')
    def test_post_errors_with_no_message_or_error_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, '')

    @mock.patch('requests.post')
    def test_post_errors_with_message_and_error_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = json.dumps({
            "statusCode": 999,
            "errorCode": "code",
            "error": "error",
            "message": "message"
        })
        mock_post.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post_error_with_code_property(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"errorCode": "e0",' \
                                          '"message": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_no_error_code(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"message": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_text_response(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = 'there has been a terrible error'

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message,
                             'there has been a terrible error')

    @mock.patch('requests.post')
    def test_post_error_with_no_response_text(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = None

            with self.assertRaises(Auth0Error) as context:
                rc.post('the-url')

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, '')

    @mock.patch('requests.post')
    def test_file_post_content_type_is_none(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = 'Success'

        data = {'some': 'data'}
        files = [mock.Mock()]

        rc.file_post('the-url', data=data, files=files)

        mock_post.assert_called_once_with('the-url', data=data, files=files, headers=headers, timeout=5.0)

    @mock.patch('requests.put')
    def test_put(self, mock_put):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_put.return_value.text = '["a", "b"]'
        mock_put.return_value.status_code = 200

        data = {'some': 'data'}

        response = rc.put(url='the-url', data=data)
        mock_put.assert_called_with('the-url', json=data,
                                    headers=headers, timeout=5.0)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.put')
    def test_put_errors(self, mock_put):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_put.return_value.text = '{"statusCode": 999,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'
        mock_put.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.put(url='the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.patch')
    def test_patch(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_patch.return_value.text = '["a", "b"]'
        mock_patch.return_value.status_code = 200

        data = {'some': 'data'}

        response = rc.patch(url='the-url', data=data)
        mock_patch.assert_called_with('the-url', json=data,
                                      headers=headers, timeout=5.0)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.patch')
    def test_patch_errors(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_patch.return_value.text = '{"statusCode": 999,' \
                                       ' "errorCode": "code",' \
                                       ' "message": "message"}'
        mock_patch.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.patch(url='the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.delete')
    def test_delete(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }

        mock_delete.return_value.text = '["a", "b"]'
        mock_delete.return_value.status_code = 200

        response = rc.delete(url='the-url/ID')
        mock_delete.assert_called_with('the-url/ID', headers=headers, params={}, json=None, timeout=5.0)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.delete')
    def test_delete_with_body_and_params(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {
            'Authorization': 'Bearer a-token',
            'Content-Type': 'application/json',
        }

        mock_delete.return_value.text = '["a", "b"]'
        mock_delete.return_value.status_code = 200

        data = {'some': 'data'}
        params = {'A': 'param', 'B': 'param'}

        response = rc.delete(url='the-url/ID', params=params, data=data)
        mock_delete.assert_called_with('the-url/ID', headers=headers, params=params, json=data, timeout=5.0)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.delete')
    def test_delete_errors(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_delete.return_value.text = '{"statusCode": 999,' \
                                        ' "errorCode": "code",' \
                                        ' "message": "message"}'
        mock_delete.return_value.status_code = 999

        with self.assertRaises(Auth0Error) as context:
            rc.delete(url='the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    def test_disabled_telemetry(self):
        rc = RestClient(jwt='a-token', telemetry=False)
        expected_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer a-token',
        }

        self.assertEqual(rc.base_headers, expected_headers)

    def test_enabled_telemetry(self):
        rc = RestClient(jwt='a-token', telemetry=True)

        user_agent = rc.base_headers['User-Agent']
        auth0_client_bytes = base64.b64decode(rc.base_headers['Auth0-Client'])
        auth0_client_json = auth0_client_bytes.decode('utf-8')
        auth0_client = json.loads(auth0_client_json)
        content_type = rc.base_headers['Content-Type']

        from auth0 import __version__ as auth0_version
        python_version = '{}.{}.{}'.format(sys.version_info.major,
                                           sys.version_info.minor,
                                           sys.version_info.micro)

        client_info = {
            'name': 'auth0-python',
            'version': auth0_version,
            'env': {
                'python': python_version
            }
        }

        self.assertEqual(user_agent, 'Python/{}'.format(python_version))
        self.assertEqual(auth0_client, client_info)
        self.assertEqual(content_type, 'application/json')
