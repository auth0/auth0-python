import unittest
import mock
from ...authentication.get_token import GetToken


class TestGetToken(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.get_token.GetToken.post')
    def test_authorization_code(self, mock_post, mock_token_verifier):

        g = GetToken('my.domain.com', mock_token_verifier)

        # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        g.authorization_code(client_id='cid',
                             client_secret='clsec',
                             code='cd',
                             grant_type='gt',
                             redirect_uri='idt')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/token')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'clsec',
            'code': 'cd',
            'grant_type': 'gt',
            'redirect_uri': 'idt'
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken'}

        g.authorization_code(client_id='cid',
                             client_secret='clsec',
                             code='cd',
                             grant_type='gt',
                             redirect_uri='idt')

        mock_token_verifier.verify.assert_not_called()


    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.get_token.GetToken.post')
    def test_authorization_code_pkce(self, mock_post, mock_token_verifier):

        g = GetToken('my.domain.com', mock_token_verifier)

        # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        g.authorization_code_pkce(client_id='cid',
                                  code_verifier='cdver',
                                  code='cd',
                                  grant_type='gt',
                                  redirect_uri='idt')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/token')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'code_verifier': 'cdver',
            'code': 'cd',
            'grant_type': 'gt',
            'redirect_uri': 'idt'
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken'}

        g.authorization_code_pkce(client_id='cid',
                                  code_verifier='cdver',
                                  code='cd',
                                  grant_type='gt',
                                  redirect_uri='idt')

        mock_token_verifier.verify.assert_not_called()

    @mock.patch('auth0.v3.authentication.get_token.GetToken.post')
    def test_client_credentials(self, mock_post):

        g = GetToken('my.domain.com')

        g.client_credentials(client_id='cid',
                             client_secret='clsec',
                             audience='aud',
                             grant_type='gt')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/token')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'clsec',
            'audience': 'aud',
            'grant_type': 'gt'
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.get_token.GetToken.post')
    def test_login(self, mock_post, mock_token_verifier):

        g = GetToken('my.domain.com', mock_token_verifier)

         # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        g.login(client_id='cid',
                client_secret='clsec',
                username='usrnm',
                password='pswd',
                scope='http://test.com/api',
                realm='rlm',
                audience='aud',
                grant_type='gt')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/token')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'clsec',
            'username':'usrnm',
            'password':'pswd',
            'scope':'http://test.com/api',
            'realm':'rlm',
            'audience': 'aud',
            'grant_type': 'gt'
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken'}

        g.login(client_id='cid',
                client_secret='clsec',
                username='usrnm',
                password='pswd',
                scope='http://test.com/api',
                realm='rlm',
                audience='aud',
                grant_type='gt')

        mock_token_verifier.verify.assert_not_called()

    @mock.patch('auth0.v3.authentication.utils.token_verifier.TokenVerifier')
    @mock.patch('auth0.v3.authentication.get_token.GetToken.post')
    def test_refresh_token(self, mock_post, mock_token_verifier):

        g = GetToken('my.domain.com', mock_token_verifier)

         # CALL 1: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken', 'id_token': 'idToken'}

        g.refresh_token(client_id='cid',
                        client_secret='clsec',
                        refresh_token='rt',
                        grant_type='gt')

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], 'https://my.domain.com/oauth/token')
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'client_secret': 'clsec',
            'refresh_token': 'rt',
            'grant_type': 'gt'
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })

        mock_token_verifier.verify.assert_called_with('idToken', 'my.domain.com', 'cid')
        mock_token_verifier.reset_mock()

        # CALL 2: Will return id_token, which will get verified
        mock_post.return_value = {'access_token': 'accessToken'}

        g.refresh_token(client_id='cid',
                        client_secret='clsec',
                        refresh_token='rt',
                        grant_type='gt')

        mock_token_verifier.verify.assert_not_called()