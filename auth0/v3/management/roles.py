from .rest import RestClient


class Roles(object):
    """Auth0 roles endpoints

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
        url = '{}://{}/api/v2/roles'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def list(self, page=0, per_page=25, include_totals=True, name_filter=None):
        """List or search roles.

        Args:
            page (int, optional): The result's page number (zero based). By default,
               retrieves the first page of results.

            per_page (int, optional): The amount of entries per page. By default,
               retrieves 25 results per page.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise. Defaults to True.

            name_filter (str, optional): A case-insensitive filter to apply
                to search for roles by name.

        See: https://auth0.com/docs/api/management/v2#!/Roles/get_roles
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower(),
            'name_filter': name_filter
        }
        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a new role.

        Args:
            body (dict): the attributes for the role to create.

        See: https://auth0.com/docs/api/v2#!/Roles/post_roles
        """
        return self.client.post(self._url(), data=body)

    def get(self, id):
        """Get a role.

        Args:
            id (str): The id of the role to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Roles/get_roles_by_id
        """

        return self.client.get(self._url(id))

    def delete(self, id):
        """Delete a role.

        Args:
            id (str): The id of the role to delete.

        See: https://auth0.com/docs/api/management/v2#!/Roles/delete_roles_by_id
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update a role with the attributes passed in 'body'

        Args:
            id (str): The id of the role to update.

            body (dict): the attributes to update on the role.

        See: https://auth0.com/docs/api/management/v2#!/Roles/patch_roles_by_id
        """
        return self.client.patch(self._url(id), data=body)

    def list_users(self, id, page=0, per_page=25, include_totals=True):
        """List the users that have been associated with a given role.

        Args:
            id (str): The role's id.

            page (int, optional): The result's page number (zero based). By default,
               retrieves the first page of results.

            per_page (int, optional): The amount of entries per page. By default,
               retrieves 25 results per page.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise. Defaults to True.

        See https://auth0.com/docs/api/management/v2#!/Roles/get_role_user
        """

        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower()
        }
        url = self._url('{}/users'.format(id))
        return self.client.get(url, params=params)

    def add_users(self, id, users):
        """Assign users to a role.

        Args:
            id (str): The role's id.

            users (list of str): A list of users ids to add to this role.

        See https://auth0.com/docs/api/management/v2#!/Roles/post_role_users
        """
        url = self._url('{}/users'.format(id))
        body = {'users': users}
        return self.client.post(url, data=body)

    def list_permissions(self, id, page=0, per_page=25, include_totals=True):
        """List the permissions associated to a role.

        Args:
            id (str): The role's id.

            page (int, optional): The result's page number (zero based). By default,
               retrieves the first page of results.

            per_page (int, optional): The amount of entries per page. By default,
               retrieves 25 results per page.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise. Defaults to True.

        See https://auth0.com/docs/api/management/v2#!/Roles/get_role_permission
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower()
        }
        url = self._url('{}/permissions'.format(id))
        return self.client.get(url, params=params)

    def remove_permissions(self, id, permissions):
        """Unassociates permissions from a role.

        Args:
            id (str): The role's id.

            permissions (list of str): A list of permission ids to unassociate from the role.

        See https://auth0.com/docs/api/management/v2#!/Roles/delete_role_permission_assignment
        """
        url = self._url('{}/permissions'.format(id))
        body = {'permissions': permissions}
        return self.client.delete(url, data=body)

    def add_permissions(self, id, permissions):
        """Associates permissions with a role.

        Args:
            id (str): The role's id.

            permissions (list of str): A list of permission ids to associate to the role.

        See https://auth0.com/docs/api/management/v2#!/Roles/post_role_permission_assignment
        """
        url = self._url('{}/permissions'.format(id))
        body = {'permissions': permissions}
        return self.client.post(url, data=body)
