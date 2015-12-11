import unittest
import mock
from ...management.jobs import Jobs


class TestJobs(unittest.TestCase):

    @mock.patch('auth0.v2.management.jobs.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.get('an-id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/jobs/an-id',
        )

    @mock.patch('auth0.v2.management.jobs.RestClient')
    def test_import_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.import_users(connection_id='1234', file_obj={})

        mock_instance.file_post.assert_called_with(
            'https://domain/api/v2/jobs/users-imports',
            data={'connection_id': '1234'},
            files={'users': {}}
        )

    @mock.patch('auth0.v2.management.jobs.RestClient')
    def test_verification_email(self, mock_rc):
        mock_instance = mock_rc.return_value

        j = Jobs(domain='domain', token='jwttoken')
        j.send_verification_email({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/jobs/verification-email',
            data={'a': 'b', 'c': 'd'}
        )
