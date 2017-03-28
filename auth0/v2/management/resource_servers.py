from .rest import RestClient


class ResourceServers(object):

    """Auth0 resource servers (APIs in dashboard)

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
        if id is not None:
	    return ('https://%s/api/v2/resource-servers/%s' % (self.domain, id))
	else:
	    return ('https://%s/api/v2/resource-servers' % (self.domain))

    def all(self, fields=[], include_fields=True):
        """Retrieves a list of all resource servers.

        Requires the read:resource_servers Auth0 Management API scope.

        See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/get_resource_servers
        """
        return self.client.get(self._url())

    def create(self, body):
        """Create a new resource server.
	
	Requires the create:resource_servers Auth0 Management API scope.

        See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/post_resource_servers

        Args:
            body: {
                # (required, sets "audience") The audience identifier of the resource server. Definitely different than 'id', which is provided by this call.
	        "identifier": "",

		# (optional) The name of the resource server. Must contain at least one character. Does not allow '<' or '>'
	        "name": "",

		# (optional) The algorithm used to sign tokens ['HS256' or 'RS256']
	        "signing_alg": "",

		# (optional) The secret used to sign tokens when using symmetric algorithms
	        "signing_secret": "", 

		# (optional) The amount of time (in seconds) that the token will be valid after being issued
	        "token_lifetime": 0, 

		# (optional) An exhaustive list of all scopes grantable on this resource server.
	        "scopes": [
	    	    "scope"
	        ],
	    }
        """
        return self.client.post(self._url(), data=body)

    def get(self, id):
        """Retrieves a resource server by its id.

	Requires the read:resource_servers Auth0 Management API scope.

	See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/get_resource_servers_by_id

        Args:
            id (str): Id of the resource server to get.
        """
        return self.client.get(self._url(id))

    def delete(self, id):
        """Deletes a resource server.

	Requires the delete:resource_servers Auth0 Management API scope.

	See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/delete_resource_servers_by_id

        Args:
            id (str): Identifier of client to delete.
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client.

	Requires the update:resource_servers Auth0 Management API scope.

        Note: The body MUST NOT contain "id" or "identifier", so if you are calling this on the results from a get or create, first use
            `del result["id"]
             del result["identifier"]`

	See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/patch_resource_servers_by_id
        
        Args:
            id (str): Resource server idenitifier.
            body: {
		# (optional) The name of the resource server. Must contain at least one character. Does not allow '<' or '>'
	        "name": "",

		# (optional) The algorithm used to sign tokens ['HS256' or 'RS256']
	        "signing_alg": "",

		# (optional) The secret used to sign tokens when using symmetric algorithms
	        "signing_secret": "", 

		#(optional) The amount of time (in seconds) that the token will be valid after being issued
	        "token_lifetime": 0, 

		# (optional) An exhaustive list of all scopes grantable on this resource server.
	        "scopes": [
                    {"value":"read:testscope", "description":"My test scope!"},
	        ],
	    }
        """
        return self.client.patch(self._url(id), data=body)
