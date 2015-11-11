from .rest import RestClient


class Jobs(object):

    """Auth0 jobs endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.domain = domain
        self.client = RestClient(jwt=jwt_token)

    def _url(self, path=None):
        url = 'https://%s/api/v2/jobs' % self.domain
        if path is not None:
            return url + '/' + path
        return url

    def get(self, id):
        return self.client.get(self._url(id))

    def import_users(self, connection_id, file_obj):
        return self.client.file_post(self._url('users-imports'),
                                     data={'connection_id': connection_id},
                                     files={'users': file_obj})

    def send_verification_email(self, body):
        return self.client.post(self._url('verification-email'), data=body)
