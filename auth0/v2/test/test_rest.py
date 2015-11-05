import unittest
import mock
from ..rest import RestClient
from ..exceptions import Auth0Error


class TestRest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        rc = RestClient(endpoint='the-url', jwt='a-token')
        headers = {'Authorization': 'Bearer a-token'}

        mock_get.return_value.text = '["a", "b"]'

        response = rc.get()
        mock_get.assert_called_with('the-url', params={}, headers=headers)

        self.assertEqual(response, ['a', 'b'])

        response = rc.get(id='ID')
        mock_get.assert_called_with('the-url/ID', params={}, headers=headers)

        self.assertEqual(response, ['a', 'b'])

        response = rc.get(params={'A': 'param', 'B': 'param'})
        mock_get.assert_called_with('the-url', params={'A': 'param',
                                                       'B': 'param'},
                                               headers=headers)
        self.assertEqual(response, ['a', 'b'])

        response = rc.get(id='ID', params={'A': 'param', 'B': 'param'})
        mock_get.assert_called_with('the-url/ID', params={'A': 'param',
                                                          'B': 'param'},
                                                  headers=headers)
        self.assertEqual(response, ['a', 'b'])

        mock_get.return_value.text = ''
        response = rc.get()
        self.assertEqual(response, {})

    @mock.patch('requests.get')
    def test_get_errors(self, mock_get):
        rc = RestClient(endpoint='the-url', jwt='a-token')
        headers = {'Authorization': 'Bearer a-token'}

        mock_get.return_value.text = '{"statusCode": 999,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.get()

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')
