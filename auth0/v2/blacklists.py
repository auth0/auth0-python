from .rest import RestClient


class Blacklists(object):
    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/blacklists/tokens' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

    def get(self, aud=None):
        params = {
            'aud': aud
        }

        return self.client.get(params=params)

    def create(self, jti, aud=''):
        return self.client.post(data={'jti': jti, 'aud': aud})
