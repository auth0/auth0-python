from typing import Any

from auth0.rest import RestClient
from auth0.rest import RestClientOptions
from auth0.types import TimeoutType


class Sessions:
    """Auth0 users endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        protocol (str, optional): Protocol to use when making requests.
            (defaults to "https")

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """

    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None:
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout, options=rest_options)

    def _url(self, id: str | None = None) -> str:
        url = f"{self.protocol}://{self.domain}/api/v2/sessions"
        if id is not None:
            return f"{url}/{id}"
        return url

    def get(self, id: str) -> dict[str, Any]:
        """Get a session.

        Args:
            id (str): The id of the session to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Sessions/get-session
        """

        return self.client.get(self._url(id))

    def delete(self, id: str) -> None:
        """Delete a session.

        Args:
            id (str): The id of the session to delete.

        See: https://auth0.com/docs/api/management/v2#!/Sessions/delete-session
        """

        return self.client.delete(self._url(id))

    def revoke(self, id: str) -> None:
        """Revokes a session by ID and all associated refresh tokens..

        Args:
            id (str): The id of the session to revoke.

        See: https://auth0.com/docs/api/management/v2#!/Sessions/revoke-session
        """

        url = self._url(f"{id}/sessions")
        return self.client.post(url)
