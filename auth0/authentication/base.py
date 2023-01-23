from auth0.rest import RestClient, RestClientOptions

from .client_authentication import add_client_authentication

UNKNOWN_ERROR = "a0.sdk.internal.unknown"


class AuthenticationBase:
    """Base authentication object providing simple REST methods.

    Args:
        domain (str): The domain of your Auth0 tenant
        client_id (str): Your application's client ID
        client_secret (str, optional): Your application's client secret
        client_assertion_signing_key (str, optional): Private key used to sign the client assertion JWT.
        client_assertion_signing_alg (str, optional): Algorithm used to sign the client assertion JWT (defaults to 'RS256').
        telemetry (bool, optional): Enable or disable telemetry (defaults to True)
        timeout (float or tuple, optional): Change the requests connect and read timeout. Pass a tuple to specify both values separately or a float to set both to it. (defaults to 5.0 for both)
        protocol (str, optional): Useful for testing. (defaults to 'https')
    """

    def __init__(
        self,
        domain,
        client_id,
        client_secret=None,
        client_assertion_signing_key=None,
        client_assertion_signing_alg=None,
        telemetry=True,
        timeout=5.0,
        protocol="https",
    ):
        self.domain = domain
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_assertion_signing_key = client_assertion_signing_key
        self.client_assertion_signing_alg = client_assertion_signing_alg
        self.protocol = protocol
        self.client = RestClient(
            None,
            options=RestClientOptions(telemetry=telemetry, timeout=timeout, retries=0),
        )

    def _add_client_authentication(self, payload):
        return add_client_authentication(
            payload,
            self.domain,
            self.client_id,
            self.client_secret,
            self.client_assertion_signing_key,
            self.client_assertion_signing_alg,
        )

    def post(self, url, data=None, headers=None):
        return self.client.post(url, data=data, headers=headers)

    def authenticated_post(self, url, data=None, headers=None):
        return self.client.post(
            url, data=self._add_client_authentication(data), headers=headers
        )

    def get(self, url, params=None, headers=None):
        return self.client.get(url, params, headers)
