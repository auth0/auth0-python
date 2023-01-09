import warnings

from auth0.v3.rest import RestClient, RestClientOptions

from .base import AuthenticationBase


class Users(object):
    """Users client.

    Args:
        domain (str): The domain of your auth0 tenant
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
        protocol (str, optional): Useful for testing.
            (defaults to 'https')
    """

    def __init__(
        self,
        domain,
        telemetry=True,
        timeout=5.0,
        protocol="https",
    ):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(
            None,
            options=RestClientOptions(telemetry=telemetry, timeout=timeout, retries=0),
        )

    """Userinfo related endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def userinfo(self, access_token):

        """Returns the user information based on the Auth0 access token.
        This endpoint will work only if openid was granted as a scope for the access_token.

        Args:
            access_token (str): Auth0 access token (obtained during login).

        Returns:
            The user profile.
        """

        return self.client.get(
            url="{}://{}/userinfo".format(self.protocol, self.domain),
            headers={"Authorization": "Bearer {}".format(access_token)},
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
        warnings.warn(
            "/tokeninfo will be deprecated in future releases", DeprecationWarning
        )
        return self.client.post(
            url="{}://{}/tokeninfo".format(self.protocol, self.domain),
            data={"id_token": jwt},
        )
