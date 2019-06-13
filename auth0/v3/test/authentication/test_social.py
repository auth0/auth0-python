import unittest
import mock
from ...authentication.social import Social


class TestSocial(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.social.Social.post')
    def test_login(self, mock_post):
        s = Social('a.b.c')
        s.login(client_id='cid', access_token='atk', connection='conn')

        args, kwargs = mock_post.call_args

        self.assertEqual('https://a.b.c/oauth/access_token', args[0])
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'access_token': 'atk',
            'connection': 'conn',
            'scope': 'openid',
        })

    @mock.patch('auth0.v3.authentication.social.Social.post')
    def test_login_with_scope(self, mock_post):
        s = Social('a.b.c')
        s.login(client_id='cid', access_token='atk',
                connection='conn', scope='openid profile')

        args, kwargs = mock_post.call_args

        self.assertEqual('https://a.b.c/oauth/access_token', args[0])
        self.assertEqual(kwargs['data'], {
            'client_id': 'cid',
            'access_token': 'atk',
            'connection': 'conn',
            'scope': 'openid profile',
        })
