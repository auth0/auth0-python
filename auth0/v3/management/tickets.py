from .rest import RestClient


class Tickets(object):
    """Auth0 tickets endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0, protocol="https"):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, action):
        return '{}://{}/api/v2/tickets/{}'.format(self.protocol, self.domain, action)

    def create_email_verification(self, body):
        """Create an email verification ticket.

        Args:
            body (dict): attributes to set on the email verification request.

        See: https://auth0.com/docs/api/v2#!/Tickets/post_email_verification
        """
        return self.client.post(self._url('email-verification'), data=body)

    def create_pswd_change(self, body):
        """Create password change ticket.

        Args:
            body (dict): attributes to set on the password change request.

        See: https://auth0.com/docs/api/v2#!/Tickets/post_password_change
        """
        return self.client.post(self._url('password-change'), data=body)
