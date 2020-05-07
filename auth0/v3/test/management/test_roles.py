import unittest
import mock
from ...management.roles import Roles


class TestRoles(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Roles(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_list(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.list()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/roles', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 25,
            'page': 0,
            'include_totals': 'true',
            'name_filter': None
        })

        u.list(page=1, per_page=50, include_totals=False, name_filter='little-role')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/roles', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 50,
            'page': 1,
            'include_totals': 'false',
            'name_filter': 'little-role'
        })

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.create({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/roles', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.get('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id', args[0])

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/roles/an-id'
        )

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.update('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_list_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.list_users('an-id')

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/roles/an-id/users', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 25,
            'page': 0,
            'include_totals': 'true'
        })

        u.list_users(id='an-id', page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id/users', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 50,
            'page': 1,
            'include_totals': 'false'
        })


    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_add_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.add_users('an-id', ['a', 'b'])

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id/users',
                         args[0])
        self.assertEqual(kwargs['data'], {'users': ['a', 'b']})

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_list_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.list_permissions('an-id')

        args, kwargs = mock_instance.get.call_args
        self.assertEqual('https://domain/api/v2/roles/an-id/permissions', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 25,
            'page': 0,
            'include_totals': 'true'
        })

        u.list_permissions(id='an-id', page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id/permissions', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 50,
            'page': 1,
            'include_totals': 'false'
        })

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_remove_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.remove_permissions('an-id', ['a', 'b'])

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id/permissions',
                         args[0])
        self.assertEqual(kwargs['data'], {'permissions': ['a', 'b']})

    @mock.patch('auth0.v3.management.roles.RestClient')
    def test_add_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Roles(domain='domain', token='jwttoken')
        u.add_permissions('an-id', ['a', 'b'])

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/roles/an-id/permissions',
                         args[0])
        self.assertEqual(kwargs['data'], {'permissions': ['a', 'b']})
