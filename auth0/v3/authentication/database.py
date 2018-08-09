from .base import AuthenticationBase
import warnings
from .utils.token_verifier import TokenVerifier
from .utils.jwk_provider import UrlJwkProvider

class Database(AuthenticationBase):

    """Database & Active Directory / LDAP Authentication.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain, token_verifier=None):
        self.domain = domain
        self.token_verifier = token_verifier or TokenVerifier(UrlJwkProvider(domain))

    def login(self, client_id, username, password, connection, id_token=None,
              grant_type='password', device=None, scope='openid'):
        """Login using username and password

        Given the user credentials and the connection specified, it will do
        the authentication on the provider and return a dict with the
        access_token and id_token. This endpoint only works for database
        connections, passwordless connections, Active Directory/LDAP,
        Windows Azure AD and ADFS.
        """
        warnings.warn("/oauth/ro will be deprecated in future releases", DeprecationWarning)
        result = self.post(
            'https://%s/oauth/ro' % self.domain,
            data={
                'client_id': client_id,
                'username': username,
                'password': password,
                'id_token': id_token,
                'connection': connection,
                'device': device,
                'grant_type': grant_type,
                'scope': scope,
            },
            headers={'Content-Type': 'application/json'}
        )
        id_token = 'id_token' in result and result['id_token']
        if id_token: 
            self.token_verifier.verify(id_token, client_id)
        return result

    def signup(self, client_id, email, password, connection):
        """Signup using username and password.
        """

        return self.post(
            'https://%s/dbconnections/signup' % self.domain,
            data={
                'client_id': client_id,
                'email': email,
                'password': password,
                'connection': connection,
            },
            headers={'Content-Type': 'application/json'}
        )

    def change_password(self, client_id, email, connection, password=None):
        """Asks to change a password for a given user.
        """

        return self.post(
            'https://%s/dbconnections/change_password' % self.domain,
            data={
                'client_id': client_id,
                'email': email,
                'password': password,
                'connection': connection,
            },
            headers={'Content-Type': 'application/json'}
        )
