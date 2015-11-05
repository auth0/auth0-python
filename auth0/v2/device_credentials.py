from .rest import RestClient


class DeviceCredentials(object):

    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/device-credentials' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

    def get(self, user_id=None, client_id=None, type=None,
            fields=[], include_fields=True):
        params = {
            'fields': ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'user_id': user_id,
            'client_id': client_id,
            'type': type,
        }
        return self.client.get(params=params)

    def create(self, body):
        return self.client.post(data=body)

    def delete(self, id):
        return self.client.delete(id=id)
