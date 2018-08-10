import unittest
import mock
from ...authentication.database import Database


class TestDatabase(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.database.Database.post')
    def test_login(self, mock_post, mock_token_verifier):

        d = Database('my.domain.com', mock_token_verifier)
        
        # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        d.login(client_id='cid',
                username='usrnm',
                password='pswd',
                id_token='idt',
                connection='conn',
                device='dev',
                grant_type='gt',
                scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'username': 'usrnm',
            'password': 'pswd',
            'id_token': 'idt',
            'connection': 'conn',
            'device': 'dev',
            'grant_type': 'gt',
            'scope': 'openid profile',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })
        
        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will not return id_token
        mock_post.return_value = {'access_token': 'accessToken'}

        d.login(client_id='cid',
                username='usrnm',
                password='pswd',
                id_token='idt',
                connection='conn',
                device='dev',
                grant_type='gt',
                scope='openid profile')

        mock_token_verifier.verify.assert_not_called()

    @mock.patch('auth0.v3.authentication.database.Database.post')
    def test_signup(self, mock_post):

        d = Database('my.domain.com')

        d.signup(client_id='cid',
                 email='a@b.com',
                 password='pswd',
                 connection='conn')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/dbconnections/signup')
        self.assertEqual(kwargs['data'], {
             'client_id': 'cid',
             'email': 'a@b.com',
             'password': 'pswd',
             'connection': 'conn',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0.v3.authentication.database.Database.post')
    def test_change_password(self, mock_post):

        d = Database('my.domain.com')

        d.change_password(client_id='cid',
                          email='a@b.com',
                          password='pswd',
                          connection='conn')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0],
            'https://my.domain.com/dbconnections/change_password')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'email': 'a@b.com',
            'password': 'pswd',
            'connection': 'conn',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })
