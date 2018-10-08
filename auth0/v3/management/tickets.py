from .rest import RestClient


class Tickets(object):

    """Auth0 tickets endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, action):
        return 'https://{}/api/v2/tickets/{}'.format(self.domain, action)

    def create_email_verification(self, body):
        """Create an email verification ticket.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Tickets/post_email_verification
        """
        return self.client.post(self._url('email-verification'), data=body)

    def create_pswd_change(self, body):
        """Create password change ticket.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Tickets/post_password_change
        """
        return self.client.post(self._url('password-change'), data=body)
