import unittest
import mock
from ...management.custom_domains import CustomDomains


class TestGrants(unittest.TestCase):

    @mock.patch('auth0.v3.management.custom_domains.RestClient')
    def test_get_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = CustomDomains(domain='domain', token='jwttoken')
        g.get_all()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/custom-domains'
        )


