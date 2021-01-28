from .rest import RestClient


class Emails(object):
    """Auth0 email endpoints

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

    def _url(self, id=None):
        url = '{}://{}/api/v2/emails/provider'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def get(self, fields=None, include_fields=True):
        """Get the email provider.

        Args:
            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Leave empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise. Defaults to True.

        See: https://auth0.com/docs/api/management/v2#!/Emails/get_provider
        """
        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def config(self, body):
        """Configure the email provider.

        Args:
            body (dict): attributes of the created email provider.

        See: https://auth0.com/docs/api/v2#!/Emails/post_provider
        """
        return self.client.post(self._url(), data=body)

    def delete(self):
        """Delete the email provider. (USE WITH CAUTION)

        See: https://auth0.com/docs/api/management/v2#!/Emails/delete_provider
        """
        return self.client.delete(self._url())

    def update(self, body):
        """Update the email provider.

        Args:
            body (dict): attributes to update on the email provider

        See: https://auth0.com/docs/api/v2#!/Emails/patch_provider
        """
        return self.client.patch(self._url(), data=body)
