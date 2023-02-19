import unittest
from unittest import mock

from ...authentication.enterprise import Enterprise


class TestEnterprise(unittest.TestCase):
    @mock.patch("auth0.authentication.enterprise.Enterprise.get")
    def test_saml_metadata(self, mock_get):
        e = Enterprise("my.domain.com", "cid")

        e.saml_metadata()

        mock_get.assert_called_with(url="https://my.domain.com/samlp/metadata/cid")

    @mock.patch("auth0.authentication.enterprise.Enterprise.get")
    def test_wsfed_metadata(self, mock_get):
        e = Enterprise("my.domain.com", "cid")

        e.wsfed_metadata()

        mock_get.assert_called_with(
            url=(
                "https://my.domain.com/wsfed/FederationMetadata"
                "/2007-06/FederationMetadata.xml"
            )
        )
