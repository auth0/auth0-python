import requests


class Enterprise(object):

    def __init__(self, domain):
        self.domain = domain

    def saml_login(self, client_id, connection):
        """
        """

        return requests.get(
            'https://%s/samlp/%s' % (self.domain, client_id),
            params={'connection': connection}
        )

    def saml_metadata(self,
