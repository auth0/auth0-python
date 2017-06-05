from .base import AuthenticationBase


class Logout(AuthenticationBase):

    """Logout Endpoint

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def logout(self, client_id, return_to, federated=False):
        """Logout

        Use this endpoint to logout a user. If you want to navigate the user to a
        specific URL after the logout, set that URL at the returnTo parameter.
        The URL should be included in any the appropriate Allowed Logout URLs list:

        Args:
            client_id (str): The client_id of your client.

            returnTo (str): URL to redirect the user after the logout.

            federated (bool): Querystring parameter to log the user out of the IdP
        """
        if federated is True:
            return self.get(
                'https://%s/v2/logout?federated&%s&%s' % (self.domain, client_id, return_to),
                headers={'Content-Type': 'application/json'}
            )
        return self.get(
            'https://%s/v2/logout?%s&%s' % (self.domain, client_id, return_to),
            headers={'Content-Type': 'application/json'}
        )
