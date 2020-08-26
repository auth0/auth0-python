import unittest

import mock

from ...management.log_streams import LogStreams


class TestLogStreams(unittest.TestCase):

    def test_init_with_optionals(self):
        t = LogStreams(domain='domain', token='jwttoken', telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get('Auth0-Client', None)
        self.assertEqual(telemetry_header, None)

    @mock.patch('auth0.v3.management.log_streams.RestClient')
    def test_list(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = LogStreams(domain='domain', token='jwttoken')

        c.list()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/log-streams', args[0])
        
    @mock.patch('auth0.v3.management.log_streams.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = LogStreams(domain='domain', token='jwttoken')
        c.get('an-id')

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/log-streams/an-id', args[0])

    @mock.patch('auth0.v3.management.log_streams.RestClient')
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = LogStreams(domain='domain', token='jwttoken')
        # Sample data belongs to an `http` stream
        log_stream_data = {
            "name": "string",
            "type": "http",
            "sink": {
                "httpEndpoint": "string",
                "httpContentType": "string",
                "httpContentFormat": "JSONLINES|JSONARRAY",
                "httpAuthorization": "string"
            }
        }
        c.create(log_stream_data)

        args, kwargs = mock_instance.post.call_args

        self.assertEqual('https://domain/api/v2/log-streams', args[0])
        self.assertEqual(kwargs['data'], log_stream_data)

    @mock.patch('auth0.v3.management.log_streams.RestClient')
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = LogStreams(domain='domain', token='jwttoken')
        c.delete('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/log-streams/an-id'
        )

    @mock.patch('auth0.v3.management.log_streams.RestClient')
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value
        log_stream_update = {
            "name": "string"
        }

        c = LogStreams(domain='domain', token='jwttoken')
        c.update('an-id', log_stream_update)

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual('https://domain/api/v2/log-streams/an-id', args[0])
        self.assertEqual(kwargs['data'], log_stream_update)
