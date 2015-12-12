import unittest
import mock
from ...authentication.base import AuthenticationBase
from ...exceptions import Auth0Error


class TestBase(unittest.TestCase):

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        ab = AuthenticationBase()

        mock_post.return_value.text = '{"x": "y"}'

        data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        mock_post.assert_called_with(url='the-url', data='{"a": "b"}',
                                     headers={'c': 'd'})

        self.assertEqual(data, {'x': 'y'})

    @mock.patch('requests.post')
    def test_post_error(self, mock_post):
        ab = AuthenticationBase()

        mock_post.return_value.text = '{"error": "e0",' \
                                      '"error_description": "desc"}'

        with self.assertRaises(Auth0Error) as context:
            data = ab.post('the-url', data={'a': 'b'}, headers={'c': 'd'})

        self.assertEqual(context.exception.status_code, 'e0')
        self.assertEqual(context.exception.error_code, 'e0')
        self.assertEqual(context.exception.message, 'desc')
