from ..rest import RestClient


class Branding:
    """Auth0 Branding endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """

    def __init__(
        self,
        domain,
        token,
        telemetry=True,
        timeout=5.0,
        protocol="https",
        rest_options=None,
    ):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(
            jwt=token, telemetry=telemetry, timeout=timeout, options=rest_options
        )

    def _url(self, *args):
        url = f"{self.protocol}://{self.domain}/api/v2/branding"
        for p in args:
            if p is not None:
                url = f"{url}/{p}"
        return url

    def get(self, aud=None):
        """Retrieve branding settings. Requires "read:branding" scope.

        See: https://auth0.com/docs/api/management/v2#!/Branding/get_branding
        """

        return self.client.get(self._url())

    def update(self, body):
        """Update branding settings. Requires "update:branding" scope.

        Args:
            body (dict): Attributes for the updated trigger binding.

        See: https://auth0.com/docs/api/management/v2#!/Branding/patch_branding
        """

        return self.client.patch(self._url(), data=body)

    def get_template_universal_login(self):
        """Get template for New Universal Login Experience. Requires "read:branding" scope.

        See: https://auth0.com/docs/api/management/v2#!/Branding/get_universal_login
        """

        return self.client.get(self._url("templates", "universal-login"))

    def delete_template_universal_login(self):
        """Delete template for New Universal Login Experience. Requires "delete:branding" scope.

        See: https://auth0.com/docs/api/management/v2#!/Branding/delete_universal_login
        """

        return self.client.delete(self._url("templates", "universal-login"))

    def update_template_universal_login(self, body):
        """Update template for New Universal Login Experience. Requires "update:branding" scope.

        Args:
            body (str): Complete HTML content to assign to the template. See linked API documentation for example.

        See: https://auth0.com/docs/api/management/v2#!/Branding/put_universal_login
        """

        return self.client.put(
            self._url("templates", "universal-login"),
            data={"template": body},
        )

    def get_default_branding_theme(self):
        """Retrieve default branding theme.

        See: https://auth0.com/docs/api/management/v2#!/Branding/get_default_branding_theme
        """

        return self.client.get(self._url("themes", "default"))

    def get_branding_theme(self, theme_id):
        """Retrieve branding theme.

        Args:
            theme_id (str): The theme_id to retrieve branding theme for.

        See: https://auth0.com/docs/api/management/v2#!/Branding/get_branding_theme
        """

        return self.client.get(self._url("themes", theme_id))

    def delete_branding_theme(self, theme_id):
        """Delete branding theme.

        Args:
            theme_id (str): The theme_id to delete branding theme for.

        See: https://auth0.com/docs/api/management/v2#!/Branding/delete_branding_theme
        """

        return self.client.delete(self._url("themes", theme_id))

    def update_branding_theme(self, theme_id, body):
        """Update branding theme.

        Args:
            theme_id (str): The theme_id to update branding theme for.
            body (dict): The attributes to set on the theme.

        See: https://auth0.com/docs/api/management/v2#!/Branding/patch_branding_theme
        """

        return self.client.patch(self._url("themes", theme_id), data=body)

    def create_branding_theme(self, body):
        """Create branding theme.

        Args:
            body (dict): The attributes to set on the theme.

        See: https://auth0.com/docs/api/management/v2#!/Branding/post_branding_theme
        """

        return self.client.post(self._url("themes"), data=body)
