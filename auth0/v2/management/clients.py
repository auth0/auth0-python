from .rest import RestClient


class Clients(object):

    """Auth0 client endpoints

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
        url = 'https://%s/api/v2/clients' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, fields=[], include_fields=True):
        """Retrieves a list of all client applications.

        Important: The client_secret and encryption_key attributes can only be
        retrieved with the read:client_keys scope.

        Args:
           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be include in the result, False otherwise.
        """

        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Create a new client application.

        Args:
           body (dict): Attributes for the new client application.
              See: https://auth0.com/docs/api/v2#!/Clients/post_clients
        """

        return self.client.post(self._url(), data=body)

    def get(self, id, fields=[], include_fields=True):
        """Retrieves a client by its id.

        Important: The client_secret, encryption_key and signing_keys
        attributes can only be retrieved with the read:client_keys scope.

        Args:
           id (str): Id of the client to get.

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be include in the result, False otherwise.
        """

        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Deletes a client and all its related assets.

        Args:
           id (str): Id of client to delete.
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client.

        Important: The client_secret, encryption_key and signing_keys
        attributes can only be updated with the update:client_keys scope.

        Args:
           id (str): Client id.

           body (dict): Attributes to modify.
        """

        return self.client.patch(self._url(id), data=body)
