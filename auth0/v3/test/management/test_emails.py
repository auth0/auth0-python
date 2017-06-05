import unittest
import mock
from ...management.emails import Emails


class TestEmails(unittest.TestCase):

    @mock.patch('auth0.v3.management.emails.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        e = Emails(domain='domain', token='jwttoken')
        e.get()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/emails/provider', args[0])
        self.assertEqual(kwargs['params'], {'fields': None,
                                            'include_fields': 'true'})

        e.get(fields=['a', 'b'], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/emails/provider', args[0])
        self.assertEqual(kwargs['params'], {'fields': 'a,b',
                                            'include_fields': 'false'})

    @mock.patch('auth0.v3.management.emails.RestClient')
    def test_config(self, mock_rc):
        mock_instance = mock_rc.return_value

        e = Emails(domain='domain', token='jwttoken')
        e.config({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/emails/provider', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.emails.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        e = Emails(domain='domain', token='jwttoken')
        e.update({'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/emails/provider', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})

    @mock.patch('auth0.v3.management.emails.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        e = Emails(domain='domain', token='jwttoken')
        e.delete()

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/emails/provider'
        )
