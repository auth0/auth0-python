from .base import AuthenticationBase


class Enterprise(AuthenticationBase):

    """Enterprise endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def __init__(self, domain):
        self.domain = domain

    def saml_metadata(self, client_id):
        """Get SAML2.0 Metadata.

        Args:
            client_id (str): Id of the client to get the SAML metadata for.
        """

        return self.get(url='https://%s/samlp/metadata/%s' % (self.domain,
                                                              client_id))

    def wsfed_metadata(self):
        """Returns the WS-Federation Metadata.
        """

        url = 'https://%s/wsfed/FederationMetadata' \
              '/2007-06/FederationMetadata.xml'

        return self.get(url=url % self.domain)
