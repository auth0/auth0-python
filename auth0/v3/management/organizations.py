from .rest import RestClient


class Organizations(object):
    """Auth0 organizations endpoints

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

    def _url(self, *args):
        url = '{}://{}/api/v2/organizations'.format(self.protocol, self.domain)
        for p in args:
            if p is not None:
                url = '{}/{}'.format(url, p)
        return url

    # Organizations
    def all_organizations(self, page=None, per_page=None):
        """Retrieves a list of all the organizations.

        Args:
           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_organizations
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(), params=params)

    def get_organization_by_name(self, name=None):
        """Retrieves an organization given its name.

        Args:
           name (str): The name of the organization to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_name_by_name
        """
        params = {}

        return self.client.get(self._url('name', name), params=params)

    def get_organization(self, id):
        """Retrieves an organization by its ID.

        Args:
           id (str): Id of organization to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_organizations_by_id
        """
        params = {}

        return self.client.get(self._url(id), params=params)

    def create_organization(self, body):
        """Create a new organization.

        Args:
           body (dict): Attributes for the new organization.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/post_organizations
        """

        return self.client.post(self._url(), data=body)
    
    def update_organization(self, id, body):
        """Modifies an organization.

        Args:
           id (str): the ID of the organization.

           body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/patch_organizations_by_id
        """

        return self.client.patch(self._url(id), data=body)

    def delete_organization(self, id):
        """Deletes an organization and all its related assets.

        Args:
           id (str): Id of organization to delete.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/delete_organizations_by_id
        """

        return self.client.delete(self._url(id))


    # Organization Connections
    def all_organization_connections(self, id, page=None, per_page=None):
        """Retrieves a list of all the organization connections.

        Args:
           id (str): the ID of the organization.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_enabled_connections
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(id, 'enabled_connections'), params=params)

    def get_organization_connection(self, id, connection_id):
        """Retrieves an organization connection by its ID.

        Args:
           id (str): the ID of the organization.

           connection_id (str): the ID of the connection.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_enabled_connections_by_connectionId
        """
        params = {}

        return self.client.get(self._url(id, 'enabled_connections', connection_id), params=params)

    def create_organization_connection(self, id, body):
        """Adds a connection to an organization.

        Args:
           id (str): the ID of the organization.

           body (dict): Attributes for the connection to add.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/post_enabled_connections
        """

        return self.client.post(self._url(id, 'enabled_connections'), data=body)
    
    def update_organization_connection(self, id, connection_id, body):
        """Modifies an organization.

        Args:
           id (str): the ID of the organization.

           connection_id (str): the ID of the connection to update.

           body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/patch_enabled_connections_by_connectionId
        """

        return self.client.patch(self._url(id, 'enabled_connections', connection_id), data=body)

    def delete_organization_connection(self, id, connection_id):
        """Deletes a connection from the given organization.

        Args:
           id (str): Id of organization.

           connection_id (str): the ID of the connection to delete.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/delete_enabled_connections_by_connectionId
        """

        return self.client.delete(self._url(id, 'enabled_connections', connection_id))

    # Organization Members
    def all_organization_members(self, id, page=None, per_page=None):
        """Retrieves a list of all the organization members.

        Args:
           id (str): the ID of the organization.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_members
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(id, 'members'), params=params)

    def create_organization_members(self, id, body):
        """Adds members to an organization.

        Args:
           id (str): the ID of the organization.

           body (dict): Attributes from the members to add.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/post_members
        """

        return self.client.post(self._url(id, 'members'), data=body)

    def delete_organization_members(self, id, body):
        """Deletes members from the given organization.

        Args:
           id (str): Id of organization.

           body (dict): Attributes from the members to delete

        See: https://auth0.com/docs/api/management/v2#!/Organizations/delete_members
        """

        return self.client.delete(self._url(id, 'members'), data=body)

    # Organization Member Roles
    def all_organization_member_roles(self, id, user_id, page=None, per_page=None):
        """Retrieves a list of all the roles from the given organization member.

        Args:
           id (str): the ID of the organization.
           
           user_id (str): the ID of the user member of the organization.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_organization_member_roles
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(id, 'members', user_id, 'roles'), params=params)

    def create_organization_member_roles(self, id, user_id, body):
        """Adds roles to a member of an organization.

        Args:
           id (str): the ID of the organization.

           user_id (str): the ID of the user member of the organization.

           body (dict): Attributes from the members to add.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/post_organization_member_roles
        """

        return self.client.post(self._url(id, 'members', user_id, 'roles'), data=body)

    def delete_organization_member_roles(self, id, user_id, body):
        """Deletes roles from a member of an organization.

        Args:
           id (str): Id of organization.

           user_id (str): the ID of the user member of the organization.

           body (dict): Attributes from the members to delete

        See: https://auth0.com/docs/api/management/v2#!/Organizations/delete_organization_member_roles
        """

        return self.client.delete(self._url(id, 'members', user_id, 'roles'), data=body)


    # Organization Invitations
    def all_organization_invitations(self, id, page=None, per_page=None):
        """Retrieves a list of all the organization invitations.

        Args:
           id (str): the ID of the organization.

           page (int): The result's page number (zero based). When not set,
              the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
              the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_invitations
        """
        params = {}
        params['page'] = page
        params['per_page'] = per_page

        return self.client.get(self._url(id, 'invitations'), params=params)

    def get_organization_invitation(self, id, invitaton_id):
        """Retrieves an organization invitation by its ID.

        Args:
           id (str): the ID of the organization.

           invitaton_id (str): the ID of the invitation.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/get_invitations_by_invitation_id
        """
        params = {}

        return self.client.get(self._url(id, 'invitations', invitaton_id), params=params)

    def create_organization_invitation(self, id, body):
        """Create an invitation to an organization.

        Args:
           id (str): the ID of the organization.

           body (dict): Attributes for the invitation to create.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/post_invitations
        """

        return self.client.post(self._url(id, 'invitations'), data=body)
   
    def delete_organization_invitation(self, id, invitation_id):
        """Deletes an invitation from the given organization.

        Args:
           id (str): Id of organization.

           invitation_id (str): the ID of the invitation to delete.

        See: https://auth0.com/docs/api/management/v2#!/Organizations/delete_invitations_by_invitation_id
        """

        return self.client.delete(self._url(id, 'invitations', invitation_id))
