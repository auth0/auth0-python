from .rest import RestClient


class Users(object):

    """Auth0 users endpoints

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
        url = 'https://%s/api/v2/users' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def list(self, per_page, page, include_totals, sort, connection,
             q, search_engine, fields=[], include_fields=True):
        params = {
            'per_page': per_page,
            'page': page,
            'include_totals': include_totals,
            'sort': sort,
            'connection': connection,
            'fields': ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'q': q,
            'search_engine': search_engine
        }
        return self.client.get(self._url(), params=params)

    def create(self, body):
        return self.client.post(self._url(), data=body)

    def delete_all_users(self):
        return self.client.delete(self._url())

    def get(self, id, fields=[], include_fields=True):
        params = {
            'fields': ','.join(fields) or None,
            'include_fields': str(include_fields).lower()
        }

        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        return self.client.delete(self._url(id))

    def update(self, id, body):
        return self.client.patch(self._url(id), data=body)

    def delete_multifactor(self, id, provider):
        url = self._url('%s/multifactor/%s' % (id, provider))
        return self.client.delete(url)

    def unlink_user_account(self, id, provider, user_id):
        url = self._url('%s/identities/%s/%s' % (id, provider, user_id))
        return self.client.delete(url)
