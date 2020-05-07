from .rest import RestClient


class RulesConfigs(object):

    """RulesConfig endpoint implementation.

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, id=None):
        url = 'https://%s/api/v2/rules-configs' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self):
        """Lists the config variable keys for rules.

        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/get_rules_configs
        """
        return self.client.get(self._url())

    def unset(self, key):
        """Removes the rules config for a given key.

        Args:
            key (str): rules config key to remove

        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/delete_rules_configs_by_key
        """
        return self.client.delete(self._url(key))

    def set(self, key, value):
        """Sets the rules config for a given key.

        Args:
            key (str): rules config key to set

            value (str): value to set for the rules config key

        See: https://auth0.com/docs/api/management/v2#!/Rules_Configs/put_rules_configs_by_key
        """
        url = self._url('{}'.format(key))
        body = {'value': value}
        return self.client.put(url, data=body)

