from .base import AuthenticationBase
from .utils.token_verifier import TokenVerifier
from .utils.jwk_provider import UrlJwkProvider

class Social(AuthenticationBase):

    """Social provider's endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain, token_verifier=None):
        self.domain = domain
        self.token_verifier = token_verifier or TokenVerifier(UrlJwkProvider(domain))

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

        result = self.post(
            'https://%s/oauth/access_token' % self.domain,
            data={
                'client_id': client_id,
                'access_token': access_token,
                'connection': connection,
                'scope': scope,
            },
            headers={'Content-Type': 'application/json'}
        )
        id_token = 'id_token' in result and result['id_token']
        if id_token: 
            self.token_verifier.verify(id_token, client_id)
        return result