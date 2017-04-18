from .rest import RestClient


class ResourceServers(object):

    """Auth0 resource servers endpoints

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
        url = 'https://%s/api/v2/resource-servers' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def create(self, body):
        """Create a new resource server.

        Args:
           body (dict): Attributes for the new resource Server
              See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/post_resource_servers
        """

        return self.client.post(self._url(), data=body)

    def get_all(self):
        """Retrieves all resource servers
        """

        return self.client.get(self._url())

    def get(self, id):
        """Retrieves a resource server by its id.

        Args:
           id (str): Id of the resource server to get.
        """

        return self.client.get(self._url(id))

    def delete(self, id):
        """Deletes a resource server.

        Args:
           id (str): Id of resource server to delete.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a resource server.

        Args:
           id (str): The id of the resource server to update.

           body (dict): Attributes to modify.
        """

        return self.client.patch(self._url(id), data=body)
