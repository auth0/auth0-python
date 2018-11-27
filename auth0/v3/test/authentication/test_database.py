import unittest
import mock
from ...authentication.database import Database


class TestDatabase(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.database.Database.post')
    def test_login(self, mock_post):

        d = Database('my.domain.com')

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

    @mock.patch('auth0.v3.authentication.database.Database.post')
    def test_signup(self, mock_post):

        d = Database('my.domain.com')

        # using only email and password
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
                         'username': None,
                         'user_metadata': None
                        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })


        # Using also username and metadata
        sample_meta = {
            'hobby': 'surfing',
            'preference': {
                'color': 'pink'
            }
        }
        d.signup(client_id='cid',
                 email='a@b.com',
                 password='pswd',
                 connection='conn',
                 username='usr',
                 user_metadata=sample_meta)

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/dbconnections/signup')
        self.assertEqual(kwargs['data'], {
                         'client_id': 'cid',
                         'email': 'a@b.com',
                         'password': 'pswd',
                         'connection': 'conn',
                         'username': 'usr',
                         'user_metadata': sample_meta
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
