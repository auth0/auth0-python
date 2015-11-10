from .rest import RestClient


class Emails(object):
    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, id=None):
        url = 'https://%s/api/v2/emails/provider' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def get(self, fields=[], include_fields=True):
        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def config(self, body):
        return self.client.post(self._url(), data=body)

    def delete(self):
        return self.client.delete(self._url())

    def update(self, body):
        return self.client.patch(self._url(), data=body)

