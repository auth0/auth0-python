import unittest
import mock
from ...management.clients import Clients


class TestClients(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Clients(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'page': None,
                                            'per_page': None})

        # Fields filter
        c.all(fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false',
                                            'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all(page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'page': 7,
                                            'per_page': 25})

        # Extra parameters
        c.all(extra_params={'some_key': 'some_value'})

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'page': None,
                                            'per_page': None,
                                            'some_key': 'some_value'})

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/clients',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.get('this-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients/this-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        c.get('this-id', fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients/this-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.delete('this-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/clients/this-id'
        )

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.update('this-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/clients/this-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.clients.RestClient')
    def test_rotate_secret(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.rotate_secret('this-id')

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/clients/this-id/rotate-secret', data={'id': 'this-id'}
        )



