import requests
from ...exceptions import JwkProviderError
from .leaky_bucket import Bucket

class JwkProvider(object):

    def get_jwk(key_id=None):
        """Obtains a JSON Web Key
        
        Args:
            key_id (str): The id of the key to obtain
        """
        raise NotImplementedError

class UrlJwkProvider(JwkProvider):

    def __init__(self, domain, bucket=Bucket()):
        self.url = "https://%s/.well-known/jwks.json" % (domain)
        self._jwks = None
        self._bucket = bucket

    def get_jwk(self, key_id=None):
        """Obtains a JSON Web Key
        
        Args:
            key_id (str): The id of the key to obtain. If omitted and the JWK set has only one element, that one is returned.
         
        Returns:
            A dict representing the JWK
        """
        key = None
        if self._jwks:
            # First look for a cached key
            key = self._find_key(key_id)
        if not key:
            # Then fetch a fresh JWK set and look for it there
            self._jwks = self._fetch_jwks()
            key = self._find_key(key_id)
        if key:
            return key
        raise JwkProviderError('There is no key in the set with key id %s' % (key_id))

    def _find_key(self, key_id=None):
        for key in self._jwks:
            if 'kid' in key and key['kid']==key_id:
                return key
        if not key_id and len(self._jwks)==1:
            return self._jwks[0]

    def _fetch_jwks(self):
        # Only if this provider is not rate limited the request can be performed
        if self._bucket.consume():
            return requests.get(self.url).json()['keys']
        raise JwkProviderError('Requests are rate-limited for another %d seconds' % (self._bucket.leaks_in()))