import unittest
import mock
from ...authentication.users import Users


class TestUsers(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.users.Users.get')
    def test_userinfo(self, mock_get):

        u = Users('my.domain.com')

        u.userinfo(access_token='atk')

        mock_get.assert_called_with(
            url='https://my.domain.com/userinfo',
            headers={'Authorization': 'Bearer atk'}
        )

    @mock.patch('auth0.v3.authentication.users.Users.post')
    def test_tokeninfo(self, mock_post):

        u = Users('my.domain.com')

        u.tokeninfo(jwt='jwtoken')

        mock_post.assert_called_with(
            url='https://my.domain.com/tokeninfo',
            data={'id_token': 'jwtoken'}
        )
