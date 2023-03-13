# Examples using auth0-python

- [Authentication SDK](#authentication-sdk)
  - [ID token validation](#id-token-validation)
  - [Authenticating with a application configured to use `private_key_jwt` token endpoint auth method](#authenticating-with-a-application-configured-to-use-private-key-jwt-token-endpoint-auth-method)
- [Management SDK](#management-sdk)
  - [Connections](#connections)
- [Error handling](#error-handling)
- [Asynchronous environments](#asynchronous-environments)

## Authentication SDK

### ID token validation

Upon successful authentication, the credentials received may include an `id_token`, if the authentication request contained the `openid` scope. The `id_token` contains information associated with the authenticated user. You can read more about ID tokens [here](https://auth0.com/docs/tokens/concepts/id-tokens).

Before you access its contents, you must verify that the ID token has not been tampered with and that it is meant for your application to consume. The `TokenVerifier` class can be used to perform this verification.

To create a `TokenVerifier`, the following arguments are required:

- A `SignatureVerifier` instance, which is responsible for verifying the token's algorithm name and signature.
- The expected issuer value, which typically matches the Auth0 domain prefixed with `https://` and suffixed with `/`.
- The expected audience value, which typically matches the Auth0 application client ID.

The type of `SignatureVerifier` used depends upon the signing algorithm used by your Auth0 application. You can view this value in your application settings under `Advanced settings | OAuth | JsonWebToken Signature Algorithm`. Auth0 recommends using the RS256 asymmetric signing algorithm. You can read more about signing algorithms [here](https://auth0.com/docs/tokens/signing-algorithms).

For asymmetric algorithms like RS256, use the `AsymmetricSignatureVerifier` class, passing
the public URL where the certificates for the public keys can be found. This will typically be your Auth0 domain with the `/.well-known/jwks.json` path appended to it. For example, `https://your-domain.auth0.com/.well-known/jwks.json`.

For symmetric algorithms like HS256, use the `SymmetricSignatureVerifier` class, passing the value of the client secret of your Auth0 application.

The following example demonstrates the verification of an ID token signed with the RS256 signing algorithm:

```python
from auth0.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier

domain = 'myaccount.auth0.com'
client_id = 'exampleid'

# After authenticating
id_token = auth_result['id_token']

jwks_url = 'https://{}/.well-known/jwks.json'.format(domain)
issuer = 'https://{}/'.format(domain)

sv = AsymmetricSignatureVerifier(jwks_url)  # Reusable instance
tv = TokenVerifier(signature_verifier=sv, issuer=issuer, audience=client_id)
tv.verify(id_token)
```

If the token verification fails, a `TokenValidationError` will be raised. In that scenario, the ID token should be deemed invalid and its contents should not be trusted.

### Authenticating with a application configured to use `private_key_jwt` token endpoint auth method

```python
from auth0.authentication import GetToken

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAwfUb0nUC0aKB3WiytFhnCIg455BYC+dR3MUGadWpIg7S6lbi
...
2tjIvH4GN9ZkIGwzxIOP61wkUGwGaIzacOTIWOvqRI0OaYr9U18Ep1trvgGR
-----END RSA PRIVATE KEY-----
"""

get_token = GetToken(
    "my-domain.us.auth0.com",
    "my-client-id",
    client_assertion_signing_key=private_key,
)
token = get_token.client_credentials(
    "https://my-domain.us.auth0.com/api/v2/"
)
```

## Management SDK

### Connections

Let's see how we can use this to get all available connections.
(this action requires the token to have the following scope: `read:connections`)

```python
auth0.connections.all()
```

Which will yield a list of connections similar to this:

```python
[
    {
        'enabled_clients': [u'rOsnWgtw23nje2QCDuDJNVpxlsCylSLE'],
        'id': u'con_ErZf9LpXQDE0cNBr',
        'name': u'Amazon-Connection',
        'options': {u'profile': True, u'scope': [u'profile']},
        'strategy': u'amazon'
    },
    {
        'enabled_clients': [u'rOsnWgtw23nje2QCDuDJNVpxlsCylSLE'],
        'id': u'con_i8qF5DPiZ3FdadwJ',
        'name': u'Username-Password-Authentication',
        'options': {u'brute_force_protection': True},
        'strategy': u'auth0'
    }
]
```

Modifying an existing connection is equally as easy. Let's change the name
of connection `'con_ErZf9LpXQDE0cNBr'`.
(The token will need scope: `update:connections` to make this one work)

```python
auth0.connections.update('con_ErZf9LpXQDE0cNBr', {'name': 'MyNewName'})
```

That's it! Using the `get` method of the connections endpoint we can verify
that the rename actually happened.

```python
modified_connection = auth0.connections.get('con_ErZf9LpXQDE0cNBr')
```

Which returns something like this

```python
{
    'enabled_clients': [u'rOsnWgtw23nje2QCDuDJNVpxlsCylSLE'],
    'id': u'con_ErZf9LpXQDE0cNBr',
    'name': u'MyNewName',
    'options': {u'profile': True, u'scope': [u'profile']},
    'strategy': u'amazon'
}
```
Success!

All endpoints follow a similar structure to `connections`, and try to follow as
closely as possible the [API documentation](https://auth0.com/docs/api/v2).

## Error handling

When consuming methods from the API clients, the requests could fail for a number of reasons:
- Invalid data sent as part of the request: An `Auth0Error` is raised with the error code and description.
- Global or Client Rate Limit reached: A `RateLimitError` is raised and the time at which the limit
resets is exposed in the `reset_at` property. When the header is unset, this value will be `-1`.
- Network timeouts: Adjustable by passing a `timeout` argument to the client. See the [rate limit docs](https://auth0.com/docs/policies/rate-limits) for details.

## Asynchronous environments

This SDK provides async methods built on top of [asyncio](https://docs.python.org/3/library/asyncio.html). To make them available you must have the [aiohttp](https://docs.aiohttp.org/en/stable/) module installed.

Then additional methods with the `_async` suffix will be added to modules created by the `management.Auth0` class or to classes that are passed to the `asyncify` method. For example:

```python
import asyncio
import aiohttp
from auth0.asyncify import asyncify
from auth0.management import Auth0, Users, Connections
from auth0.authentication import Users as AuthUsers

auth0 = Auth0('domain', 'mgmt_api_token')


async def main():
    # users = auth0.users.all() <= sync
    users = await auth0.users.all_async()  # <= async

    # To share a session amongst multiple calls to the same service
    async with auth0.users as users:
        data = await users.get_async(id)
        users.update_async(id, data)

    # To share a session amongst multiple calls to multiple services
    async with Auth0('domain', 'mgmt_api_token') as auth0:
        user = await auth0.users.get_async(user_id)
        connection = await auth0.connections.get_async(connection_id)

    # Use asyncify directly on services
    Users = asyncify(Users)
    Connections = asyncify(Connections)
    users = Users(domain, mgmt_api_token)
    connections = Connections(domain, mgmt_api_token)

    # Create a session and share it among the services
    session = aiohttp.ClientSession()
    users.set_session(session)
    connections.set_session(session)
    u = await auth0.users.all_async()
    c = await auth0.connections.all_async()
    session.close()

    # Use auth api
    U = asyncify(AuthUsers)
    u = U(domain=domain)
    await u.userinfo_async(access_token)


asyncio.run(main())
```
