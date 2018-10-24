from .rest import RestClient


class CustomDomains(object):

    """Auth0 custom domains endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, id=None):
        url = 'https://%s/api/v2/custom-domains' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def get_all(self):
        """Retrieves all custom domains.
            
        See: https://auth0.com/docs/api/management/v2#!/Custom_Domains/get_custom_domains
        """

        return self.client.get(self._url())

    def delete(self, id):
        """Deletes a grant.

        Args:
           id (str): The id of the grant to delete


        See: https://auth0.com/docs/api/management/v2#!/Grants/delete_grants_by_id
        """
        url = self._url('%s' % (id))
        return self.client.delete(url)