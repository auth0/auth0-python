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

    def _defaults(self, params):
        params.setdefault('response_type', 'code')
        params.setdefault('scope', 'openid')
        return params

    def get_authorize_url(self, quote_via=quote_plus, **kwargs):
        """
        :param quote_via: callable
        :param client_id: str
        :param audience: str
        :param state: str
        :param redirect_uri: str
        :param response_type: str
        :param scope: str
        :return: str
        """

        params = urlencode(self._defaults(kwargs), doseq=True, quote_via=quote_via) \
            if _ver > '34' \
            else '&'.join(['{}={}'.format(quote_via(k, safe=''), quote_via(v, safe=''))
                           for k, v in self._defaults(kwargs).items()])
        return urlunparse(['https', self.domain, '/authorize', None, params, None])

    def authorize(self, **kwargs):
        """Authorization code grant

        This is the OAuth 2.0 grant that regular web apps utilize in order to access an API.

        :param client_id: str
        :param audience: str
        :param state: str
        :param redirect_uri: str
        :param response_type: str
        :param scope: str
        :return: Response
        """
        return self.get(
            'https://%s/authorize' % self.domain,
            params=self._defaults(kwargs))
