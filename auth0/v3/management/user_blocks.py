from .rest import RestClient


class UserBlocks(object):
    """Auth0 user blocks endpoints

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
        url = '{}://{}/api/v2/user-blocks'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def get_by_identifier(self, identifier):
        """Gets blocks by identifier

        Args:
           identifier (str): Should be any of: username, phone_number, email.

        See: https://auth0.com/docs/api/management/v2#!/User_Blocks/get_user_blocks
        """

        params = {'identifier': identifier}

        return self.client.get(self._url(), params=params)

    def unblock_by_identifier(self, identifier):
        """Unblocks by identifier

        Args:
           identifier (str): Should be any of: username, phone_number, email.

        See: https://auth0.com/docs/api/management/v2#!/User_Blocks/delete_user_blocks
        """

        params = {'identifier': identifier}

        return self.client.delete(self._url(), params=params)

    def get(self, id):
        """Get a user's blocks

        Args:
           id (str): The user_id of the user to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/User_Blocks/get_user_blocks_by_id
        """

        return self.client.get(self._url(id))

    def unblock(self, id):
        """Unblock a user

        Args:
           id (str): The user_id of the user to update.

        See: https://auth0.com/docs/api/management/v2#!/User_Blocks/delete_user_blocks_by_id
        """

        return self.client.delete(self._url(id))
