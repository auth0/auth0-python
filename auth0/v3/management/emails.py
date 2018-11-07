from .rest import RestClient


class Emails(object):

    """Auth0 email endpoints

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
        url = 'https://{}/api/v2/emails/provider'.format(self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def get(self, fields=None, include_fields=True):
        """Get the email provider.

        Args:
            fields (list of str, optional): A list of fields to include or
                exclude from the result (depending on include_fields). Empty
                to retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise.

        See: https://auth0.com/docs/api/management/v2#!/Emails/get_provider
        """
        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}

        return self.client.get(self._url(), params=params)

    def config(self, body):
        """Configure the email provider.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Emails/post_provider
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
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Emails/patch_provider
        """
        return self.client.patch(self._url(), data=body)
