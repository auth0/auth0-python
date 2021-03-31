from .rest import RestClient


class Hooks(object):

    """Hooks endpoint implementation.

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
        url = "{}://{}/api/v2/hooks".format(self.protocol, self.domain)
        if id is not None:
            return "{}/{}".format(url, id)
        return url

    def all(
        self,
        enabled=True,
        fields=None,
        include_fields=True,
        page=None,
        per_page=None,
        include_totals=False,
    ):
        """Retrieves a list of all hooks.

        Args:
            enabled (bool, optional): If provided, retrieves hooks that match
                the value, otherwise all hooks are retrieved.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise
                (defaults to true).

            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/get_hooks
        """

        params = {
            "fields": fields and ",".join(fields) or None,
            "include_fields": str(include_fields).lower(),
            "page": page,
            "per_page": per_page,
            "include_totals": str(include_totals).lower(),
        }

        # since the default is True, this is here to disable the filter
        if enabled is not None:
            params["enabled"] = str(enabled).lower()

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a new Hook.

        Args:
            body (dict): Attributes for the newly created hook,
                See: https://auth0.com/docs/api/v2#!/Hooks/post_hooks
        """
        return self.client.post(self._url(), data=body)

    def get(self, id, fields=None):
        """Retrieves a hook by its ID.

        Args:
            id (str): The id of the hook to retrieve.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/get_hooks_by_id
        """
        params = {
            "fields": fields and ",".join(fields) or None,
        }
        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Deletes a hook.

        Args:
            id (str): The id of the hook to delete.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/delete_hooks_by_id
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Updates an existing hook.

        Args:
            id (str): The id of the hook to modify.

            body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/v2#!/Hooks/patch_hooks_by_id
        """
        return self.client.patch(self._url(id), data=body)

    def get_secrets(self, id):
        """Retrieves a hook's secrets.

        Args:
            id (str): The id of the hook to retrieve secrets from.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/get_secrets
        """

        return self.client.get(self._url("%s/secrets" % id))

    def add_secrets(self, id, body):
        """Add one or more secrets for an existing hook.

        Args:
            id (str): The id of the hook to add secrets to.

            body (dict): Dict of key-value pairs where the value must be a string.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/post_secrets
        """
        return self.client.post(self._url("%s/secrets" % id), data=body)

    def delete_secrets(self, id, body):
        """Delete one or more existing secrets for an existing hook.

        Args:
            id (str): The id of the hook to add secrets to.

            body (list): List of secret names to delete.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/delete_secrets
        """
        return self.client.delete(self._url("%s/secrets" % id), data=body)

    def update_secrets(self, id, body):
        """Update one or more existing secrets for an existing hook.

        Args:
            id (str): The id of the hook to add secrets to.

            body (dict): Dict of key-value pairs where the value must be a string.

        See: https://auth0.com/docs/api/management/v2#!/Hooks/patch_secrets
        """
        return self.client.patch(self._url("%s/secrets" % id), data=body)
