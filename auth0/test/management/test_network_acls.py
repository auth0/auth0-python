import unittest
from unittest import mock

from ...management.network_acls import NetworkAcls


class TestNetworkAcls(unittest.TestCase):
    def test_init_with_optionals(self):
        t = NetworkAcls(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.all()

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/network-acls",
            params={"page": 0, "per_page": 25, "include_totals": "true"},
        )

        s.all(page=1, per_page=50, include_totals=False)

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/network-acls",
            params={"page": 1, "per_page": 50, "include_totals": "false"},
        )

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.create({"name": "test"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/network-acls", data={"name": "test"}
        )

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.get("an-id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/network-acls/an-id"
        )

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.delete("an-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/network-acls/an-id"
        )

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.update("an-id", {"a": "b", "c": "d"})

        mock_instance.put.assert_called_with(
            "https://domain/api/v2/network-acls/an-id",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.network_acls.RestClient")
    def test_update_partial(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = NetworkAcls(domain="domain", token="jwttoken")
        s.update_partial("an-id", {"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/network-acls/an-id",
            data={"a": "b", "c": "d"},
        )