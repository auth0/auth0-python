import unittest
from unittest import mock

from ...authentication.revoke_token import RevokeToken


class TestRevokeToken(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_revoke_refresh_token(self, mock_post):
        a = RevokeToken("my.domain.com", "cid")

        # regular apps
        a.revoke_refresh_token(token="tkn")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/revoke")
        self.assertEqual(kwargs["data"], {"client_id": "cid", "token": "tkn"})

        # confidential apps
        a = RevokeToken("my.domain.com", "cid", client_secret="sh!")
        a.revoke_refresh_token(token="tkn")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/revoke")
        self.assertEqual(
            kwargs["data"], {"client_id": "cid", "token": "tkn", "client_secret": "sh!"}
        )
