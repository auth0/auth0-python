from .base import AuthenticationBase


class AuthorizeClient(AuthenticationBase):

    """Authorize Client

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def authorize(self, client_id, audience=None, state=None, redirect_uri=None,
                  response_type='code', scope='openid'):
        """Authorization code grant

        This is the OAuth 2.0 grant that regular web apps utilize in order to access an API.
        """
        params = {
            'client_id': client_id,
            'audience': audience,
            'response_type': response_type,
            'scope': scope,
            'state': state,
            'redirect_uri': redirect_uri
        }

        return self.get(
            'https://{}/authorize'.format(self.domain),
            params=params)
