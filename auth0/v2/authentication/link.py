from .base import AuthenticationBase


class Link(AuthenticationBase):

    def __init__(self, domain):
        self.domain = domain

    def unlink(self, access_token, user_id):
        return self.post(
            url='https://%s/unlink' % self.domain,
            data={
                'access_token': access_token,
                'user_id': user_id,
            },
            headers={'Content-Type': 'application/json'}
        )
