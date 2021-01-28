from .rest import RestClient


class UsersByEmail(object):
    """Auth0 users by email endpoints

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

    def _url(self):
        url = '{}://{}/api/v2/users-by-email'.format(self.protocol, self.domain)
        return url

    def search_users_by_email(self, email, fields=None, include_fields=True):
        """List or search users.

        Args:

            email: Email to search.

            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Leave empty to
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
