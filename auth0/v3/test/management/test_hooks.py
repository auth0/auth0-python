import unittest
import mock
from ...management.hooks import Hooks


class TestRules(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Hooks(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')

        # with default params
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks', args[0])
        self.assertEqual(kwargs['params'], {
            "enabled": 'true',
            "fields": None,
            "include_fields": 'true',
            "page": None,
            "per_page": None,
            "include_totals": 'false',
        })

        # with fields params
        c.all(enabled=False, fields=['a', 'b'],
              include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false',
                                            'enabled': 'false',
                                            'page': None,
                                            'per_page': None,
                                            'include_totals': 'false'})

        # with pagination params
        c.all(page=3, per_page=27, include_totals=True)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'enabled': 'true',
                                            'page': 3,
                                            'per_page': 27,
                                            'include_totals': 'true'})

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/hooks', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.get('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': None})

        c.get('an-id', fields=['a', 'b'])

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b'})

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/hooks/an-id'
        )

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.update('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    # test for hooks secrets
    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_add_secret(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.add_secrets('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id/secrets', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_get_secrets(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.get_secrets('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id/secrets', args[0])
        self.assertNotIn("params", kwargs)

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_delete_secrets(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.delete_secrets('an-id', ['a', 'b'])

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id/secrets', args[0])
        self.assertEqual(kwargs['data'], ['a', 'b'])

    @mock.patch('auth0.v3.management.hooks.RestClient')
    def test_update_secrets(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Hooks(domain='domain', token='jwttoken')
        c.update_secrets('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/hooks/an-id/secrets', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
