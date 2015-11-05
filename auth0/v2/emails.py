from .rest import RestClient


class Emails(object):
    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/emails/provider' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

    def get(self, fields=[], include_fields=True):
        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(params=params)

    def config(self, body):
        return self.client.post(data=body)

    def delete(self):
        return self.client.delete(id=None)

    def update(self, body):
        return self.client.patch(data=body)

