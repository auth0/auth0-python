import unittest
from unittest import mock

from ...management.connections import Connections


class TestConnection(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Connections(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.connections.RestClient")
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        # Default parameters are requested
        c = Connections(domain="domain", token="jwttoken")
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": None,
                "strategy": None,
                "page": None,
                "per_page": None,
                "include_fields": "true",
                "name": None,
            },
        )

        # Fields filter
        c.all(fields=["a", "b"], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": "a,b",
                "strategy": None,
                "page": None,
                "per_page": None,
                "include_fields": "false",
                "name": None,
            },
        )

        # Fields + strategy filter
        c.all(fields=["a", "b"], strategy="auth0", include_fields=True)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": "a,b",
                "strategy": "auth0",
                "page": None,
                "per_page": None,
                "include_fields": "true",
                "name": None,
            },
        )

        # Specific pagination
        c.all(page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": None,
                "strategy": None,
                "page": 7,
                "per_page": 25,
                "include_fields": "true",
                "name": None,
            },
        )

        # Extra parameters
        c.all(extra_params={"some_key": "some_value"})

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": None,
                "strategy": None,
                "page": None,
                "per_page": None,
                "include_fields": "true",
                "some_key": "some_value",
                "name": None,
            },
        )

        # Name
        c.all(name="foo")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/connections", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "fields": None,
                "strategy": None,
                "page": None,
                "per_page": None,
                "include_fields": "true",
                "name": "foo",
            },
        )

    @mock.patch("auth0.management.connections.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        c = Connections(domain="domain", token="jwttoken")
        c.get("an-id")

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/connections/an-id", args[0])
        self.assertEqual(kwargs["params"], {"fields": None, "include_fields": "true"})

        c.get("an-id", fields=["a", "b"])

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/connections/an-id", args[0])
        self.assertEqual(kwargs["params"], {"fields": "a,b", "include_fields": "true"})

        c.get("an-id", fields=["a", "b"], include_fields=False)

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/connections/an-id", args[0])
        self.assertEqual(kwargs["params"], {"fields": "a,b", "include_fields": "false"})

    @mock.patch("auth0.management.connections.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.delete.return_value = {}

        c = Connections(domain="domain", token="jwttoken")
        c.delete("this-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/connections/this-id"
        )

    @mock.patch("auth0.management.connections.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        c = Connections(domain="domain", token="jwttoken")
        c.update("that-id", {"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/connections/that-id", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.connections.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.post.return_value = {}

        c = Connections(domain="domain", token="jwttoken")
        c.create({"a": "b", "c": "d"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/connections", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.connections.RestClient")
    def test_delete_user_by_email(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.delete_user_by_email.return_value = {}

        c = Connections(domain="domain", token="jwttoken")
        c.delete_user_by_email("123", "test@example.com")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/connections/123/users",
            params={"email": "test@example.com"},
        )
