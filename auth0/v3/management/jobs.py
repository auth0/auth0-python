from .rest import RestClient


class Jobs(object):

    """Auth0 jobs endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0):
        self.domain = domain
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout)

    def _url(self, path=None):
        url = 'https://{}/api/v2/jobs'.format(self.domain)
        if path is not None:
            return '{}/{}'.format(url, path)
        return url

    def get(self, id):
        """Retrieves a job. Useful to check its status.

        Args:
            id (str): The id of the job.

        See: https://auth0.com/docs/api/management/v2#!/Jobs/get_jobs_by_id
        """
        return self.client.get(self._url(id))

    def get_failed_job(self, id):
        """Get failed job error details

        Args:
            id (str): The id of the job.

        See: https://auth0.com/docs/api/management/v2#!/Jobs/get_errors
        """
        url = self._url('{}/errors'.format(id))
        return self.client.get(url)

    def get_results(self, job_id):
        """Get results of a job

        Args:
            job_id (str): The ID of the job.

        See: https://auth0.com/docs/api/management/v2#!/Jobs/get_results
        """
        url = self._url('%s/results' % job_id)
        return self.client.get(url)

    def export_users(self, body):
        """Export all users to a file using a long running job.

        Check job status with get(). URL pointing to the export file will be
        included in the status once the job is complete.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/management/v2#!/Jobs/post_users_exports
        """
        return self.client.post(self._url('users-exports'), data=body)

    def import_users(self, connection_id, file_obj, upsert=False):
        """Imports users to a connection from a file.

        Args:
            connection_id (str): The connection id of the connection to which
                users will be inserted.

            file_obj (file): A file-like object to upload. The format for
                this file is explained in: https://auth0.com/docs/bulk-import

        See: https://auth0.com/docs/api/management/v2#!/Jobs/post_users_imports
        """
        return self.client.file_post(self._url('users-imports'),
                                     data={'connection_id': connection_id, 'upsert': str(upsert).lower()},
                                     files={'users': file_obj})

    def send_verification_email(self, body):
        """Send verification email.

        Send an email to the specified user that asks them to click a link to
        verify their email address.

        Args:
            body (dict): Please see: https://auth0.com/docs/api/v2#!/Jobs/post_verification_email
        """
        return self.client.post(self._url('verification-email'), data=body)
