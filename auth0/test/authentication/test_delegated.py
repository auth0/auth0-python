import unittest
from unittest import mock

from ...authentication.delegated import Delegated


class TestDelegated(unittest.TestCase):
    @mock.patch("auth0.authentication.delegated.Delegated.post")
    def test_get_token_id_token(self, mock_post):
        d = Delegated("my.domain.com", "cid")

        d.get_token(
            target="tgt",
            api_type="apt",
            grant_type="gt",
            id_token="idt",
            scope="openid profile",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/delegation")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "grant_type": "gt",
                "id_token": "idt",
                "target": "tgt",
                "scope": "openid profile",
                "api_type": "apt",
            },
        )

    @mock.patch("auth0.authentication.delegated.Delegated.post")
    def test_get_token_refresh_token(self, mock_post):
        d = Delegated("my.domain.com", "cid")

        d.get_token(
            target="tgt",
            api_type="apt",
            grant_type="gt",
            refresh_token="rtk",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/delegation")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "grant_type": "gt",
                "refresh_token": "rtk",
                "target": "tgt",
                "scope": "openid",
                "api_type": "apt",
            },
        )

    @mock.patch("auth0.authentication.delegated.Delegated.post")
    def test_get_token_value_error(self, mock_post):
        d = Delegated("my.domain.com", "cid")

        with self.assertRaises(ValueError):
            d.get_token(
                target="tgt",
                api_type="apt",
                grant_type="gt",
                refresh_token="rtk",
                id_token="idt",
            )
