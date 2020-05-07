import unittest
import mock
from ...management.tenants import Tenants


class TestTenants(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Tenants(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.tenants.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        t = Tenants(domain='domain', token='jwttoken')
        t.get()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/tenants/settings', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        t.get(fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/tenants/settings', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

        t.get(fields=['a', 'b'], include_fields=True)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/tenants/settings', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'true'})

    @mock.patch('auth0.v3.management.tenants.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        t = Tenants(domain='domain', token='jwttoken')
        t.update({'a': 'b', 'c': 'd'})

        mock_instance.patch.assert_called_with(
            'https://domain/api/v2/tenants/settings',
            data={'a': 'b', 'c': 'd'}
        )
