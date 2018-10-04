import sys
from requests.compat import urlencode, urlunparse, quote_plus
from .base import AuthenticationBase

_ver = '{}{}{}'.format(*sys.version_info)


class AuthorizeClient(AuthenticationBase):
    """Authorize Client

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def get_authorize_url(self, client_id, audience=None, state=None, redirect_uri=None,
                          response_type='code', scope='openid', quote_via=quote_plus):
        """
        use quote_via=urllib.quote to to urlencode spaces into "%20", the default is "+"
        """
        params = {
            'client_id': client_id,
            'audience': audience,
            'response_type': response_type,
            'scope': scope,
            'state': state,
            'redirect_uri': redirect_uri
        }
        query = urlencode(params, doseq=True, quote_via=quote_via) \
            if _ver > '34' \
            else '&'.join(['{}={}'.format(quote_via(k, safe=''), quote_via(v, safe=''))
                           for k, v in params.items()])
        return urlunparse(['https', self.domain, '/authorize', None, query, None])

    def authorize(self, client_id, audience=None, state=None, redirect_uri=None,
                  response_type='code', scope='openid'):
        """Authorization code grant

        This is the OAuth 2.0 grant that regular web apps utilize in order to access an API.
        """
        params = {
            'client_id': client_id,
            'audience': audience,
            'response_type': response_type,
            'scope': scope,
            'state': state,
            'redirect_uri': redirect_uri
        }

        return self.get(
            'https://%s/authorize' % self.domain,
            params=params)
