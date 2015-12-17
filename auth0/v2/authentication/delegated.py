from .base import AuthenticationBase


class Delegated(AuthenticationBase):

    def __init__(self, domain):
        self.domain = domain

    def get_token(self, client_id, target, api_type, grant_type,
                  id_token=None, refresh_token=None):

        if id_token and refresh_token:
            raise ValueError('Only one of id_token or refresh_token '
                             'can be None')

        data = {
            'client_id': client_id,
            'grant_type': grant_type,
            'target': target,
            'scope': 'openid',
            'api_type': api_type,
        }

        if id_token:
            data.update({'id_token': id_token})
        elif refresh_token:
            data.update({'refresh_token': refresh_token})
        else:
            raise ValueError('Either id_token or refresh_token must '
                             'have a value')

        return self.post(
            'https://%s/delegation' % self.domain,
            headers={'Content-Type': 'application/json'},
            data=data
        )
