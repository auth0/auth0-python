from .rest import RestClient


class Blacklists(object):
    def __init__(self, domain, jwt_token):
        self.url = 'https://%s/api/v2/blacklists/tokens' % domain
        self.client = RestClient(jwt=jwt_token)

    def get(self, aud=None):
        params = {
            'aud': aud
        }

        return self.client.get(self.url, params=params)

    def create(self, jti, aud=''):
        return self.client.post(self.url, data={'jti': jti, 'aud': aud})
