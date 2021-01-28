from .base import AuthenticationBase


class Social(AuthenticationBase):

    """Social provider's endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def login(self, client_id, access_token, connection, scope='openid'):
        """Login using a social provider's access token

        Given the social provider's access_token and the connection specified,
        it will do the authentication on the provider and return a dict with
        the access_token and id_token. Currently, this endpoint only works for
        Facebook, Google, Twitter and Weibo.

        Args:
            client_id (str): application's client id.

            access_token (str): social provider's access_token.

            connection (str): connection type (e.g: 'facebook')

        Returns:
            A dict with 'access_token' and 'id_token' keys.
        """

        return self.post(
            '{}://{}/oauth/access_token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'access_token': access_token,
                'connection': connection,
                'scope': scope,
            }
        )
