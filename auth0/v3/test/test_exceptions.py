import unittest
from ..exceptions import Auth0Error


class TestAuth0Error(unittest.TestCase):

    def test_construct(self):
        err = Auth0Error(123, 456, 'some message')
        self.assertIsInstance(err, Exception)

    def test_str(self):
        err = Auth0Error(123, 456, 'some message')
        string_repr = str(err)
        self.assertIn('some message', string_repr)
