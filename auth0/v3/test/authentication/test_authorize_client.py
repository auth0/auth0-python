import unittest
from requests.compat import quote

import mock
from ...authentication.authorize_client import AuthorizeClient


class TestAuthorizeClient(unittest.TestCase):

    def test_get_authorize_url(self):
        expected_result = 'https://my.domain.com/authorize' \
                          '?client_id=cid' \
                          '&audience=https%3A%2F%2Ftest.com%2Fapi' \
                          '&state=st+ate' \
                          '&redirect_uri=http%3A%2F%2Flocalhost%3Fcallback' \
                          '&response_type=code' \
                          '&scope=openid'

        a = AuthorizeClient('my.domain.com')

        result = a.get_authorize_url(
            client_id='cid',
            audience='https://test.com/api',
            state='st ate',
            redirect_uri='http://localhost?callback',
        )

        self.assertEqual(result, expected_result)

    def test_get_authorize_url_quote(self):
        expected_result = 'https://my.domain.com/authorize' \
                          '?client_id=cid' \
                          '&audience=https%3A%2F%2Ftest.com%2Fapi%3Ffoo%3Dbar' \
                          '&state=st%20ate' \
                          '&redirect_uri=http%3A%2F%2Flocalhost%3Fcallback' \
                          '&response_type=code' \
                          '&scope=openid'

        a = AuthorizeClient('my.domain.com')

        result = a.get_authorize_url(
            quote_via=quote,
            client_id='cid',
            audience='https://test.com/api?foo=bar',
            state='st ate',
            redirect_uri='http://localhost?callback',
        )

        self.assertEqual(result, expected_result)

    @mock.patch('auth0.v3.authentication.authorize_client.AuthorizeClient.get')
    def test_login(self, mock_get):

        a = AuthorizeClient('my.domain.com')

        a.authorize(client_id='cid',
                    audience='https://test.com/api',
                    state='st',
                    redirect_uri='http://localhost',
                    response_type='token',
                    scope='openid profile')

        args, kwargs = mock_get.call_args

        self.assertEqual(args[0], 'https://my.domain.com/authorize')
        self.assertEqual(kwargs['params'], {
            'client_id': 'cid',
            'audience': 'https://test.com/api',
            'state': 'st',
            'redirect_uri': 'http://localhost',
            'response_type': 'token',
            'scope': 'openid profile'
        })
