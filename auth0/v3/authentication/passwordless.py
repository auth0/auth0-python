from .base import AuthenticationBase


class Passwordless(AuthenticationBase):

    """Passwordless connections endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def email(self, client_id, email, send='link', auth_params={}):
        """Start flow sending an email.

        Given the user email address, it will send an email with:

          - A link (default, send:"link"). You can then authenticate with
            this user opening the link and he will be automatically logged in
            to the application. Optionally, you can append/override
            parameters to the link (like scope, redirect_uri, protocol,
            response_type, etc.) using auth_params dict.

          - A verification code (send:"code"). You can then authenticate with
            this user using email as username and code as password.

        Args:
            client_id (str): Id of the client.

            email (str): Email address.

            send (str, optional): Can be: 'link' or 'code'. Defaults to 'link'.

            auth_params (dict, optional): Parameters to append or override.
        """

        return self.post(
            'https://%s/passwordless/start' % self.domain,
            data={
                'client_id': client_id,
                'connection': 'email',
                'email': email,
                'send': send,
                'authParams': auth_params,
            },
            headers={'Content-Type': 'application/json'}
        )

    def sms(self, client_id, phone_number):
        """Start flow sending a SMS message.
        """

        return self.post(
            'https://%s/passwordless/start' % self.domain,
            data={
                'client_id': client_id,
                'connection': 'sms',
                'phone_number': phone_number,
            },
            headers={'Content-Type': 'application/json'}
        )

    def sms_login(self, client_id, phone_number, code, scope='openid'):
        """Login using phone number/verification code.
        """

        return self.post(
            'https://%s/oauth/ro' % self.domain,
            data={
                'client_id': client_id,
                'connection': 'sms',
                'grant_type': 'password',
                'username': phone_number,
                'password': code,
                'scope': scope,
            },
            headers={'Content-Type': 'application/json'}
        )
