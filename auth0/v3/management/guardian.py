from .rest import RestClient


class Guardian(object):
    """Auth0 guardian endpoints

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
        url = '{}://{}/api/v2/guardian'.format(self.protocol, self.domain)
        if id is not None:
            return '{}/{}'.format(url, id)
        return url

    def all_factors(self):
        """Retrieves all factors. Useful to check factor enablement and
             trial status.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/get_factors                 
        """

        return self.client.get(self._url('factors'))

    def update_factor(self, name, body):
        """Update Guardian factor.
        Useful to enable / disable factor.

        Args:
            name (str): Either push-notification or sms.

            body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/put_factors_by_name
        """
        url = self._url('factors/{}'.format(name))
        return self.client.put(url, data=body)

    def update_templates(self, body):
        """Update enrollment and verification SMS templates.

        Useful to send custom messages on sms enrollment and verification.

        Args:
            body (dict): Attributes to modify.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/put_templates
        """

        return self.client.put(self._url('factors/sms/templates'), data=body)

    def get_templates(self):
        """Get enrollment and verification templates.

        Retrieve both templates. Useful to check if a different template than
            default was set.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/get_templates
        """

        return self.client.get(self._url('factors/sms/templates'))

    def get_enrollment(self, id):
        """Retrieves an enrollment.
        Useful to check its type and related metadata.

        Args:
           id (str): The id of the device account to update.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/get_enrollments_by_id
        """
        url = self._url('enrollments/{}'.format(id))
        return self.client.get(url)

    def delete_enrollment(self, id):
        """Deletes an enrollment.

        Useful when you want to force re-enroll.

        Args:
           id (str): The id of the device account to update.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/delete_enrollments_by_id
        """
        url = self._url('enrollments/{}'.format(id))
        return self.client.delete(url)

    def create_enrollment_ticket(self, body):
        """Creates an enrollment ticket for user_id

        A useful way to send an email to a user, with a link that lead to
            start the enrollment process.

        Args:
            body (dict): Details of the user to send the ticket to.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/post_ticket
        """
        return self.client.post(self._url('enrollments/ticket'), data=body)

    def get_factor_providers(self, factor_name, name):
        """Get Guardian SNS or SMS factor providers.

        Returns provider configuration.

        Args:
           factor_name (str): Either push-notification or sms.

           name (str): Name of the provider.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/get_sns
             https://auth0.com/docs/api/management/v2#!/Guardian/get_twilio
        """
        url = self._url('factors/{}/providers/{}'.format(factor_name, name))
        return self.client.get(url)

    def update_factor_providers(self, factor_name, name, body):
        """Get Guardian factor providers.

        Returns provider configuration.

        Args:
           factor_name (str): Either push-notification or sms.

           name (str): Name of the provider.

           body (dict): Details of the factor provider.

        See: https://auth0.com/docs/api/management/v2#!/Guardian/put_twilio
        """
        url = self._url('factors/{}/providers/{}'.format(factor_name, name))
        return self.client.put(url, data=body)
