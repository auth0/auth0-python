from .base import AuthenticationBase


class RevokeToken(AuthenticationBase):

    """Revoke Refresh Token endpoint

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def revoke_refresh_token(self, client_id, token, client_secret=None):
        """Revokes a Refresh Token if it has been compromised
           
           Each revocation request invalidates not only the specific token, but all other tokens 
           based on the same authorization grant. This means that all Refresh Tokens that have 
           been issued for the same user, application, and audience will be revoked.

           Args:
                client_id (str): your application's client Id

                token (str): the Refresh Token you want to revoke

                client_secret (str, optional): Your application's Client Secret. 
                        Required for confidential applications.
            
            See: https://auth0.com/docs/api/authentication#refresh-token
        """
        body = {
            'client_id': client_id,
            'token': token,
            'client_secret': client_secret
        }

        return self.post(
            'https://{}/oauth/revoke'.format(self.domain), data=body)
