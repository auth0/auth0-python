from ..rest import RestClient


class Actions:
    """Auth0 Actions endpoints

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """

    def __init__(
        self,
        domain,
        token,
        telemetry=True,
        timeout=5.0,
        protocol="https",
        rest_options=None,
    ):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(
            jwt=token, telemetry=telemetry, timeout=timeout, options=rest_options
        )

    def _url(self, *args):
        url = f"{self.protocol}://{self.domain}/api/v2/actions"
        for p in args:
            if p is not None:
                url = f"{url}/{p}"
        return url

    def get_actions(
        self,
        trigger_id=None,
        action_name=None,
        deployed=None,
        installed=False,
        page=None,
        per_page=None,
    ):
        """Get all actions.

        Args:
           trigger_id (str, optional): Filter the results to only actions associated
                 with this trigger ID.

           action_name (str, optional): Filter the results to only actions with this name.

           deployed (bool, optional): True to filter the results to only deployed actions.
                Defaults to False.

           installed (bool, optional): True to filter the results to only installed actions.
                Defaults to False.

           page (int, optional): The result's page number (zero based). When not set,
                the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
                the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_actions
        """

        if deployed is not None:
            deployed = str(deployed).lower()

        params = {
            "triggerId": trigger_id,
            "actionName": action_name,
            "deployed": deployed,
            "installed": str(installed).lower(),
            "page": page,
            "per_page": per_page,
        }

        return self.client.get(self._url("actions"), params=params)

    def create_action(self, body):
        """Create a new action.

        Args:
           body (dict): Attributes for the new action.

        See: https://auth0.com/docs/api/management/v2#!/Actions/post_action
        """

        return self.client.post(self._url("actions"), data=body)

    def update_action(self, id, body):
        """Updates an action.

        Args:
           id (str): the ID of the action.

           body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Actions/patch_action
        """

        return self.client.patch(self._url("actions", id), data=body)

    def get_action(self, id):
        """Retrieves an action by its ID.

        Args:
           id (str): Id of action to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_action
        """
        params = {}

        return self.client.get(self._url("actions", id), params=params)

    def delete_action(self, id, force=False):
        """Deletes an action and all of its associated versions.

        Args:
           id (str): ID of the action to delete.

           force (bool, optional): True to force action deletion detaching bindings,
               False otherwise. Defaults to False.

        See: https://auth0.com/docs/api/management/v2#!/Actions/delete_action
        """
        params = {"force": str(force).lower()}

        return self.client.delete(self._url("actions", id), params=params)

    def get_triggers(self):
        """Retrieve the set of triggers currently available within actions.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_triggers
        """
        params = {}

        return self.client.get(self._url("triggers"), params=params)

    def get_execution(self, id):
        """Get information about a specific execution of a trigger.

        Args:
           id (str): The ID of the execution to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_execution
        """
        params = {}

        return self.client.get(self._url("executions", id), params=params)

    def get_action_versions(self, id, page=None, per_page=None):
        """Get all of an action's versions.

        Args:
           id (str): The ID of the action.

           page (int, optional): The result's page number (zero based). When not set,
                the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
                the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_action_versions
        """
        params = {"page": page, "per_page": per_page}

        return self.client.get(self._url("actions", id, "versions"), params=params)

    def get_trigger_bindings(self, id, page=None, per_page=None):
        """Get the actions that are bound to a trigger.

        Args:
           id (str): The trigger ID.

           page (int, optional): The result's page number (zero based). When not set,
                the default value is up to the server.

           per_page (int, optional): The amount of entries per page. When not set,
                the default value is up to the server.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_bindings
        """
        params = {"page": page, "per_page": per_page}
        return self.client.get(self._url("triggers", id, "bindings"), params=params)

    def get_action_version(self, action_id, version_id):
        """Retrieve a specific version of an action.

        Args:
           action_id (str): The ID of the action.

           version_id (str): The ID of the version to retrieve.

        See: https://auth0.com/docs/api/management/v2#!/Actions/get_action_version
        """
        params = {}

        return self.client.get(
            self._url("actions", action_id, "versions", version_id), params=params
        )

    def deploy_action(self, id):
        """Deploy an action.

        Args:
           id (str): The ID of the action to deploy.

        See: https://auth0.com/docs/api/management/v2#!/Actions/post_deploy_action
        """
        return self.client.post(self._url("actions", id, "deploy"))

    def rollback_action_version(self, action_id, version_id):
        """Roll back to a previous version of an action.

        Args:
           action_id (str): The ID of the action.

           version_id (str): The ID of the version.

        See: https://auth0.com/docs/api/management/v2#!/Actions/post_deploy_draft_version
        """
        return self.client.post(
            self._url("actions", action_id, "versions", version_id, "deploy"), data={}
        )

    def update_trigger_bindings(self, id, body):
        """Update a trigger's bindings.

        Args:
           id (str): The ID of the trigger to update.

           body (dict): Attributes for the updated trigger binding.

        See: https://auth0.com/docs/api/management/v2#!/Actions/patch_bindings
        """
        return self.client.patch(self._url("triggers", id, "bindings"), data=body)
