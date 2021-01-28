from .rest import RestClient


class Clients(object):
    """Auth0 applications endpoints

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
        url = '{}://{}/api/v2/clients'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all(self, fields=None, include_fields=True, page=None, per_page=None, extra_params=None):
        """Retrieves a list of all the applications.

        Important: The client_secret and encryption_key attributes can only be
        retrieved with the read:client_keys scope.

        Args:
           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Leave empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise. Defaults to True.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

           extra_params (dictionary, optional): The extra parameters to add to
             the request. The fields, include_fields, page and per_page values
             specified as parameters take precedence over the ones defined here.

        See: https://auth0.com/docs/api/management/v2#!/Clients/get_clients
        """
        params = extra_params or {}
        params['fields'] = fields and ','.join(fields) or None
        params['include_fields'] = str(include_fields).lower()
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Create a new application.

        Args:
           body (dict): Attributes for the new application.

        See: https://auth0.com/docs/api/v2#!/Clients/post_clients
        """

        return self.client.post(self._url(), data=body)

    def get(self, id, fields=None, include_fields=True):
        """Retrieves an application by its id.

        Important: The client_secret, encryption_key and signing_keys
        attributes can only be retrieved with the read:client_keys scope.

        Args:
           id (str): Id of the application to get.

           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Leave empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise. Defaults to True.

        See: https://auth0.com/docs/api/management/v2#!/Clients/get_clients_by_id
        """

        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Deletes an application and all its related assets.

        Args:
           id (str): Id of application to delete.

        See: https://auth0.com/docs/api/management/v2#!/Clients/delete_clients_by_id
        """

        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies an application.

        Important: The client_secret, encryption_key and signing_keys
        attributes can only be updated with the update:client_keys scope.

        Args:
           id (str): Client ID of the application.

           body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Clients/patch_clients_by_id
        """

        return self.client.patch(self._url(id), data=body)

    def rotate_secret(self, id):
        """Rotate a client secret. The generated secret is NOT base64 encoded.

        Args:
           id (str): Client ID of the application.

        See: https://auth0.com/docs/api/management/v2#!/Clients/post_rotate_secret
        """

        data = {'id': id}

        url = self._url('%s/rotate-secret' % id)
        return self.client.post(url, data=data)
