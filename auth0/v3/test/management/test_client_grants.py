import unittest
import mock
from ...management.client_grants import ClientGrants


class TestClientGrants(unittest.TestCase):

    @mock.patch('auth0.v3.management.client_grants.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain='domain', token='jwttoken')

        # With default params
        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/client-grants', args[0])
        self.assertEqual(kwargs['params'], {
            'audience': None,
            'per_page': 50,
            'page': 0,
            'include_totals': 'true'
        })

        # With audience
        c.all(audience='http://domain.auth0.com/api/v2/')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/client-grants', args[0])
        self.assertEqual(kwargs['params'], {
            'audience': 'http://domain.auth0.com/api/v2/',
            'per_page': 50,
            'page': 0,
            'include_totals': 'true'
        })

        # With pagination params
        c.all(per_page=23, page=7, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/client-grants', args[0])
        self.assertEqual(kwargs['params'], {
            'audience': None,
            'per_page': 23,
            'page': 7,
            'include_totals': 'false'
        })

    @mock.patch('auth0.v3.management.client_grants.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain='domain', token='jwttoken')
        c.create({'a': 'b', 'c': 'd'})

        mock_instance.post.assert_called_with(
            'https://domain/api/v2/client-grants',
            data={'a': 'b', 'c': 'd'}
        )

    @mock.patch('auth0.v3.management.client_grants.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain='domain', token='jwttoken')
        c.delete('this-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/client-grants/this-id'
        )

    @mock.patch('auth0.v3.management.client_grants.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = ClientGrants(domain='domain', token='jwttoken')
        c.update('this-id', {'a': 'b', 'c': 'd'})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/client-grants/this-id', args[0])
        self.assertEqual(kwargs['data'], {'a': 'b', 'c': 'd'})