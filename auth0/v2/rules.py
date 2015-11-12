from .rest import RestClient


class Rules(object):

    """Rules endpoint implementation.

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, id=None):
        url = 'https://%s/api/v2/rules' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, stage='login_success', enabled=True, fields=[],
            include_fields=True):
        """Retrieves a list of all rules.
        """

        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower(),
                  'enabled': str(enabled).lower(),
                  'stage': stage}

        return self.client.get(self._url(), params=params)

    def create(self, body):
        return self.client.post(self._url(), data=body)

    def get(self, id, fields=[], include_fields=True):
        params = {'fields': ','.join(fields),
                  'include_fields': str(include_fields).lower()}
        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        return self.client.delete(self._url(id))

    def update(self, id, body):
        return self.client.patch(self._url(id), data=body)
