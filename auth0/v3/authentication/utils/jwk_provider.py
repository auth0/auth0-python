import requests
from ...exceptions import JwkProviderError

class JwkProvider(object):

    def get_jwk(key_id=None):
        """Obtains a JSON Web Key
        
        Args:
            key_id (str): The id of the key to obtain
        """
        raise NotImplementedError

class UrlJwkProvider(JwkProvider):

    def __init__(self, domain):
        self.url = "https://%s/.well-known/jwks.json" % (domain)
        self._jwks = None

    def get_jwk(self, key_id=None):
        """Obtains a JSON Web Key
        
        Args:
            key_id (str): The id of the key to obtain. If ommited and the JWK set has only one element, that one is returned.
         
        Returns:
            A dict representing the JWK
        """
        if not self._jwks:
            self._jwks = self._fetch_jwks()
            #TODO: See how to cache/save this result
            #FIXME: Add some rate-limiting bucket
        if not key_id and len(self._jwks)==1:
            return self._jwks[0]
        for key in self._jwks:
            if 'kid' in key and key['kid']==key_id:
                return key
        raise JwkProviderError('There is no key in the set with key id "{}"'.format(key_id))

    def _fetch_jwks(self):
        return requests.get(self.url).json()['keys']