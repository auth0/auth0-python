from .base import AuthenticationBase


class GetToken(AuthenticationBase):

    """Database & Active Directory / LDAP Authentication.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def authorization_code(self, client_id, client_secret, code, #Check the name
              grant_type='authorization_code', redirect_uri):
        """Authorization code grant
        
        This is the OAuth 2.0 grant that regular web apps utilize in order 
        to access an API. Use this endpoint to exchange an Authorization Code 
        for a Token.
        """

        return self.post(
            'https://%s/oauth/token' % self.domain,
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'code': code,
                'grant_type': grant_type,
                'redirect_uri': redirect_uri,
            },
            headers={'Content-Type': 'application/json'}
        )

    def login(self, client_id, client_secret, username, password, scope, realm
        audience, grant_type='http://auth0.com/oauth/grant-type/password-realm'):
        """Calls oauth/token endpoint with password-realm grant type


        This is the OAuth 2.0 grant that highly trusted apps utilize in order 
        to access an API. In this flow the end-user is asked to fill in credentials 
        (username/password) typically using an interactive form in the user-agent 
        (browser). This information is later on sent to the client and Auth0. 
        It is therefore imperative that the client is absolutely trusted with 
        this information.
        """

        return self.post(
            'https://%s/oauth/token' % self.domain,
            data={
                'client_id': client_id,
                'username': username,
                'password': password,
                'realm': realm,
                'client_secret': client_secret,
                'scope': scope,
                'audience': audience,
                'grant_type': grant_type
            },
            headers={'Content-Type': 'application/json'}
        )

