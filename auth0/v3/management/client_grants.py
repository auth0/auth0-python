from .rest import RestClient


class ClientGrants(object):

    """Auth0 client grants endpoints

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
        url = 'https://%s/api/v2/client-grants' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, audience=None, page=0, per_page=50, include_totals=True):
        """Retrieves all client grants.

        Args:
            audience (str, optional): URL Encoded audience of a Resource Server
                to filter

            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.
                Default: 50. Max value: 100

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.
        """

        params = {
            'audience': audience or None,
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower()
        }

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a client grant.

        Args:
           body (dict): Attributes for the new client grant.
              See: https://auth0.com/docs/api/management/v2#!/Client_Grants/post_client_grants
        """

        return self.client.post(self._url(), data=body)

    def delete(self, id):
        """Deletes a client grant.

        Args:
           id (str): Id of client grant to delete.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client grant.

        Args:
           id (str): The id of the client grant to modify.

           body (dict): Attributes to modify.
        """

        return self.client.patch(self._url(id), data=body)
