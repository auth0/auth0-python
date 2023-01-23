import unittest
from unittest import mock

from ...management.client_credentials import ClientCredentials


class TestClientCredentials(unittest.TestCase):
    def test_init_with_optionals(self):
        t = ClientCredentials(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.client_credentials.RestClient")
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value
        c = ClientCredentials(domain="domain", token="jwttoken")
        c.all("cid")
        mock_instance.get.assert_called_with(
            "https://domain/api/v2/clients/cid/credentials"
        )

    @mock.patch("auth0.management.client_credentials.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value
        c = ClientCredentials(domain="domain", token="jwttoken")
        c.get("cid", "this-id")
        mock_instance.get.assert_called_with(
            "https://domain/api/v2/clients/cid/credentials/this-id"
        )

    @mock.patch("auth0.management.client_credentials.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value
        c = ClientCredentials(domain="domain", token="jwttoken")
        c.create("cid", {"a": "b", "c": "d"})
        mock_instance.post.assert_called_with(
            "https://domain/api/v2/clients/cid/credentials", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.client_credentials.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value
        c = ClientCredentials(domain="domain", token="jwttoken")
        c.delete("cid", "this-id")
        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/clients/cid/credentials/this-id"
        )
