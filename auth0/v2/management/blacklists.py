from .rest import RestClient


class Blacklists(object):

    """Auth0 blacklists endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.url = 'https://%s/api/v2/blacklists/tokens' % domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def get(self, aud=None):
        """Retrieves the jti and aud of all tokens in the blacklist.

        Args:
            aud (str, optional): The JWT's aud claim. The client_id of the
                client for which it was issued.
        """

        params = {
            'aud': aud
        }

        return self.client.get(self.url, params=params)

    def create(self, jti, aud=''):
        """Adds a token to the blacklist.

        Args:
            jti (str): the jti of the JWT to blacklist.
            aud (str, optional): The JWT's aud claim. The client_id of the
                client for which it was issued.
        """

        return self.client.post(self.url, data={'jti': jti, 'aud': aud})
