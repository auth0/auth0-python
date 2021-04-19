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

        self.assertEqual('https://domain/api/v2/organizations/name/test-org', args[0])
        self.assertEqual(kwargs['params'], {})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_get_organization(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.get_organization('org123')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/org123', args[0])
        self.assertEqual(kwargs['params'], {})

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

    # Organization Members
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_all_organization_members(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all_organization_members('test-org')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/members', args[0])
        self.assertEqual(kwargs['params'], {'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all_organization_members('test-org', page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/members', args[0])
        self.assertEqual(kwargs['params'], {'page': 7,
                                            'per_page': 25})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_create_organization_members(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.create_organization_members('test-org', {'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/organizations/test-org/members',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_delete_organization_members(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.delete_organization_members('test-org', {'a': 'b', 'c': 'd'})

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/organizations/test-org/members',
            data={'a': 'b', 'c': 'd'}
        )

    # Organization Member Roles
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_all_organization_member_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all_organization_member_roles('test-org', 'test-user')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/members/test-user/roles', args[0])
        self.assertEqual(kwargs['params'], {'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all_organization_member_roles('test-org', 'test-user', page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/members/test-user/roles', args[0])
        self.assertEqual(kwargs['params'], {'page': 7,
                                            'per_page': 25})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_create_organization_member_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.create_organization_member_roles('test-org', 'test-user', {'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/organizations/test-org/members/test-user/roles',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_delete_organization_member_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.delete_organization_member_roles('test-org', 'test-user', {'a': 'b', 'c': 'd'})

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/organizations/test-org/members/test-user/roles',
            data={'a': 'b', 'c': 'd'}
        )

    # Organization Invitations
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_all_organization_invitations(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')

        # Default parameters are requested
        c.all_organization_invitations('test-org')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/invitations', args[0])
        self.assertEqual(kwargs['params'], {'page': None,
                                            'per_page': None})

        # Specific pagination
        c.all_organization_invitations('test-org', page=7, per_page=25)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/invitations', args[0])
        self.assertEqual(kwargs['params'], {'page': 7,
                                            'per_page': 25})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_get_organization_invitation(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.get_organization_invitation('test-org', 'test-inv')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/organizations/test-org/invitations/test-inv', args[0])
        self.assertEqual(kwargs['params'], {})

    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_create_organization_invitation(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.create_organization_invitation('test-org', {'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/organizations/test-org/invitations',
            data={'a': 'b', 'c': 'd'}
        )
   
    @mock.patch('auth0.v3.management.organizations.RestClient')
    def test_delete_organization_invitation(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Organizations(domain='domain', token='jwttoken')
        c.delete_organization_invitation('test-org', 'test-inv')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/organizations/test-org/invitations/test-inv'
        )
