from .rest import RestClient


class Connections(object):
    """Auth0 connection endpoints

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
        url = '{}://{}/api/v2/connections'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all(self, strategy=None, fields=None, include_fields=True, page=None, per_page=None, extra_params=None):
        """Retrieves all connections.

        Args:
           strategy (str, optional): Only retrieve connections of
              this strategy type. (e.g: strategy='amazon')

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Leave empty to
              retrieve all fields. By default, all the fields will be retrieved.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise. Defaults to True.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

           extra_params (dictionary, optional): The extra parameters to add to
             the request. The fields, include_fields, page and per_page values
             specified as parameters take precedence over the ones defined here.

        See: https://auth0.com/docs/api/management/v2#!/Connections/get_connections

        Returns:
           A list of connection objects.
        """

        params = extra_params or {}
        params['strategy'] = strategy or None
        params['fields'] = fields and ','.join(fields) or None
        params['include_fields'] = str(include_fields).lower()
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(), params=params)

    def get(self, id, fields=None, include_fields=True):
        """Retrieve connection by id.

        Args:
           id (str): Id of the connection to get.

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Leave empty to
              retrieve all fields. By default, all the fields will be retrieved.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise. Defaults to True.

        See: https://auth0.com/docs/api/management/v2#!/Connections/get_connections_by_id

        Returns:
            A connection object.
        """

        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Deletes a connection and all its users.

        Args:
           id: Id of the connection to delete.

        See: https://auth0.com/docs/api/management/v2#!/Connections/delete_connections_by_id

        Returns:
           An empty dict.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a connection.

        Args:
           id: Id of the connection.

           body (dict): Specifies which fields are to be modified, and to what values.

        See: https://auth0.com/docs/api/management/v2#!/Connections/patch_connections_by_id

        Returns:
           The modified connection object.
        """

        return self.client.patch(self._url(id), data=body)

    def create(self, body):
        """Creates a new connection.

        Args:
            body (dict): Attributes used to create the connection. Mandatory
                attributes are: 'name' and 'strategy'.

        See: https://auth0.com/docs/api/management/v2#!/Connections/post_connections
        """

        return self.client.post(self._url(), data=body)

    def delete_user_by_email(self, id, email):
        """Deletes a specified connection user by its email.

        Args:
           id (str): The id of the connection (must be a database connection).

           email (str): The email of the user to delete.

        See: https://auth0.com/docs/api/management/v2#!/Connections/delete_users_by_email

        Returns:
            An empty dict.
        """
        return self.client.delete(self._url(id) + '/users', params={'email': email})
