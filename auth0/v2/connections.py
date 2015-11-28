from .rest import RestClient


class Connections(object):
    """Auth0 connection endpoints

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

    def _url(self, id=None):
        url = 'https://%s/api/v2/connections' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, strategy=None, fields=[], include_fields=True):
        """Retrieves all connections.

        Args:
           strategy (str, optional): Only retrieve connections of
              this strategy type. (e.g: strategy='amazon')

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be include in the result, False otherwise.

        Returns:
           A list of connection objects.
        """

        params = {'strategy': strategy or None,
                  'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def get(self, id, fields=[], include_fields=True):
        """Retrieve connection by id.

        Args:
           id (str): Id of the connection to get.

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be include in the result, False otherwise.

        Returns:
            A connection object.
        """

        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Deletes a connection and all its users.

        Args:
           id: Id of the connection to delete.

        Returns:
           An empty dict.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a connection.

        Args:
           id: Id of the connection.

           body (dict): Specifies which fields are to be modified, and to what
              values.

        Returns:
           The modified connection object.
        """

        return self.client.patch(self._url(id), data=body)

    def create(self, body):
        """Creates a new connection.

        Args:
            body (dict): Attributes used to create the connection. Mandatory
                attributes are: 'name' and 'strategy'.
        """

        return self.client.post(self._url(), data=body)
