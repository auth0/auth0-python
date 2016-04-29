from .base import AuthenticationBase


class Users(AuthenticationBase):

    """Userinfo related endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def userinfo(self, access_token):

        """Returns the user information based on the Auth0 access token.

        Args:
            access_token (str): Auth0 access token (obtained during login).

        Returns:
            The user profile.
        """

        return self.get(
            url='https://%s/userinfo' % self.domain,
            headers={'Authorization': 'Bearer %s' % access_token}
        )

    def tokeninfo(self, jwt):

        """Returns user profile based on the user's jwt

        Validates a JSON Web Token (signature and expiration) and returns the
        user information associated with the user id (sub property) of
        the token.

        Args:
            jwt (str): User's jwt

        Returns:
            The user profile.
        """

        return self.post(
            url='https://%s/tokeninfo' % self.domain,
            data={'id_token': jwt},
            headers={'Content-Type': 'application/json'}
        )
