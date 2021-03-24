import unittest
import mock
from ...authentication.authorize_client import AuthorizeClient


class TestAuthorizeClient(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.authorize_client.AuthorizeClient.get')
    def test_login(self, mock_get):

        a = AuthorizeClient('my.domain.com')

        a.authorize(client_id='cid',
                    audience='https://test.com/api',
                    state='st',
                    redirect_uri='http://localhost',
                    response_type='token',
                    scope='openid profile',
                    organization='org_123',
                    invitation='invitation_abc')

        args, kwargs = mock_get.call_args

        self.assertEqual(args[0], 'https://my.domain.com/authorize')
        self.assertEqual(kwargs['params'], {
            'client_id': 'cid',
            'audience': 'https://test.com/api',
            'state': 'st',
            'redirect_uri': 'http://localhost',
            'response_type': 'token',
            'scope': 'openid profile',
            'organization': 'org_123',
            'invitation': 'invitation_abc'
        })

    @mock.patch('auth0.v3.authentication.authorize_client.AuthorizeClient.get')
    def test_login_default_param_values(self, mock_get):

        a = AuthorizeClient('my.domain.com')

        a.authorize(client_id='cid')

        args, kwargs = mock_get.call_args

        self.assertEqual(args[0], 'https://my.domain.com/authorize')
        self.assertEqual(kwargs['params'], {
            'audience': None,
            'invitation': None,
            'organization':  None,
            'redirect_uri': None,
            'state': None,
            'client_id': 'cid',
            'response_type':  'code',
            'scope': 'openid'
        })
