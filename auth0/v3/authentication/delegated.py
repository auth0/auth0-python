from .base import AuthenticationBase
from .utils.token_verifier import TokenVerifier

class Delegated(AuthenticationBase):

    """Delegated authentication endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain, token_verifier=None):
        self.domain = domain
        self.token_verifier = token_verifier or TokenVerifier(domain)

    def get_token(self, client_id, target, api_type, grant_type,
                  id_token=None, refresh_token=None, scope='openid'):

        """Obtain a delegation token.
        """

        if id_token and refresh_token:
            raise ValueError('Only one of id_token or refresh_token '
                             'can be None')

        data = {
            'client_id': client_id,
            'grant_type': grant_type,
            'target': target,
            'scope': scope,
            'api_type': api_type,
        }

        if id_token:
            data.update({'id_token': id_token})
        elif refresh_token:
            data.update({'refresh_token': refresh_token})
        else:
            raise ValueError('Either id_token or refresh_token must '
                             'have a value')

        result = self.post(
            'https://%s/delegation' % self.domain,
            headers={'Content-Type': 'application/json'},
            data=data
        )
        id_token = 'id_token' in result and result['id_token']
        if id_token: 
            self.token_verifier.verify(id_token, client_id)
        return result
