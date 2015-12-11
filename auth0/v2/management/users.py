from .rest import RestClient


class Users(object):

    """Auth0 users endpoints

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
        url = 'https://%s/api/v2/users' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def list(self, page=0, per_page=25, sort=None, connection=None, q=None,
             search_engine='v1', include_totals=True, fields=[],
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

            search_engine (str, optional): Use 'v2' if you want to try our new
                search engine.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be include in the result, False otherwise.
        """
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': str(include_totals).lower(),
            'sort': sort,
            'connection': connection,
            'fields': ','.join(fields) or None,
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
        """
        return self.client.delete(self._url())

    def get(self, id, fields=[], include_fields=True):
        """Get a user.

        Args:
            id (str): The user_id of the user to retrieve.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be include in the result, False otherwise.
        """
        params = {
            'fields': ','.join(fields) or None,
            'include_fields': str(include_fields).lower()
        }

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Delete a user.

        Args:
            id (str): The user_id of the user to delete.
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update a user with the attributes passed in 'body'

        Args:
            id (str): The user_id of the user to update.

            body (dict): Please see: https://auth0.com/docs/api/v2#!/Users/patch_users_by_id
        """
        return self.client.patch(self._url(id), data=body)

    def delete_multifactor(self, id, provider):
        """Delete a user's multifactor provider.

        Args:
            id (str): The user's id.

            provider (str): The multifactor provider. Supported values 'duo'
                or 'google-authenticator'
        """
        url = self._url('%s/multifactor/%s' % (id, provider))
        return self.client.delete(url)

    def unlink_user_account(self, id, provider, user_id):
        """Unlink a user account

        Args:
            id (str): The user_id of the user identity.

            provider (str): The type of identity provider (e.g: facebook).

            user_id (str): The unique identifier for the user for the identity.
        """
        url = self._url('%s/identities/%s/%s' % (id, provider, user_id))
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
        url = self._url('%s/identities' % user_id)
        return self.client.post(url, data=body)
