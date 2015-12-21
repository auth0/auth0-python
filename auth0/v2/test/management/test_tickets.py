import unittest
import mock
from ...management.tickets import Tickets


class TestTickets(unittest.TestCase):

    @mock.patch('auth0.v2.management.tickets.RestClient')
    def test_email(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Tickets(domain='domain', token='jwttoken')
        t.create_email_verification({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/tickets/email-verification',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v2.management.tickets.RestClient')
    def test_pswd(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Tickets(domain='domain', token='jwttoken')
        t.create_pswd_change({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/tickets/password-change',
            data={'a': 'b', 'c': 'd'}
        )
