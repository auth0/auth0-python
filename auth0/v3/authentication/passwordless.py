from .base import AuthenticationBase


class Passwordless(AuthenticationBase):

    """Passwordless connections endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def email(self, client_id, email, send='link', auth_params=None, client_secret=None):
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
            client_id (str): Client Id of the application.

            email (str): Email address.

            send (str, optional): Can be: 'link' or 'code'. Defaults to 'link'.

            auth_params (dict, optional): Parameters to append or override.

            client_secret (str): Client Secret of the application.
        """

        return self.post(
            'https://{}/passwordless/start'.format(self.domain),
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'connection': 'email',
                'email': email,
                'send': send,
                'authParams': auth_params
            }
        )

    def sms(self, client_id, phone_number, client_secret=None):
        """Start flow sending an SMS message.

        Given the user phone number, it will send an SMS with 
        a verification code. You can then authenticate with
        this user using phone number as username and code as password.

        Args:
            client_id (str): Client Id of the application.

            client_secret (str): Client Secret of the application.

            phone_number (str): Phone number.
        """

        return self.post(
            'https://{}/passwordless/start'.format(self.domain),
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'connection': 'sms',
                'phone_number': phone_number,
            }
        )

    def sms_login(self, client_id, phone_number, code, scope='openid'):
        """Login using phone number/verification code.

        Args:
            client_id (str): Client Id of the application.

            phone_number (str): Phone number.

            code (str): Code received in the SMS.

            scope (str, optional): Scope to use. Defaults to 'openid'.
        """

        return self.post(
            'https://{}/oauth/ro'.format(self.domain),
            data={
                'client_id': client_id,
                'connection': 'sms',
                'grant_type': 'password',
                'username': phone_number,
                'password': code,
                'scope': scope,
            }
        )
