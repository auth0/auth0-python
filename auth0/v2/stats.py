from .rest import RestClient


class Stats(object):
    """Auth0 stats endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, action):
        return 'https://%s/api/v2/stats/%s' % (self.domain, action)

    def active_users(self):
        return self.client.get(self._url('active-users'))

    def daily_stats(self, from_date=None, to_date=None):
        return self.client.get(self._url('daily'), params={'from': from_date,
                                                           'to': to_date})
