from .rest import RestClient


class Stats(object):
    """Auth0 stats endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, action):
        return 'https://%s/api/v2/stats/%s' % (self.domain, action)

    def active_users(self):
        """Gets the active users count (logged in during the last 30 days).

        Returns: An integer.
        """

        return self.client.get(self._url('active-users'))

    def daily_stats(self, from_date=None, to_date=None):
        """Gets the daily stats for a particular period.

        Args:
           from_date (str): The first day of the period (inclusive) in
              YYYYMMDD format.

           to_date (str): The last day of the period (inclusive) in
              YYYYMMDD format.
        """

        return self.client.get(self._url('daily'), params={'from': from_date,
                                                           'to': to_date})
