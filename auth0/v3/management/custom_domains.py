from .rest import RestClient


class CustomDomains(object):

    """Auth0 custom domains endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, id=None):
        url = 'https://%s/api/v2/custom-domains' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self):
        """Retrieves all custom domains.

        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/get_custom_domains
        """
        return self.client.get(self._url())

    def get(self, id):
        """Retrieves custom domain.

        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/get_custom_domains_by_id
        """
        url = self._url('%s' % (id))
        return self.client.get(url)

    def delete(self, id):
        """Deletes a grant.

        Args:
           id (str): The id of the custom domain to delete


        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/delete_custom_domains_by_id
        """
        url = self._url('%s' % (id))
        return self.client.delete(url)

    def create_new(self, body):
        """Configure a new custom domain

        Args:
           body (str): The domain, tye and verification method in json


        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/post_custom_domains
        """
        return self.client.post(self._url(), data=body)

    def verify(self, id):
        """Verify a custom domain

        Args:
           id (str): The id of the custom domain to delete


        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/post_verify
        """
        url = self._url('%s/verify' % (id))
        return self.client.post(url)