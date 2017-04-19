import unittest
import mock
from ...management.logs import Logs

class TestLogs(unittest.TestCase):

    @mock.patch('auth0.v3.management.logs.RestClient')
    def test_search(self, mock_rc):
        mock_instance = mock_rc.return_value

        l = Logs(domain='domain', token='jwttoken')
        l.search()

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/logs', args[0])
        self.assertEqual(kwargs['params']['sort'], None)
        self.assertEqual(kwargs['params']['q'], None)
        self.assertEqual(kwargs['params']['from'], None)
        self.assertEqual(kwargs['params']['take'], None)
        self.assertEqual(kwargs['params']['include_fields'], 'true')
        self.assertEqual(kwargs['params']['include_totals'], 'true')
        self.assertEqual(kwargs['params']['per_page'], 50)
        self.assertEqual(kwargs['params']['page'], 0)
        self.assertEqual(kwargs['params']['fields'], None)

        l.search(fields=['description', 'client_id'])

        args, kwargs = mock_instance.get.call_args
        self.assertEqual(kwargs['params']['fields'], 'description,client_id')

        l.search(page=0, per_page=2)

        args, kwargs = mock_instance.get.call_args
        self.assertEqual(kwargs['params']['per_page'], 2)
        self.assertEqual(kwargs['params']['page'], 0)


    @mock.patch('auth0.v3.management.logs.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        l = Logs(domain='domain', token='jwttoken')
        l.get('get_id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/logs/get_id'
        )
