from .rest import RestClient


class UsersByEmail(object):

    """Auth0 users by email endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self):
        url = 'https://{}/api/v2/users-by-email'.format(self.domain)
        return url

    def search_users_by_email(self, email, fields=None, include_fields=True):
        """List or search users.

        Args:

            email: Email to search

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be include in the result, False otherwise.

        See: https://auth0.com/docs/api/management/v2#!/Users_By_Email/get_users_by_email
        """
        params = {
            'email': email,
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower()
        }
        return self.client.get(self._url(), params=params)
