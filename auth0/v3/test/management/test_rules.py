import unittest
import mock
from ...management.rules import Rules


class TestRules(unittest.TestCase):

    @mock.patch('auth0.v2.management.rules.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Rules(domain='domain', token='jwttoken')
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/rules', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true',
                                            'enabled': 'true',
                                            'stage': 'login_success'})

        c.all(stage='stage', enabled=False, fields=['a', 'b'],
              include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/rules', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false',
                                            'enabled': 'false',
                                            'stage': 'stage'})

    @mock.patch('auth0.v2.management.rules.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Rules(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/rules', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v2.management.rules.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Rules(domain='domain', token='jwttoken')
        c.get('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/rules/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        c.get('an-id', fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/rules/an-id', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v2.management.rules.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Rules(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/rules/an-id'
        )

    @mock.patch('auth0.v2.management.rules.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Rules(domain='domain', token='jwttoken')
        c.update('an-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/rules/an-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})
