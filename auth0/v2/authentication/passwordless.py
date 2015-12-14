import requests


class Passwordless(object):

    def __init__(self, domain):
        self.domain = domain

    def email(self, client_id, email, send, auth_params):
        """Start flow sending an email.
        """

        return requests.post(
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

        return requests.post(
            'https://%s/passwordless/start' % self.domain,
            data={
                'client_id': client_id,
                'connection': 'sms',
                'email': email,
                'phone_number': phone_number,
            },
            headers={'Content-Type': 'application/json'}
        )

    def sms_login(self, client_id, phone_number, code):
        """Login using phone number/verification code.
        """

        return requests.post(
            'https://%s/passwordless/start' % self.domain,
            data={
                'client_id': client_id,
                'connection': 'sms',
                'grant_type': 'password',
                'username': phone_number,
                'password': code,
                'scope': 'openid',
            },
            headers={'Content-Type': 'application/json'}
        )
