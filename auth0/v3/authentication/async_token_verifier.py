"""Token Verifier module"""
from .. import TokenValidationError
from ..rest_async import AsyncRestClient
from .token_verifier import AsymmetricSignatureVerifier, JwksFetcher


class AsyncAsymmetricSignatureVerifier(AsymmetricSignatureVerifier):
    """Verifier for RSA signatures, which rely on public key certificates.

    Args:
        jwks_url (str): The url where the JWK set is located.
        algorithm (str, optional): The expected signing algorithm. Defaults to "RS256".
    """

    def __init__(self, jwks_url, algorithm="RS256"):
        super(AsyncAsymmetricSignatureVerifier, self).__init__(jwks_url, algorithm)
        self._fetcher_async = AsyncJwksFetcher(jwks_url)

    async def _fetch_key_async(self, key_id=None):
        return await self._fetcher.get_key(key_id)

    def verify_signature_async(self, token):
        """Verifies the signature of the given JSON web token.

        Args:
            token (str): The JWT to get its signature verified.

        Raises:
            TokenValidationError: if the token cannot be decoded, the algorithm is invalid
            or the token's signature doesn't match the calculated one.
        """
        kid = self._get_kid(token)
        secret_or_certificate = self._fetch_key(key_id=kid)

        return self._decode_jwt(token, secret_or_certificate)


class AsyncJwksFetcher(JwksFetcher):
    """Class that fetches and holds a JSON web key set.
    This class makes use of an in-memory cache. For it to work properly, define this instance once and re-use it.

    Args:
        jwks_url (str): The url where the JWK set is located.
        cache_ttl (str, optional): The lifetime of the JWK set cache in seconds. Defaults to 600 seconds.
    """

    def __init__(self, *args, **kwargs):
        super(AsyncJwksFetcher, self).__init__(*args, **kwargs)
        self._async_client = AsyncRestClient(None)

    async def _fetch_jwks_async(self, force=False):
        """Attempts to obtain the JWK set from the cache, as long as it's still valid.
        When not, it will perform a network request to the jwks_url to obtain a fresh result
        and update the cache value with it.

        Args:
            force (bool, optional): whether to ignore the cache and force a network request or not. Defaults to False.
        """
        if force or self._cache_expired():
            self._cache_value = {}
            try:
                jwks = await self._async_client.get(self._jwks_url)
                self._cache_jwks(jwks)
            except:  # noqa: E722
                return self._cache_value
            return self._cache_value

        self._cache_is_fresh = False
        return self._cache_value

    async def get_key_async(self, key_id):
        """Obtains the JWK associated with the given key id.

        Args:
            key_id (str): The id of the key to fetch.

        Returns:
            the JWK associated with the given key id.

        Raises:
            TokenValidationError: when a key with that id cannot be found
        """
        keys = await self._fetch_jwks_async()

        if keys and key_id in keys:
            return keys[key_id]

        if not self._cache_is_fresh:
            keys = await self._fetch_jwks_async(force=True)
            if keys and key_id in keys:
                return keys[key_id]
        raise TokenValidationError(
            'RSA Public Key with ID "{}" was not found.'.format(key_id)
        )
