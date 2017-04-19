import unittest
import mock
from ...management.blacklists import Blacklists


class TestBlacklists(unittest.TestCase):

    @mock.patch('auth0.v3.management.blacklists.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Blacklists(domain='domain', token='jwttoken')
        t.get(aud='an-id')

        mock_instance.get.assert_called_with(
            'https://domain/api/v2/blacklists/tokens',
            params={'aud': 'an-id'}
        )

    @mock.patch('auth0.v3.management.blacklists.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Blacklists(domain='domain', token='jwttoken')
        t.create(jti='the-jti', aud='the-aud')

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/blacklists/tokens', args[0])
        self.assertEqual(kwargs['data'], {'jti': 'the-jti', 'aud': 'the-aud'})
