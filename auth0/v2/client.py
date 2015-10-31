from .rest import RestClient


class Client(object):

    """Docstring for Client. """

    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/clients' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

    def all(self, fields=[], include_fields=True):
        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(params=params)

    def create(self, body):
        return self.client.post(data=body)

    def get(self, id, fields=[], include_fields=True):
        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(id=id, params=params)

    def delete(self, id):
        return self.client.delete(id=id)

    def update(self, id, body):
        return self.client.patch(id=id, data=body)
