from .rest import RestClient


class Connection(object):
    """Auth0 connection endpoints"""

    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/connections' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

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

        return self.client.get(params=params)

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

        return self.client.get(params=params, id=id)

    def delete(self, id):
        """Deletes a connection and all its users.

        Args:
           id: Id of the connection to delete.

        Returns:
           An empty dict.
        """

        return self.client.delete(id=id)

    def update(self, id, body):
        """Modifies a connection.

        Args:
           id: Id of the connection.

           body (dict): Specifies which fields are to be modified, and to what
              values.

        Returns:
           The modified connection object.
        """

        return self.client.patch(id=id, data=body)

    def create(self, body):
        """Creates a new connection. """

        return self.client.post(data=body)
