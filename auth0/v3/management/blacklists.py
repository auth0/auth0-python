from .rest import RestClient


class Blacklists(object):
    """Auth0 blacklists endpoints

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
        self.url = '{}://{}/api/v2/blacklists/tokens'.format(protocol, domain)
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def get(self, aud=None):
        """Retrieves the jti and aud of all tokens in the blacklist.

        Args:
            aud (str, optional): The JWT's aud claim. The client_id of the
                application for which it was issued.


        See: https://auth0.com/docs/api/management/v2#!/Blacklists/get_tokens
        """

        params = {
            'aud': aud
        }

        return self.client.get(self.url, params=params)

    def create(self, jti, aud=None):
        """Adds a token to the blacklist.

        Args:
            jti (str): the jti of the JWT to blacklist.

            aud (str, optional): The JWT's aud claim. The client_id of the
                application for which it was issued.

        See: https://auth0.com/docs/api/management/v2#!/Blacklists/post_tokens
        """
        body = {
            'jti': jti,
        }

        if aud:
            body.update({'aud': aud})

        return self.client.post(self.url, data=body)
