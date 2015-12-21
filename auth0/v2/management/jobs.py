from .rest import RestClient


class Jobs(object):

    """Auth0 jobs endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry)

    def _url(self, path=None):
        url = 'https://%s/api/v2/jobs' % self.domain
        if path is not None:
            return url + '/' + path
        return url

    def get(self, id):
        """Retrieves a job. Useful to check its status.

        Args:
            id (str): The id of the job.
        """
        return self.client.get(self._url(id))

    def import_users(self, connection_id, file_obj):
        """Imports users to a connection from a file.

        Args:
            connection_id (str): The connection id of the connection to which
                users will be inserted.

            file_obj (file): A file-like object to upload. The format for
                this file is explained in: https://auth0.com/docs/bulk-import
        """
        return self.client.file_post(self._url('users-imports'),
                                     data={'connection_id': connection_id},
                                     files={'users': file_obj})

    def send_verification_email(self, body):
        """Send verification email.

        Send an email to the specified user that asks them to click a link to
        verify their email address.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Jobs/post_verification_email
        """
        return self.client.post(self._url('verification-email'), data=body)
