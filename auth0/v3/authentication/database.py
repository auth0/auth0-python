import warnings

from .base import AuthenticationBase


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

        body = {
            'client_id': client_id,
            'username': username,
            'password': password,
            'connection': connection,
            'grant_type': grant_type,
            'scope': scope,
        }
        if id_token:
            body.update({'id_token': id_token})
        if device:
            body.update({'device': device})
        return self.post('{}://{}/oauth/ro'.format(self.protocol, self.domain), data=body)

    def signup(self, client_id, email, password, connection, username=None, user_metadata=None,
               given_name=None, family_name=None, name=None, nickname=None, picture=None):
        """Signup using email and password.

        Args:
           client_id (str): ID of the application to use.

           email (str): The user's email address.

           password (str): The user's desired password.

           connection (str): The name of the database connection where this user should be created.

           username (str, optional): The user's username, if required by the database connection.

           user_metadata (dict, optional): Additional key-value information to store for the user.
                    Some limitations apply, see: https://auth0.com/docs/metadata#metadata-restrictions

           given_name (str, optional): The user's given name(s).

           family_name (str, optional): The user's family name(s).

           name (str, optional): The user's full name.

           nickname (str, optional): The user's nickname.

           picture (str, optional): A URI pointing to the user's picture.


        See: https://auth0.com/docs/api/authentication#signup
        """
        body = {
            'client_id': client_id,
            'email': email,
            'password': password,
            'connection': connection,
        }
        if username:
            body.update({'username': username})
        if user_metadata:
            body.update({'user_metadata': user_metadata})
        if given_name:
            body.update({'given_name': given_name})
        if family_name:
            body.update({'family_name': family_name})
        if name:
            body.update({'name': name})
        if nickname:
            body.update({'nickname': nickname})
        if picture:
            body.update({'picture': picture})

        return self.post('{}://{}/dbconnections/signup'.format(self.protocol, self.domain), data=body)

    def change_password(self, client_id, email, connection, password=None):
        """Asks to change a password for a given user.
            
           client_id (str): ID of the application to use.

           email (str): The user's email address.

           connection (str): The name of the database connection where this user should be created.
        """
        body = {
            'client_id': client_id,
            'email': email,
            'connection': connection,
        }
        
        return self.post('{}://{}/dbconnections/change_password'.format(self.protocol, self.domain), data=body)
