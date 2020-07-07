import unittest
import mock
from ...authentication.revoke_token import RevokeToken


class TestRevokeToken(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.revoke_token.RevokeToken.post')
    def test_revoke_refresh_token(self, mock_post):

        a = RevokeToken('my.domain.com')

        # regular apps
        a.revoke_refresh_token(client_id='cid', token='tkn')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/revoke')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'token': 'tkn'
        })

        # confidential apps
        a.revoke_refresh_token(client_id='cid',
                    token='tkn',
                    client_secret='sh!')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/revoke')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'token': 'tkn',
            'client_secret': 'sh!'
        })
