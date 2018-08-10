import unittest
import mock
from ...authentication.social import Social


class TestSocial(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.social.Social.post')
    def test_login(self, mock_post, mock_token_verifier):

        s = Social('my.domain.com', mock_token_verifier)

         # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        s.login(client_id='cid', access_token='atk', connection='conn')

        args, kwargs = mock_post.call_args

        self.assertEqual('https://my.domain.com/oauth/access_token', args[0])
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'access_token': 'atk',
            'connection': 'conn',
            'scope': 'openid',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken'}

        s.login(client_id='cid', access_token='atk', connection='conn')

        mock_token_verifier.verify.assert_not_called()

    @mock.patch('auth0.v3.authentication.social.Social.post')
    def test_login_with_scope(self, mock_post):
        s = Social('my.domain.com')
        s.login(client_id='cid', access_token='atk',
                connection='conn', scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual('https://my.domain.com/oauth/access_token', args[0])
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'access_token': 'atk',
            'connection': 'conn',
            'scope': 'openid profile',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })
