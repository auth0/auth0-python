from .base import AuthenticationBase


class Users(AuthenticationBase):

    def __init__(self, domain):
        self.domain = domain

    def userinfo(self, access_token):
        return self.get(
            url='https://%s/userinfo' % self.domain,
            headers={'Authorization': 'Bearer %s' % access_token}
        )

    def tokeninfo(self, jwt):
        return self.post(
            url='https://%s/tokeninfo' % self.domain,
            data={'id_token': jwt},
            headers={'Content-Type: application/json'}
        )
