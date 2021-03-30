import unittest
import mock
from ...management.organizations import Organizations


class TestOrganizations(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Organizations(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    # Organizations
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_all_organizations(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all_organizations()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations', args[0])
        self.assertEqual(kwargs['params'], {'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all_organizations(page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations', args[0])
        self.assertEqual(kwargs['params'], {'page': 7,
                                            'per_page': 25})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_get_organization_by_name(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.get_organization_by_name('test-org')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations', args[0])
        self.assertEqual(kwargs['params'], {'name': 'test-org'})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_create_organization(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.create_organization({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/organizations',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_update_organization(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.update_organization('this-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/organizations/this-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
   
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_delete_organization(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.delete_organization('this-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/organizations/this-id'
        )
    
    # Organization Connections
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_all_organization_connections(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all_organization_connections('test-org')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/enabled_connections', args[0])
        self.assertEqual(kwargs['params'], {'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all_organization_connections('test-org', page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/enabled_connections', args[0])
        self.assertEqual(kwargs['params'], {'page': 7,
                                            'per_page': 25})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_get_organization_connection(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.get_organization_connection('test-org', 'test-con')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/enabled_connections/test-con', args[0])
        self.assertEqual(kwargs['params'], {})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_create_organization_connection(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.create_organization_connection('test-org', {'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/organizations/test-org/enabled_connections',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_update_organization_connection(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.update_organization_connection('test-org', 'test-con', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/enabled_connections/test-con', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
   
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_delete_organization_connection(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.delete_organization_connection('test-org', 'test-con')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/organizations/test-org/enabled_connections/test-con'
        )