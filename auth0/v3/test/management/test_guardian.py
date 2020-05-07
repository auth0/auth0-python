import unittest
import mock
from ...management.guardian import Guardian


class TestGuardian(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Guardian(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_all_factors(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.all_factors()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/guardian/factors'
        )

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_update_factor(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.update_factor('push-notification', {'enabled': True})

        args, kwargs = mock_instance.put.call_args
        self.assertEqual('https://domain/api/v2/guardian/factors/push-notification', args[0])
        self.assertEqual(kwargs['data'], {'enabled': True})

        g.update_factor('sms', {'enabled': False})

        args, kwargs = mock_instance.put.call_args
        self.assertEqual('https://domain/api/v2/guardian/factors/sms', args[0])
        self.assertEqual(kwargs['data'], {'enabled': False})

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_update_templates(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.update_templates({'enrollment_message': 'hello',
                            'verification_message': 'verified'})

        args, kwargs = mock_instance.put.call_args
        self.assertEqual('https://domain/api/v2/guardian/factors/sms/templates', args[0])
        self.assertEqual(kwargs['data'], {'enrollment_message': 'hello',
                                          'verification_message': 'verified'})

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_get_templates(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.get_templates()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/guardian/factors/sms/templates'
        )

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_get_enrollment(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.get_enrollment('some_id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/guardian/enrollments/some_id'
        )

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_delete_enrollment(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.delete_enrollment('some_id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/guardian/enrollments/some_id'
        )

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_create_enrollment_ticket(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.create_enrollment_ticket({'user_id': 'some_id',
                                    'email': 'test@test.com',
                                    'send_mail': 'false'})

        args, kwargs = mock_instance.post.call_args
        self.assertEqual('https://domain/api/v2/guardian/enrollments/ticket', args[0])
        self.assertEqual(kwargs['data'], {'user_id': 'some_id',
                                          'email': 'test@test.com',
                                          'send_mail': 'false'})

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_get_factor_providers(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.get_factor_providers('sms', 'twilio')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/guardian/factors/sms/providers/twilio'
        )

    @mock.patch('auth0.v3.management.guardian.RestClient')
    def test_update_factor_providers(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = Guardian(domain='domain', token='jwttoken')
        g.update_factor_providers('sms',
                                  'twilio',
                                  {'from': 'test@test.com',
                                   'messaging_service_sid': 'qwerty',
                                   'auth_token': 'abc.xyz.123',
                                   'sid': 'abc.xyz'})

        args, kwargs = mock_instance.put.call_args
        self.assertEqual('https://domain/api/v2/guardian/factors/sms/providers/twilio', args[0])
        self.assertEqual(kwargs['data'], {'from': 'test@test.com',
                                          'messaging_service_sid': 'qwerty',
                                          'auth_token': 'abc.xyz.123',
                                          'sid': 'abc.xyz'})
