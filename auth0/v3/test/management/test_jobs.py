import unittest
import mock
from ...management.jobs import Jobs


class TestJobs(unittest.TestCase):

    def test_init_with_optionals(self):
        t = Jobs(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.get('an-id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/jobs/an-id',
        )

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def get_failed_job(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.get('an-id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/jobs/an-id/errors',
        )

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def get_job_results(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.get('an-id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/jobs/an-id/results',
        )

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def test_export_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.export_users({'connection_id': 'cxn_id', 'format': 'json'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/jobs/users-exports',
            data={'connection_id': 'cxn_id', 'format': 'json'}
        )

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def test_import_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.import_users(connection_id='1234', file_obj={})

        mock_instance.file_post.assert_called_with(
            'https://domain/api/v2/jobs/users-imports',
            data={'connection_id': '1234', 'upsert': 'false', 'send_completion_email': 'true', 'external_id': None},
            files={'users': {}}
        )

        j.import_users(connection_id='1234', file_obj={}, upsert=True, send_completion_email=False, external_id="ext-id-123")
        mock_instance.file_post.assert_called_with(
            'https://domain/api/v2/jobs/users-imports',
            data={'connection_id': '1234', 'upsert': 'true', 'send_completion_email': 'false', 'external_id': 'ext-id-123'},
            files={'users': {}}
        )

        j.import_users(connection_id='1234', file_obj={}, upsert=False, send_completion_email=True)
        mock_instance.file_post.assert_called_with(
            'https://domain/api/v2/jobs/users-imports',
            data={'connection_id': '1234', 'upsert': 'false', 'send_completion_email': 'true', 'external_id': None},
            files={'users': {}}
        )

    @mock.patch('auth0.v3.management.jobs.RestClient')
    def test_verification_email(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.send_verification_email({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/jobs/verification-email',
            data={'a': 'b', 'c': 'd'}
        )
