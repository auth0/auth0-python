from .rest import RestClient


class RulesConfigs(object):

    """RulesConfig endpoint implementation.

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, id=None):
        url = 'https://%s/api/v2/rules-configs' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, stage='login_success', enabled=True, fields=None,
            include_fields=True, page=None, per_page=None, include_totals=False):
        """Lists the config variable keys for rules.


        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/get_rules_configs
        """

        return self.client.get(self._url())


    def remove(self, key):
        """Removes the rules config for a given key.


        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/delete_rules_configs_by_key
        """

        params = {
            'key': key
        }
        return self.client.delete(self._url(), params=params)

    def set_rule_for_key(self, key, body):
        """Sets the rules config for a given key.


        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/put_rules_configs_by_key
        """

        params = {
            'key': key
        }
        url = self._url('{}'.format(key))
        return self.client.put(url, data=body)

