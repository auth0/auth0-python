from .base import AuthenticationBase


class Enterprise(AuthenticationBase):

    def __init__(self, domain):
        self.domain = domain

    def saml_metadata(self, client_id):
        return self.get(url='https://%s/samlp/metadata/%s' % (self.domain,
                                                              client_id))

    def wsfed_metadata(self):
        url = 'https://%s/wsfed/FederationMetadata' \
              '/2007-06/FederationMetadata.xml'

        return self.get(url=url % self.domain)
