import unittest
import mock
from ...management.connections import Connections


class TestConnection(unittest.TestCase):

    @mock.patch('auth0.v2.management.connections.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        c = Connections(domain='domain', token='jwttoken')
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/connections', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'strategy': None,
                                            'include_fields': 'true'})

        c.all(fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/connections', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'strategy': None,
                                            'include_fields': 'false'})

        c.all(fields=['a', 'b'], strategy='strategy', include_fields=True)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/connections', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'strategy': 'strategy',
                                            'include_fields': 'true'})

    @mock.patch('auth0.v2.management.connections.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        c = Connections(domain='domain', token='jwttoken')
        c.get('an-id')

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/connections/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        c.get('an-id', fields=['a', 'b'])

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/connections/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'true'})

        c.get('an-id', fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/connections/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v2.management.connections.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.delete.return_value = {}

        c = Connections(domain='domain', token='jwttoken')
        c.delete('this-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/connections/this-id'
        )

    @mock.patch('auth0.v2.management.connections.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        c = Connections(domain='domain', token='jwttoken')
        c.update('that-id', {'a': 'b', 'c': 'd'})

        mock_instance.patch.assert_called_with(
            'https://domain/api/v2/connections/that-id',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v2.management.connections.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.post.return_value = {}

        c = Connections(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/connections',
            data={'a': 'b', 'c': 'd'}
        )
