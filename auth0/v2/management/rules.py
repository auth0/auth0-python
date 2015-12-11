from .rest import RestClient


class Rules(object):

    """Rules endpoint implementation.

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
        url = 'https://%s/api/v2/rules' % self.domain
        if id is not None:
            return url + '/' + id
        return url

    def all(self, stage='login_success', enabled=True, fields=[],
            include_fields=True):
        """Retrieves a list of all rules.

        Args:
            enabled (bool, optional): If provided, retrieves rules that match
                the value, otherwise all rules are retrieved.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise
                (defaults to true).

            stage (str, optional):  Retrieves rules that match the execution
                stage (defaults to login_success).
        """

        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower(),
                  'enabled': str(enabled).lower(),
                  'stage': stage}

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a new rule.

        Args:
            body (dict): Attributes for the newly created rule,
                please see: https://auth0.com/docs/api/v2#!/Rules/post_rules
        """
        return self.client.post(self._url(), data=body)

    def get(self, id, fields=[], include_fields=True):
        """Retrieves a rule by its ID.

        Args:
            id (str): The id of the rule to retrieve.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result, empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise
                (defaults to true).
        """
        params = {'fields': ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}
        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Delete a rule.

        Args:
            id (str): The id of the rule to delete.
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update an existing rule

        Args:
            id (str): The id of the rule to modify.

            body (dict): Please see: https://auth0.com/docs/api/v2#!/Rules/patch_rules_by_id
        """
        return self.client.patch(self._url(id), data=body)
