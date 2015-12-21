import unittest
import mock
from ...authentication.link import Link


class TestLink(unittest.TestCase):

    @mock.patch('auth0.v2.authentication.link.Link.post')
    def test_unlink(self, mock_post):

        l = Link('my.domain.com')

        l.unlink(access_token='atk', user_id='uid')

        args, kwargs = mock_post.call_args

        self.assertEqual(kwargs['url'], 'https://my.domain.com/unlink')
        self.assertEqual(kwargs['data'], {
            'access_token': 'atk',
            'user_id': 'uid',
        })
        self.assertEqual(kwargs['headers'], {
            'Content-Type': 'application/json'
        })
