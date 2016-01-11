from .base import AuthenticationBase


class Social(AuthenticationBase):

    """Social provider's endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def login(self, client_id, access_token, connection, scope='openid'):
        """Login using a social provider's access token

        Given the social provider's access_token and the connection specified,
        it will do the authentication on the provider and return a dict with
        the access_token and id_token. Currently, this endpoint only works for
        Facebook, Google, Twitter and Weibo.

        Args:
            client_id (str): client name.

            access_token (str): social provider's access_token.

            connection (str): connection type (e.g: 'facebook')

        Returns:
            A dict with 'access_token' and 'id_token' keys.
        """

        return self.post(
            'https://%s/oauth/access_token' % self.domain,
            data={
                'client_id': client_id,
                'access_token': access_token,
                'connection': connection,
                'scope': scope,
            },
            headers={'Content-Type': 'application/json'}
        )
