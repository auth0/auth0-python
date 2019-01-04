from .rest import RestClient


class Grants(object):

    """Auth0 grants endpoints

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
        url = 'https://%s/api/v2/grants' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, page=None, per_page=None, include_totals=False, extra_params=None):
        """Retrieves all grants.

        Args:
            page (int, optional): The result's page number (zero based).

            per_page (int, optional): The amount of entries per page.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise.

           extra_params (dictionary, optional): The extra parameters to add to
             the request. The page, per_page, and include_totals values
             specified as parameters take precedence over the ones defined here.
            
        See: https://auth0.com/docs/api/management/v2#!/Grants/get_grants
        """
        params = extra_params or {}
        params.update({
            'page': page,
            'per_page': per_page,
            'include_totals': str(include_totals).lower()
        })

        return self.client.get(self._url(), params=params)

    def delete(self, id):
        """Deletes a grant.

        Args:
           id (str): The id of the grant to delete


        See: https://auth0.com/docs/api/management/v2#!/Grants/delete_grants_by_id
        """
        url = self._url('%s' % (id))
        return self.client.delete(url)