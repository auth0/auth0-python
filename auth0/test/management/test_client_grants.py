import unittest
from unittest import mock

from ...management.client_grants import ClientGrants


class TestClientGrants(unittest.TestCase):
    def test_init_with_optionals(self):
        t = ClientGrants(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.client_grants.RestClient")
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain="domain", token="jwttoken")

        # With default params
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/client-grants", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "audience": None,
                "page": None,
                "per_page": None,
                "include_totals": "false",
                "client_id": None,
            },
        )

        # With audience
        c.all(audience="http://domain.auth0.com/api/v2/")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/client-grants", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "audience": "http://domain.auth0.com/api/v2/",
                "page": None,
                "per_page": None,
                "include_totals": "false",
                "client_id": None,
            },
        )

        # With pagination params
        c.all(per_page=23, page=7, include_totals=True)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/client-grants", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "audience": None,
                "page": 7,
                "per_page": 23,
                "include_totals": "true",
                "client_id": None,
            },
        )

        # With client_id param
        c.all(client_id="exampleid")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/client-grants", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "audience": None,
                "page": None,
                "per_page": None,
                "include_totals": "false",
                "client_id": "exampleid",
            },
        )

    @mock.patch("auth0.management.client_grants.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain="domain", token="jwttoken")
        c.create({"a": "b", "c": "d"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/client-grants", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.client_grants.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain="domain", token="jwttoken")
        c.delete("this-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/client-grants/this-id"
        )

    @mock.patch("auth0.management.client_grants.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain="domain", token="jwttoken")
        c.update("this-id", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual("https://domain/api/v2/client-grants/this-id", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})
