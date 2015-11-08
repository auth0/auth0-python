from .rest import RestClient


class Tickets(object):

    """Auth0 tickets endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, action):
        return 'https://%s/api/v2/tickets/%s' % (self.domain, action)

    def create_email_verification(self, body):
        return self.client.post(self._url('email-verification'), data=body)

    def create_pswd_change(self, body):
        return self.client.post(self._url('password-change'), data=body)
