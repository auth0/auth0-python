import base64
import json
from time import sleep

import mock
import sys
import requests
import unittest
from ...authentication.base import AuthenticationBase
from ...exceptions import Auth0Error, RateLimitError


class TestBase(unittest.TestCase):

    def test_telemetry_enabled_by_default(self):
        ab = AuthenticationBase('auth0.com')

        user_agent = ab.base_headers['User-Agent']
        auth0_client_bytes = base64.b64decode(ab.base_headers['Auth0-Client'])
        auth0_client_json = auth0_client_bytes.decode('utf-8')
        auth0_client = json.loads(auth0_client_json)
        content_type = ab.base_headers['Content-Type']

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

    def test_telemetry_disabled(self):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        self.assertEqual(ab.base_headers, {'Content-Type': 'application/json'})

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False, timeout=(10, 2))

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"x": "y"}'

        data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        mock_post.assert_called_with(url='the-url', json={'a': 'b'},
                                     headers={'c': 'd', 'Content-Type': 'application/json'}, timeout=(10, 2))

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.post')
    def test_post_with_defaults(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"x": "y"}'

        # Only required params are passed
        data = ab.post('the-url')

        mock_post.assert_called_with(url='the-url', json=None,
                                     headers={'Content-Type': 'application/json'}, timeout=5.0)

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.post')
    def test_post_includes_telemetry(self, mock_post):
        ab = AuthenticationBase('auth0.com')

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"x": "y"}'

        data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        self.assertEqual(mock_post.call_count, 1)
        call_kwargs = mock_post.call_args[1]
        self.assertEqual(call_kwargs['url'], 'the-url')
        self.assertEqual(call_kwargs['json'], {'a': 'b'})
        headers = call_kwargs['headers']
        self.assertEqual(headers['c'], 'd')
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertIn('User-Agent', headers)
        self.assertIn('Auth0-Client', headers)

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.post')
    def test_post_error(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"error": "e0",' \
                                          '"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_rate_limit_error(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        mock_post.return_value.text = '{"statusCode": 429,' \
                                      ' "error": "e0",' \
                                      ' "error_description": "desc"}'
        mock_post.return_value.status_code = 429
        mock_post.return_value.headers = {
            'x-ratelimit-limit': '3',
            'x-ratelimit-remaining': '6',
            'x-ratelimit-reset': '9',
        }

        with self.assertRaises(Auth0Error) as context:
            ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, 'e0')
        self.assertEqual(context.exception.message, 'desc')
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, 9)

    @mock.patch('requests.post')
    def test_post_rate_limit_error_without_headers(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        mock_post.return_value.text = '{"statusCode": 429,' \
                                      ' "error": "e0",' \
                                      ' "error_description": "desc"}'
        mock_post.return_value.status_code = 429
        mock_post.return_value.headers = {}

        with self.assertRaises(Auth0Error) as context:
            ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, 'e0')
        self.assertEqual(context.exception.message, 'desc')
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, -1)

    @mock.patch('requests.post')
    def test_post_error_with_code_property(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"code": "e0",' \
                                          '"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_no_error_code(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code,
                             'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_text_response(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = 'there has been a terrible error'

            with self.assertRaises(Auth0Error) as context:
                ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code,
                             'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message,
                             'there has been a terrible error')

    @mock.patch('requests.post')
    def test_post_error_with_no_response_text(self, mock_post):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = None

            with self.assertRaises(Auth0Error) as context:
                ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code,
                             'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, '')

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        ab = AuthenticationBase('auth0.com', telemetry=False, timeout=(10, 2))

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"x": "y"}'

        data = ab.get('the-url', params={'a': 'b'}, headers={'c': 'd'})

        mock_get.assert_called_with(url='the-url', params={'a': 'b'},
                                    headers={'c': 'd', 'Content-Type': 'application/json'}, timeout=(10, 2))

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.get')
    def test_get_with_defaults(self, mock_get):
        ab = AuthenticationBase('auth0.com', telemetry=False)

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"x": "y"}'

        # Only required params are passed
        data = ab.get('the-url')

        mock_get.assert_called_with(url='the-url', params=None,
                                    headers={'Content-Type': 'application/json'}, timeout=5.0)

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.get')
    def test_get_includes_telemetry(self, mock_get):
        ab = AuthenticationBase('auth0.com')

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"x": "y"}'

        data = ab.get('the-url', params={'a': 'b'}, headers={'c': 'd'})

        self.assertEqual(mock_get.call_count, 1)
        call_kwargs = mock_get.call_args[1]
        self.assertEqual(call_kwargs['url'], 'the-url')
        self.assertEqual(call_kwargs['params'], {'a': 'b'})
        headers = call_kwargs['headers']
        self.assertEqual(headers['c'], 'd')
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertIn('User-Agent', headers)
        self.assertIn('Auth0-Client', headers)

        self.assertEqual(data, {"x": "y"})

    def test_get_can_timeout(self):
        ab = AuthenticationBase('auth0.com', timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            ab.get('https://google.com', params={'a': 'b'}, headers={'c': 'd'})

    def test_post_can_timeout(self):
        ab = AuthenticationBase('auth0.com', timeout=0.00001)

        with self.assertRaises(requests.exceptions.Timeout):
            ab.post('https://google.com', data={'a': 'b'}, headers={'c': 'd'})
