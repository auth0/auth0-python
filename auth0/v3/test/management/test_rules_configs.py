import unittest
import mock
from ...management.rules_configs import RulesConfigs


class TestRules(unittest.TestCase):

    @mock.patch('auth0.v3.management.rules_configs.RestClient')
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = RulesConfigs(domain='domain', token='jwttoken')

        c.all()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual('https://domain/api/v2/rules-configs', args[0])

    @mock.patch('auth0.v3.management.rules_configs.RestClient')
    def test_unset(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = RulesConfigs(domain='domain', token='jwttoken')
        c.unset('an-id')

        mock_instance.delete.assert_called_with(
            'https://domain/api/v2/rules-configs/an-id'
        )

    @mock.patch('auth0.v3.management.rules_configs.RestClient')
    def test_set(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = RulesConfigs(domain='domain', token='jwttoken')
        g.set('key', 'MY_RULES_CONFIG_VALUES')

        args, kwargs = mock_instance.put.call_args
        self.assertEqual('https://domain/api/v2/rules-configs/key', args[0])




