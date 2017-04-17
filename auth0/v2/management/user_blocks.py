from .rest import RestClient


class UserBlocks(object):

    """Auth0 user blocks endpoints

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

    def _url(self, id=None):
        url = 'https://%s/api/v2/user-blocks' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def get_by_identifier(self, identifier):
        """Gets blocks by identifier

        Args:
           identifier (str): Should be any of: username, phone_number, email.
        """

        params = {'identifier': identifier}

        return self.client.get(self._url(), params=params)

    def unblock_by_identifier(self, identifier):
        """Unblocks by identifier

        Args:
           identifier (str): Should be any of: username, phone_number, email.
        """

        params = {'identifier': identifier}

        return self.client.delete(self._url(), params=params)

    def get(self, id):
        """Get a user's blocks

        Args:
           id (str): The user_id of the user to retrieve.
        """

        return self.client.get(self._url(id))

    def unblock(self, id):
        """Unblock a user
        
        Args:
           id (str): The user_id of the user to update.
        """

        return self.client.delete(self._url(id))
