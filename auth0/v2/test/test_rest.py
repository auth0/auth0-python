import unittest
import json
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

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        rc = RestClient(endpoint='the-url', jwt='a-token')
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_post.return_value.text = '["a", "b"]'

        data = {'some': 'data'}

        response = rc.post(data=data)
        mock_post.assert_called_with('the-url', data=json.dumps(data),
                                     headers=headers)

        self.assertEqual(response, ['a', 'b'])

        response = rc.post(data=data, id='ID')
        mock_post.assert_called_with('the-url/ID', data=json.dumps(data),
                                     headers=headers)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.post')
    def test_post_errors(self, mock_post):
        rc = RestClient(endpoint='the-url', jwt='a-token')

        mock_post.return_value.text = '{"statusCode": 999,' \
                                      ' "errorCode": "code",' \
                                      ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.post()

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')
