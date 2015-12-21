import unittest
import mock
from ...management.clients import Clients


class TestClients(unittest.TestCase):

    @mock.patch('auth0.v2.management.clients.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        c.all(fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/clients', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v2.management.clients.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/clients',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v2.management.clients.RestClient')
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

    @mock.patch('auth0.v2.management.clients.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.delete('this-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/clients/this-id'
        )

    @mock.patch('auth0.v2.management.clients.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Clients(domain='domain', token='jwttoken')
        c.update('this-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/clients/this-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
