import unittest
import mock
from ...management.users import Users


class TestUsers(unittest.TestCase):

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_list(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.list()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/users', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 25,
            'page': 0,
            'include_totals': 'true',
            'sort': None,
            'connection': None,
            'fields': None,
            'include_fields': 'true',
            'q': None,
            'search_engine': 'v1'
        })

        u.list(page=1, per_page=50, sort='s', connection='con', q='q',
               search_engine='se', include_totals=False, fields=['a', 'b'],
               include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/users', args[0])
        self.assertEqual(kwargs['params'], {
            'per_page': 50,
            'page': 1,
            'include_totals': 'false',
            'sort': 's',
            'connection': 'con',
            'fields': 'a,b',
            'include_fields': 'false',
            'q': 'q',
            'search_engine': 'se'
        })

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.create({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/users', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_delete_all_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.delete_all_users()

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/users'
        )

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.get('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/users/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        u.get('an-id', fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/users/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/users/an-id'
        )

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.update('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/users/an-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_delete_multifactor(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.delete_multifactor('an-id', 'provider')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/users/an-id/multifactor/provider'
        )

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_unlink_user_account(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.unlink_user_account('an-id', 'provider', 'user-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/users/an-id/identities/provider/user-id'
        )

    @mock.patch('auth0.v2.management.users.RestClient')
    def test_link_user_account(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain='domain', token='jwttoken')
        u.link_user_account('user-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/users/user-id/identities',
                         args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
