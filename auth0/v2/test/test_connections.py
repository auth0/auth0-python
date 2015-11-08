import unittest
import mock
from ..connection import Connection


class TestConnection(unittest.TestCase):

    @mock.patch('auth0.v2.connection.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        c = Connection(domain='domain', jwt_token='jwttoken')
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

    @mock.patch('auth0.v2.connection.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        c = Connection(domain='domain', jwt_token='jwttoken')
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
