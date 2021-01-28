from .rest import RestClient


class Tenants(object):
    """Auth0 tenants endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0, protocol="https"):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self):
        return '{}://{}/api/v2/tenants/settings'.format(self.protocol, self.domain)

    def get(self, fields=None, include_fields=True):
        """Get tenant settings.

        Args:
           fields (list of str, optional): A list of fields to include or
              exclude from the result (depending on include_fields). Leave empty to
              retrieve all fields.

           include_fields (bool, optional): True if the fields specified are
              to be included in the result, False otherwise. Defaults to True.
              
        See: https://auth0.com/docs/api/management/v2#!/Tenants/get_settings
        """

        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def update(self, body):
        """Update tenant settings.

        Args:
            body (dict): the attributes to update in the tenant.

        See: https://auth0.com/docs/api/v2#!/Tenants/patch_settings
        """
        return self.client.patch(self._url(), data=body)
