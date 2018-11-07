from .rest import RestClient


class Tenants(object):

    """Auth0 tenants endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self):
        return 'https://{}/api/v2/tenants/settings'.format(self.domain)

    def get(self, fields=None, include_fields=True):
        """Get tenant settings.

        Args:
           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise.
              
           See: https://auth0.com/docs/api/management/v2#!/Tenants/get_settings
        """

        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def update(self, body):
        """Update tenant settings.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Tenants/patch_settings
        """
        return self.client.patch(self._url(), data=body)
