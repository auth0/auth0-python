import unittest
import mock
from ...authentication.passwordless import Passwordless


class TestPasswordless(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_email(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email(client_id='cid',
                email='a@b.com',
                send='snd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'email': 'a@b.com',
            'send': 'snd',
            'connection': 'email',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_email_with_auth_params(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email(client_id='cid',
                email='a@b.com',
                send='snd',
                auth_params={'a': 'b'})

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'email': 'a@b.com',
            'send': 'snd',
            'authParams': {'a': 'b'},
            'connection': 'email',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_email_with_client_secret(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email(client_id='cid',
                client_secret='csecret',
                email='a@b.com',
                send='snd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'csecret',
            'email': 'a@b.com',
            'send': 'snd',
            'connection': 'email',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_sms(self, mock_post):
        p = Passwordless('my.domain.com')

        p.sms(client_id='cid', phone_number='123456')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'phone_number': '123456',
            'connection': 'sms',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_sms_with_client_secret(self, mock_post):
        p = Passwordless('my.domain.com')

        p.sms(client_id='cid', client_secret='csecret', phone_number='123456')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/passwordless/start')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'csecret',
            'phone_number': '123456',
            'connection': 'sms',
        })
        
    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_login_with_phone(self, mock_post):

        p = Passwordless('my.domain.com')

        p.login(
                client_id='cid',
                client_secret='csec',
                username='123456',
                realm='sms',
                otp='abcd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'csec',
            'realm': 'sms',
            'grant_type': 'http://auth0.com/oauth/grant-type/passwordless/otp',
            'username': '123456',
            'otp': 'abcd',
            'audience': '',
            'scope': 'openid',
        })


    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_login_with_email(self, mock_post):

        p = Passwordless('my.domain.com')

        p.login(
                client_id='cid',
                client_secret='csec',
                username='a@b',
                realm='email',
                otp='abcd',
                scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'csec',
            'realm': 'email',
            'grant_type': 'http://auth0.com/oauth/grant-type/passwordless/otp',
            'username': 'a@b.com',
            'otp': 'abcd',
            'audience': '',
            'scope': 'openid profile',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_sms_login(self, mock_post):

        p = Passwordless('my.domain.com')

        p.sms_login(client_id='cid', phone_number='123456', code='abcd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'sms',
            'grant_type': 'password',
            'username': '123456',
            'password': 'abcd',
            'scope': 'openid',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_sms_login_with_scope(self, mock_post):

        p = Passwordless('my.domain.com')

        p.sms_login(client_id='cid', phone_number='123456',
                    code='abcd', scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'sms',
            'grant_type': 'password',
            'username': '123456',
            'password': 'abcd',
            'scope': 'openid profile',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_email_legacy_login(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email_login(client_id='cid', email='a@b.com', code='abcd')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'email',
            'grant_type': 'password',
            'username': 'a@b.com',
            'password': 'abcd',
            'scope': 'openid',
        })

    @mock.patch('auth0.v3.authentication.passwordless.Passwordless.post')
    def test_email_login_legacy_with_scope(self, mock_post):

        p = Passwordless('my.domain.com')

        p.email_login(client_id='cid', email='a@b.com',
                    code='abcd', scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/ro')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'connection': 'email',
            'grant_type': 'password',
            'username': 'a@b.com',
            'password': 'abcd',
            'scope': 'openid profile',
        })

