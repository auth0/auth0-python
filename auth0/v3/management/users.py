from .rest import RestClient


class Users(object):

    """Auth0 users endpoints

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
        url = 'https://{}/api/v2/users'.format(self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def list(self, page=0, per_page=25, sort=None, connection=None, q=None,
             search_engine=None, include_totals=True, fields=None,
             include_fields=True):
        """List or search users.

        Args:
            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.

            sort (str, optional): The field to use for sorting.
                1 == ascending and -1 == descending. (e.g: email:1)

            connection (str, optional): Connection filter.

            q (str, optional): Query in Lucene query string syntax. Only fields
                in app_metadata, user_metadata or the normalized user profile
                are searchable.

            search_engine (str, optional): The version of the search_engine to use
                when querying for users. Will default to the latest version available.
                See: https://auth0.com/docs/users/search

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be include in the result, False otherwise.

        See: https://auth0.com/docs/api/management/v2#!/Users/get_users
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower(),
            'sort': sort,
            'connection': connection,
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'q': q,
            'search_engine': search_engine
        }
        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a new user.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Users/post_users
        """
        return self.client.post(self._url(), data=body)

    def delete_all_users(self):
        """Deletes all users (USE WITH CAUTION).

        Args:
        """
        return self.client.delete(self._url())

    def get(self, id, fields=None, include_fields=True):
        """Get a user.

        Args:
            id (str): The user_id of the user to retrieve.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise.

        See: https://auth0.com/docs/api/management/v2#!/Users/get_users_by_id
        """
        params = {
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower()
        }

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Delete a user.

        Args:
            id (str): The user_id of the user to delete.

        See: https://auth0.com/docs/api/management/v2#!/Users/delete_users_by_id
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update a user with the attributes passed in 'body'

        Args:
            id (str): The user_id of the user to update.

            body (dict): Please see: https://auth0.com/docs/api/v2#!/Users/patch_users_by_id
        """
        return self.client.patch(self._url(id), data=body)

    def list_roles(self, id, page=0, per_page=25, include_totals=True):
        """List the roles associated with a user.

        Args:
            id (str): The user's id.

            page (int, optional): The result's page number (zero based). 
  
            per_page (int, optional): The amount of entries per page. 

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

        See https://auth0.com/docs/api/management/v2#!/Users/get_user_roles
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower()
        }

        url = self._url('{}/roles'.format(id))
        return self.client.get(url, params=params)

    def remove_roles(self, id, roles):
        """Removes an array of roles from a user.

        Args:
            id (str): The user's id.

            roles (list of str): A list of roles ids to unassociate from the user.

        See https://auth0.com/docs/api/management/v2#!/Users/delete_user_roles
        """
        url = self._url('{}/roles'.format(id))
        body = {'roles': roles}
        return self.client.delete(url, data=body)

    def add_roles(self, id, roles):
        """Associate an array of roles with a user.

        Args:
            id (str): The user's id.

            roles (list of str): A list of roles ids to associated with the user.

        See https://auth0.com/docs/api/management/v2#!/Users/post_user_roles
        """
        url = self._url('{}/roles'.format(id))
        body = {'roles': roles}
        return self.client.post(url, data=body)

    def list_permissions(self, id, page=0, per_page=25, include_totals=True):
        """List the permissions associated to the user.

        Args:
            id (str): The user's id.

            page (int, optional): The result's page number (zero based). 
  
            per_page (int, optional): The amount of entries per page. 

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

        See https://auth0.com/docs/api/management/v2#!/Users/get_permissions
        """

        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower()
        }
        url = self._url('{}/permissions'.format(id))
        return self.client.get(url, params=params)

    def remove_permissions(self, id, permissions):
        """Removes permissions from a user.

        Args:
            id (str): The user's id.

            permissions (list of str): A list of permission ids to unassociate from the user.

        See https://auth0.com/docs/api/management/v2#!/Users/delete_permissions
        """
        url = self._url('{}/permissions'.format(id))
        body = {'permissions': permissions}
        return self.client.delete(url, data=body)

    def add_permissions(self, id, permissions):
        """Assign permissions to a user.

        Args:
            id (str): The user's id.

            permissions (list of str): A list of permission ids to associated with the user.

        See https://auth0.com/docs/api/management/v2#!/Users/post_permissions
        """
        url = self._url('{}/permissions'.format(id))
        body = {'permissions': permissions}
        return self.client.post(url, data=body)

    def delete_multifactor(self, id, provider):
        """Delete a user's multifactor provider.

        Args:
            id (str): The user's id.

            provider (str): The multifactor provider. Supported values 'duo'
                or 'google-authenticator'

        See: https://auth0.com/docs/api/management/v2#!/Users/delete_multifactor_by_provider
        """
        url = self._url('{}/multifactor/{}'.format(id, provider))
        return self.client.delete(url)

    def unlink_user_account(self, id, provider, user_id):
        """Unlink a user account

        Args:
            id (str): The user_id of the user identity.

            provider (str): The type of identity provider (e.g: facebook).

            user_id (str): The unique identifier for the user for the identity.

        See: https://auth0.com/docs/api/management/v2#!/Users/delete_user_identity_by_user_id
        """
        url = self._url('{}/identities/{}/{}'.format(id, provider, user_id))
        return self.client.delete(url)

    def link_user_account(self, user_id, body):
        """Link user accounts.

        Links the account specified in the body (secondary account) to the
        account specified by the id param of the URL (primary account).

        Args:
            id (str): The user_id of the primary identity where you are linking
                the secondary account to.

            body (dict): Please see: https://auth0.com/docs/api/v2#!/Users/post_identities
        """
        url = self._url('{}/identities'.format(user_id))
        return self.client.post(url, data=body)

    def regenerate_recovery_code(self, user_id):
        """Removes the current recovery token, generates and returns a new one

        Args:
            user_id (str):  The user_id of the user identity.

        See: https://auth0.com/docs/api/management/v2#!/Users/post_recovery_code_regeneration
        """
        url = self._url('{}/recovery-code-regeneration'.format(user_id))
        return self.client.post(url)

    def get_guardian_enrollments(self, user_id):
        """Retrieves all Guardian enrollments.

        Args:
            user_id (str):  The user_id of the user to retrieve

        See: https://auth0.com/docs/api/management/v2#!/Users/get_enrollments
        """
        url = self._url('{}/enrollments'.format(user_id))
        return self.client.get(url)

    def get_log_events(self, user_id, page=0, per_page=50, sort=None,
                       include_totals=False):
        """Retrieve every log event for a specific user id

        Args:
            user_id (str):  The user_id of the logs to retrieve

            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.
                Default: 50. Max value: 100

            sort (str, optional):  The field to use for sorting. Use field:order
                where order is 1 for ascending and -1 for descending.
                For example date:-1

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

            See: https://auth0.com/docs/api/management/v2#!/Users/get_logs_by_user
        """

        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower(),
            'sort': sort
        }

        url = self._url('{}/logs'.format(user_id))
        return self.client.get(url, params=params)
