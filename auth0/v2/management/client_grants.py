from .rest import RestClient


class ClientGrants(object):

    """Auth0 client grants

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
	    return ('https://%s/api/v2/client-grants/%s' % (self.domain, id))
	else:
	    return ('https://%s/api/v2/client-grants' % (self.domain))

    def all(self, audience=None):
        """Retrieves a list of all client grants.

        Requires the read:client_grants Auth0 Management API scope.

        See: https://auth0.com/docs/api/management/v2#!/Client_Grants/get_client_grants
        Args:
            audience: "" # filter by the audience (resource_servers.identifier) to authenticate against.
        """
        params = {"audience": audience}
        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Create a new client grant.
	
	Requires the create:client_grants Auth0 Management API scope.

        See: https://auth0.com/docs/api/management/v2#!/Client_Grants/post_client_grants

        Args:
            body: {
		# (required) The client ID to grant to
		"client_id": "",

		# (required) The audience (resource_servers.identifier) to authenticate against.
		"audience": "",
		
		# The scope values for audience to grant to this client.
		"scope": [
		    "read:testscope",
		]
	    }
        """
        return self.client.post(self._url(), data=body)

    def delete(self, id):
        """Deletes a client grant.

	Requires the delete:client_grants Auth0 Management API scope.

	See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/delete_client_grants_by_id

        Args:
            id (str): Id of the client grant to delete.
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Modifies a client.

	Requires the update:client_grants Auth0 Management API scope.

        Note: The body MUST NOT contain "id" or "identifier", so if you are calling this on the results from a get or create, first use
            `del result["id"]
             del result["identifier"]`

	See: https://auth0.com/docs/api/management/v2#!/Resource_Servers/patch_client_grants_by_id
        
        Args:
            id (str): Resource server idenitifier.
            body: {
		# (optional) The name of the client grant. Must contain at least one character. Does not allow '<' or '>'
	        "name": "",

		# (optional) The algorithm used to sign tokens ['HS256' or 'RS256']
	        "signing_alg": "",

		# (optional) The secret used to sign tokens when using symmetric algorithms
	        "signing_secret": "", 

		#(optional) The amount of time (in seconds) that the token will be valid after being issued
	        "token_lifetime": 0, 

		# (optional) An exhaustive list of all scopes grantable on this client grant.
	        "scopes": [
                    {"value":"read:testscope", "description":"My test scope!"},
	        ],
	    }
        """
        return self.client.patch(self._url(id), data=body)
