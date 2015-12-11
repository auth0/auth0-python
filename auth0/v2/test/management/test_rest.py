import unittest
import json
import mock
from ...management.rest import RestClient
from ...exceptions import Auth0Error


class TestRest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}

        mock_get.return_value.text = '["a", "b"]'

        response = rc.get('the-url')
        mock_get.assert_called_with('the-url', params={}, headers=headers)

        self.assertEqual(response, ['a', 'b'])

        response = rc.get(url='the/url', params={'A': 'param', 'B': 'param'})
        mock_get.assert_called_with('the/url', params={'A': 'param',
                                                       'B': 'param'},
                                               headers=headers)
        self.assertEqual(response, ['a', 'b'])

        mock_get.return_value.text = ''
        response = rc.get('the/url')
        self.assertEqual(response, {})

    @mock.patch('requests.get')
    def test_get_errors(self, mock_get):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}

        mock_get.return_value.text = '{"statusCode": 999,' \
                                     ' "errorCode": "code",' \
                                     ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.get('the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_post.return_value.text = '{"a": "b"}'

        data = {'some': 'data'}

        response = rc.post('the/url', data=data)
        mock_post.assert_called_with('the/url', data=json.dumps(data),
                                     headers=headers)

        self.assertEqual(response, {'a': 'b'})

    @mock.patch('requests.post')
    def test_post_errors(self, mock_post):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_post.return_value.text = '{"statusCode": 999,' \
                                      ' "errorCode": "code",' \
                                      ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.post('the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.patch')
    def test_patch(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token',
                   'Content-Type': 'application/json'}

        mock_patch.return_value.text = '["a", "b"]'

        data = {'some': 'data'}

        response = rc.patch(url='the-url', data=data)
        mock_patch.assert_called_with('the-url', data=json.dumps(data),
                                      headers=headers)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.patch')
    def test_patch_errors(self, mock_patch):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_patch.return_value.text = '{"statusCode": 999,' \
                                       ' "errorCode": "code",' \
                                       ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.patch(url='the/url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')

    @mock.patch('requests.delete')
    def test_delete(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)
        headers = {'Authorization': 'Bearer a-token'}

        mock_delete.return_value.text = '["a", "b"]'

        response = rc.delete(url='the-url/ID')
        mock_delete.assert_called_with('the-url/ID', headers=headers)

        self.assertEqual(response, ['a', 'b'])

    @mock.patch('requests.delete')
    def test_delete_errors(self, mock_delete):
        rc = RestClient(jwt='a-token', telemetry=False)

        mock_delete.return_value.text = '{"statusCode": 999,' \
                                        ' "errorCode": "code",' \
                                        ' "message": "message"}'

        with self.assertRaises(Auth0Error) as context:
            rc.delete(url='the-url')

        self.assertEqual(context.exception.status_code, 999)
        self.assertEqual(context.exception.error_code, 'code')
        self.assertEqual(context.exception.message, 'message')
