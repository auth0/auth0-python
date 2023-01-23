import unittest
from unittest import mock

from ...authentication.database import Database


class TestDatabase(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_signup(self, mock_post):
        d = Database("my.domain.com", "cid")

        # using only email and password
        d.signup(email="a@b.com", password="pswd", connection="conn")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/dbconnections/signup")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "email": "a@b.com",
                "password": "pswd",
                "connection": "conn",
            },
        )

        # Using also optional properties
        sample_meta = {"hobby": "surfing", "preference": {"color": "pink"}}
        d.signup(
            email="a@b.com",
            password="pswd",
            connection="conn",
            username="usr",
            user_metadata=sample_meta,
            given_name="john",
            family_name="doe",
            name="john doe",
            nickname="johnny",
            picture="avatars.com/john-doe",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/dbconnections/signup")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "email": "a@b.com",
                "password": "pswd",
                "connection": "conn",
                "username": "usr",
                "user_metadata": sample_meta,
                "given_name": "john",
                "family_name": "doe",
                "name": "john doe",
                "nickname": "johnny",
                "picture": "avatars.com/john-doe",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_change_password(self, mock_post):
        d = Database("my.domain.com", "cid")

        # ignores the password argument
        d.change_password(email="a@b.com", password="pswd", connection="conn")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/dbconnections/change_password")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "email": "a@b.com",
                "connection": "conn",
            },
        )
