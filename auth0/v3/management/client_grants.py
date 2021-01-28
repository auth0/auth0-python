from .rest import RestClient


class ClientGrants(object):
    """Auth0 client grants endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0, protocol="https"):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, id=None):
        url = '{}://{}/api/v2/client-grants'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all(self, audience=None, page=None, per_page=None, include_totals=False, client_id=None):
        """Retrieves all client grants.

        Args:
            audience (str, optional): URL encoded audience of a Resource Server
                to filter.

            page (int, optional): The result's page number (zero based). When not set,
                the default value is up to the server.

            per_page (int, optional): The amount of entries per page. When not set,
                the default value is up to the server.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise. Defaults to False.

            client_id (string, optional): The id of a client to filter.

        See: https://auth0.com/docs/api/management/v2#!/Client_Grants/get_client_grants
        """

        params = {
            'audience': audience,
            'page': page,
            'per_page': per_page,
            'include_totals': str(include_totals).lower(),
            'client_id': client_id,
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

        See: https://auth0.com/docs/api/management/v2#!/Client_Grants/delete_client_grants_by_id
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client grant.

        Args:
           id (str): The id of the client grant to modify.

           body (dict): Attributes to update.

        See: https://auth0.com/docs/api/management/v2#!/Client_Grants/patch_client_grants_by_id
        """

        return self.client.patch(self._url(id), data=body)
