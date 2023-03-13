import unittest
from unittest import mock

from ...authentication.passwordless import Passwordless


class TestPasswordless(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_send_email(self, mock_post):
        p = Passwordless("my.domain.com", "cid")

        p.email(email="a@b.com", send="snd")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/passwordless/start")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "email": "a@b.com",
                "send": "snd",
                "connection": "email",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_send_email_with_auth_params(self, mock_post):
        p = Passwordless("my.domain.com", "cid")

        p.email(email="a@b.com", send="snd", auth_params={"a": "b"})

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/passwordless/start")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "email": "a@b.com",
                "send": "snd",
                "authParams": {"a": "b"},
                "connection": "email",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_send_email_with_client_secret(self, mock_post):
        p = Passwordless("my.domain.com", "cid", client_secret="csecret")

        p.email(email="a@b.com", send="snd")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/passwordless/start")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "csecret",
                "email": "a@b.com",
                "send": "snd",
                "connection": "email",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_send_sms(self, mock_post):
        p = Passwordless("my.domain.com", "cid")

        p.sms(phone_number="123456")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/passwordless/start")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "phone_number": "123456",
                "connection": "sms",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_send_sms_with_client_secret(self, mock_post):
        p = Passwordless("my.domain.com", "cid", client_secret="csecret")

        p.sms(phone_number="123456")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/passwordless/start")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "csecret",
                "phone_number": "123456",
                "connection": "sms",
            },
        )
