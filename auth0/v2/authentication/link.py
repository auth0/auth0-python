from .base import AuthenticationBase


class Link(AuthenticationBase):

    """Link accounts endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def unlink(self, access_token, user_id):
        """Unlink an account.
        """

        return self.post(
            url='https://%s/unlink' % self.domain,
            data={
                'access_token': access_token,
                'user_id': user_id,
            },
            headers={'Content-Type': 'application/json'}
        )
