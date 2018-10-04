import unittest
from requests.compat import quote, urlparse

import mock
from ...authentication.authorize_client import AuthorizeClient


class TestAuthorizeClient(unittest.TestCase):

    def test_get_authorize_url(self):
        expected_result = urlparse(
            'https://my.domain.com/authorize'
            '?client_id=cid'
            '&audience=https%3A%2F%2Ftest.com%2Fapi'
            '&state=st+ate'
            '&redirect_uri=http%3A%2F%2Flocalhost%3Fcallback'
            '&response_type=code'
            '&scope=openid+profile')

        a = AuthorizeClient('my.domain.com')

        actual_result = urlparse(a.get_authorize_url(
            client_id='cid',
            audience='https://test.com/api',
            state='st ate',
            redirect_uri='http://localhost?callback',
            scope='openid profile'
        ))

        self.assertEqual(actual_result.scheme, expected_result.scheme)
        self.assertEqual(actual_result.hostname, expected_result.hostname)
        self.assertEqual(actual_result.path, expected_result.path)

        # there is no guarantee the order of items in the query is equal to the method call, that's okay
        expected_query = expected_result.query.split('&')
        actual_query = actual_result.query.split('&')
        self.assertEqual(sorted(expected_query), sorted(actual_query))

    def test_get_authorize_url_quote(self):
        """
        sometimes we want to urlencode spaces into %20, we can do that with quote_via
        """
        expected_result = urlparse(
            'https://my.domain.com/authorize'
            '?client_id=cid'
            '&audience=https%3A%2F%2Ftest.com%2Fapi%3Ffoo%3Dbar'
            '&state=st%20ate'
            '&redirect_uri=http%3A%2F%2Flocalhost%3Fcallback%3D%23123'
            '&response_type=code'
            '&scope=openid%20profile'
        )
        a = AuthorizeClient('my.domain.com')

        actual_result = urlparse(a.get_authorize_url(
            client_id='cid',
            audience='https://test.com/api?foo=bar',
            state='st ate',
            redirect_uri='http://localhost?callback=#123',
            quote_via=quote,
            scope='openid profile'
        ))

        self.assertEqual(actual_result.scheme, expected_result.scheme)
        self.assertEqual(actual_result.hostname, expected_result.hostname)
        self.assertEqual(actual_result.path, expected_result.path)

        # there is no guarantee the order of items in the query is equal to the method call, that's okay
        expected_query = expected_result.query.split('&')
        actual_query = actual_result.query.split('&')
        self.assertEqual(sorted(expected_query), sorted(actual_query))

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
