from .base import AuthenticationBase


class Oauth(AuthenticationBase):

    """Oauth provider's endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def login(self, client_id, client_secret, audience, grant_type, scope='openid'):
        """Login using a Oauth

        Given the social provider's access_token and the connection specified,
        it will do the authentication on the provider and return a dict with
        the access_token and id_token. Currently, this endpoint only works for
        Facebook, Google, Twitter and Weibo.

        Args:
            client_id (str): client name.

            client_secret (str): client secret

            grant_type (str): client_credentials

        Returns:
            A dict with 'access_token' and 'id_token' keys.
        """

        return self.post(
            'https://%s/oauth/token' % self.domain,
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'audience': audience,
                'grant_type': grant_type
            },
            headers={'Content-Type': 'application/json'}
        )
