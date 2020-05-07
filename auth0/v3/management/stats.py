from .rest import RestClient


class Stats(object):
    """Auth0 stats endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, action):
        return 'https://{}/api/v2/stats/{}'.format(self.domain, action)

    def active_users(self):
        """Gets the active users count (logged in during the last 30 days).

        Returns: An integer.


        See: https://auth0.com/docs/api/management/v2#!/Stats/get_active_users
        """

        return self.client.get(self._url('active-users'))

    def daily_stats(self, from_date=None, to_date=None):
        """Gets the daily stats for a particular period.

        Args:
           from_date (str): The first day of the period (inclusive) in
              YYYYMMDD format.

           to_date (str): The last day of the period (inclusive) in
              YYYYMMDD format.

        See: https://auth0.com/docs/api/management/v2#!/Stats/get_daily
        """

        return self.client.get(self._url('daily'), params={'from': from_date,
                                                           'to': to_date})
