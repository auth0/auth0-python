from .rest import RestClient


class Logs(object):

    """Auth0 logs endpoints

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
        url = 'https://{}/api/v2/logs'.format(self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def search(self, page=0, per_page=50, sort=None, q=None,
               include_totals=True, fields=None, from_param=None, take=None,
               include_fields=True):
        """Search log events.

        Args:
            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.

            sort (str, optional): The field to use for sorting.
                1 == ascending and -1 == descending. (e.g: date:1)

            q (str, optional): Query in Lucene query string syntax.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

            from_param (str, optional): Log Event Id to start retrieving logs. You can
                limit the amount of logs using the take parameter

            take (int, optional): The total amount of entries to retrieve when
                using the from parameter.

        https://auth0.com/docs/api/management/v2#!/Logs/get_logs
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower(),
            'sort': sort,
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'q': q,
            'from': from_param,
            'take': take
        }
        return self.client.get(self._url(), params=params)

    def get(self, id):
        """Retrieves the data related to the log entry identified by id.

        Args:
            id (str): The log_id of the log to retrieve


        See: https://auth0.com/docs/api/management/v2#!/Logs/get_logs_by_id
        """

        return self.client.get(self._url(id))
