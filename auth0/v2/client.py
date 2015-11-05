from .rest import RestClient


class Client(object):

    """Docstring for Client. """

    def __init__(self, domain, jwt_token):
        url = 'https://%s/api/v2/clients' % domain

        self.client = RestClient(endpoint=url, jwt=jwt_token)

    def all(self, fields=[], include_fields=True):
        """Retrieves a list of all client applications.

        Important: The client_secret and encryption_key attributes can only be
        retrieved with the read:client_keys scope.

        Args:
           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be include in the result, False otherwise.
        """

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
