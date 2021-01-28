from .base import AuthenticationBase


class Enterprise(AuthenticationBase):

    """Enterprise endpoints.

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def saml_metadata(self, client_id):
        """Get SAML2.0 Metadata.

        Args:
            client_id (str): Client Id of the application to get the SAML metadata for.
        """

        return self.get(url='{}://{}/samlp/metadata/{}'.format(self.protocol, self.domain, client_id))

    def wsfed_metadata(self):
        """Returns the WS-Federation Metadata.
        """

        url = '{}://{}/wsfed/FederationMetadata' \
              '/2007-06/FederationMetadata.xml'

        return self.get(url=url.format(self.protocol, self.domain))
