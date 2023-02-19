import unittest
from unittest import mock

from ...authentication.users import Users


class TestUsers(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.get")
    def test_userinfo(self, mock_get):
        u = Users("my.domain.com")

        u.userinfo(access_token="atk")

        mock_get.assert_called_with(
            url="https://my.domain.com/userinfo",
            headers={"Authorization": "Bearer atk"},
        )
