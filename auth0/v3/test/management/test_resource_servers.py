import unittest
import mock
from ...management.resource_servers import ResourceServers


class TestResourceServers(unittest.TestCase):

    def test_init_with_optionals(self):
        t = ResourceServers(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.resource_servers.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        r = ResourceServers(domain='domain', token='jwttoken')

        r.create({'name': 'TestApi', 'identifier': 'https://test.com/api'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/resource-servers',
            data={'name': 'TestApi', 'identifier': 'https://test.com/api'}
        )

    @mock.patch('auth0.v3.management.resource_servers.RestClient')
    def test_get_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        r = ResourceServers(domain='domain', token='jwttoken')

        # with default params
        r.get_all()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/resource-servers',
            params={
                'page': None,
                'per_page': None,
                'include_totals': 'false'
            }
        )

        # with pagination params
        r.get_all(page=3, per_page=27, include_totals=True)

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/resource-servers',
            params={
                'page': 3,
                'per_page': 27,
                'include_totals': 'true'
            }
        )

    @mock.patch('auth0.v3.management.resource_servers.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        r = ResourceServers(domain='domain', token='jwttoken')

        r.get('some_id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/resource-servers/some_id'
        )

    @mock.patch('auth0.v3.management.resource_servers.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        r = ResourceServers(domain='domain', token='jwttoken')

        r.delete('some_id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/resource-servers/some_id'
        )

    @mock.patch('auth0.v3.management.resource_servers.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        r = ResourceServers(domain='domain', token='jwttoken')

        r.update('some_id', {'name': 'TestApi2',
                             'identifier': 'https://test.com/api2'})

        mock_instance.patch.assert_called_with(
            'https://domain/api/v2/resource-servers/some_id',
            data={'name': 'TestApi2',
                  'identifier': 'https://test.com/api2'}
        )
