import unittest
import mock
from ...management.device_credentials import DeviceCredentials


class TestDeviceCredentials(unittest.TestCase):

    @mock.patch('auth0.v3.management.device_credentials.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = DeviceCredentials(domain='domain', token='jwttoken')
        c.get(user_id='uid', client_id='cid', type='type')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/device-credentials', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'user_id': 'uid',
                                            'client_id': 'cid',
                                            'type': 'type'})

    @mock.patch('auth0.v3.management.device_credentials.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = DeviceCredentials(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/device-credentials', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.device_credentials.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = DeviceCredentials(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/device-credentials/an-id',
        )
