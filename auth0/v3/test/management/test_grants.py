import unittest
import mock
from ...management.grants import Grants


class TestGrants(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Grants(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.grants.RestClient')
    def test_get_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Grants(domain='domain', token='jwttoken')
        g.all(extra_params={'user_id':'an-id', 'client_id': 'an-id', 'audience':'test'})

        args, kwargs = mock_instance.get.call_args

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/grants', params={'user_id': 'an-id', 'client_id': 'an-id', 'audience': 'test', 'page': None, 'per_page': None, 'include_totals': 'false'}
        )


    @mock.patch('auth0.v3.management.grants.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Grants(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/grants/an-id'
        )
