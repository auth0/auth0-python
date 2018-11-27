from .base import AuthenticationBase
import warnings


class Database(AuthenticationBase):

    """Database & Active Directory / LDAP Authentication.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

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
        return self.post(
            'https://{}/oauth/ro'.format(self.domain),
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

    def signup(self, client_id, email, password, connection, username=None,
             user_metadata=None):
        """Signup using email and password.
        
        Args:
           client_id (str): ID of the application to use.

           email (str): The user's email address.

           password (str): The user's desired password.

           connection (str): The name of the database connection where this user should be created.

           username (str, optional): The user's username, if required by the database connection.

           user_metadata (dict, optional): Additional key-value information to store for the user.
                    Some limitations apply, see: https://auth0.com/docs/metadata#metadata-restrictions

        See: https://auth0.com/docs/api/authentication#signup
        """
        body = {
            'client_id': client_id,
            'email': email,
            'password': password,
            'connection': connection,
            'username': username,
            'user_metadata': user_metadata
        }

        return self.post(
            'https://{}/dbconnections/signup'.format(self.domain),
            data=body,
            headers={'Content-Type': 'application/json'}
        )

    def change_password(self, client_id, email, connection, password=None):
        """Asks to change a password for a given user.
        """

        return self.post(
            'https://{}/dbconnections/change_password'.format(self.domain),
            data={
                'client_id': client_id,
                'email': email,
                'password': password,
                'connection': connection,
            },
            headers={'Content-Type': 'application/json'}
        )
