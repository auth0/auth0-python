from .rest import RestClient


class LogStreams(object):
    """Auth0 log streams endpoints

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
        url = '{}://{}/api/v2/log-streams'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def list(self):
        """Search log events.

        Args:
        See: https://auth0.com/docs/api/management/v2/#!/Log_Streams/get_log_streams
        """

        return self.client.get(self._url())

    def get(self, id):
        """Retrieves the data related to the log stream entry identified by id.

        Args:
            id (str): The id of the log stream to retrieve.

        See: https://auth0.com/docs/api/management/v2/#!/Log_Streams/get_log_streams_by_id
        """

        return self.client.get(self._url(id))

    def create(self, body):
        """Creates a new log stream.

        Args:
            body (dict): the attributes for the role to create.

        See: https://auth0.com/docs/api/management/v2/#!/Log_Streams/post_log_streams
        """
        return self.client.post(self._url(), data=body)

    def delete(self, id):
        """Delete a log stream.

        Args:
            id (str): The id of the log ste to delete.

        See: https://auth0.com/docs/api/management/v2/#!/Log_Streams/delete_log_streams_by_id
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update a log stream with the attributes passed in 'body'

        Args:
            id (str): The id of the log stream to update.

            body (dict): the attributes to update on the log stream.

        See: https://auth0.com/docs/api/management/v2/#!/Log_Streams/patch_log_streams_by_id
        """
        return self.client.patch(self._url(id), data=body)
