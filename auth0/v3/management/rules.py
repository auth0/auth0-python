from .rest import RestClient


class Rules(object):
    """Rules endpoint implementation.

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
        url = '{}://{}/api/v2/rules'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all(self, stage='login_success', enabled=True, fields=None,
            include_fields=True, page=None, per_page=None, include_totals=False):
        """Retrieves a list of all rules.

        Args:
            stage (str, optional):  Retrieves rules that match the execution stage.
                Defaults to login_success.

            enabled (bool, optional): If provided, retrieves rules that match
                the value, otherwise all rules are retrieved.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result. Leave empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise. Defaults to True.

            page (int, optional): The result's page number (zero based). When not set,
                the default value is up to the server.

            per_page (int, optional): The amount of entries per page. When not set,
                the default value is up to the server.

            include_totals (bool, optional): True if the query summary is
                to be included in the result, False otherwise. Defaults to False.

        See: https://auth0.com/docs/api/management/v2#!/Rules/get_rules
        """

        params = {
            'stage': stage,
            'fields': fields and ','.join(fields) or None,
            'include_fields': str(include_fields).lower(),
            'page': page,
            'per_page': per_page,
            'include_totals': str(include_totals).lower()
        }

        # since the default is True, this is here to disable the filter
        if enabled is not None:
            params['enabled'] = str(enabled).lower()

        return self.client.get(self._url(), params=params)

    def create(self, body):
        """Creates a new rule.

        Args:
            body (dict): Attributes for the newly created rule.

        See: https://auth0.com/docs/api/v2#!/Rules/post_rules
        """
        return self.client.post(self._url(), data=body)

    def get(self, id, fields=None, include_fields=True):
        """Retrieves a rule by its ID.

        Args:
            id (str): The id of the rule to retrieve.

            fields (list, optional): A list of fields to include or exclude
                (depending on include_fields) from the result. Leave empty to
                retrieve all fields.

            include_fields (bool, optional): True if the fields specified are
                to be included in the result, False otherwise. Defaults to True.

        See: https://auth0.com/docs/api/management/v2#!/Rules/get_rules_by_id
        """
        params = {'fields': fields and ','.join(fields) or None,
                  'include_fields': str(include_fields).lower()}
        return self.client.get(self._url(id), params=params)

    def delete(self, id):
        """Delete a rule.

        Args:
            id (str): The id of the rule to delete.

        See: https://auth0.com/docs/api/management/v2#!/Rules/delete_rules_by_id
        """
        return self.client.delete(self._url(id))

    def update(self, id, body):
        """Update an existing rule

        Args:
            id (str): The id of the rule to modify.

            body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/v2#!/Rules/patch_rules_by_id
        """
        return self.client.patch(self._url(id), data=body)
