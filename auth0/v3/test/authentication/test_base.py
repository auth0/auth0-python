import unittest
import mock
from ...authentication.base import AuthenticationBase
from ...exceptions import Auth0Error


class TestBase(unittest.TestCase):

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        ab = AuthenticationBase()

        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"x": "y"}'

        data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        mock_post.assert_called_with(url='the-url', data='{"a": "b"}',
                                     headers={'c': 'd'})

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.post')
    def test_post_error(self, mock_post):
        ab = AuthenticationBase()

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"error": "e0",' \
                                          '"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_code_property(self, mock_post):
        ab = AuthenticationBase()

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"code": "e0",' \
                                          '"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'e0')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_no_error_code(self, mock_post):
        ab = AuthenticationBase()

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = '{"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, 'desc')

    @mock.patch('requests.post')
    def test_post_error_with_text_response(self, mock_post):
        ab = AuthenticationBase()

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = 'there has been a terrible error'

            with self.assertRaises(Auth0Error) as context:
                data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message,
                             'there has been a terrible error')

    @mock.patch('requests.post')
    def test_post_error_with_no_response_text(self, mock_post):
        ab = AuthenticationBase()

        for error_status in [400, 500, None]:
            mock_post.return_value.status_code = error_status
            mock_post.return_value.text = None

            with self.assertRaises(Auth0Error) as context:
                data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, 'a0.sdk.internal.unknown')
            self.assertEqual(context.exception.message, '')
