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

    def all(self, audience=None):
        """Retrieves all client grants.

        Args:
           audience (str, optional): URL Encoded audience of a Resource Server
               to filter
        """

        params = {'audience': audience or None}

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
           id (str): Id of client to delete.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client grant.

        Args:
           id (str): The id of the client grant to modify.

           body (dict): Attributes to modify.
        """

        return self.client.patch(self._url(id), data=body)
