import unittest
import mock
from ...management.stats import Stats


class TestTickets(unittest.TestCase):

    @mock.patch('auth0.v3.management.stats.RestClient')
    def test_active_users(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = Stats(domain='domain', token='jwttoken')
        s.active_users()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/stats/active-users',
        )

    @mock.patch('auth0.v3.management.stats.RestClient')
    def test_daily_stats(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = Stats(domain='domain', token='jwttoken')
        s.daily_stats()

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/stats/daily',
            params={'from': None, 'to': None},
        )

        s.daily_stats(from_date='12341212', to_date='56785656')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/stats/daily',
            params={'from': '12341212', 'to': '56785656'},
        )
