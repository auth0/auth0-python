# Examples using auth0-python

- [Authentication SDK](#authentication-sdk)
  - [ID token validation](#id-token-validation)
  - [Organizations](#organizations)
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
from auth0.v3.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier

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



### Organizations

[Organizations](https://auth0.com/docs/organizations) is a set of features that provide better support for developers who build and maintain SaaS and Business-to-Business (B2B) applications.

Note that Organizations is currently only available to customers on our Enterprise and Startup subscription plans.


#### Log in to an organization

Log in to an organization by specifying the ``organization`` property when calling ``authorize()``:

```python
from auth0.v3.authentication.authorize_client import AuthorizeClient

client = AuthorizeClient('my.domain.com')

client.authorize(client_id='client_id',
            redirect_uri='http://localhost',
            organization="org_abc")
```

When logging into an organization, it is important to ensure the `org_id` claim of the ID Token matches the expected organization value. The `TokenVerifier` can be be used to ensure the ID Token contains the expected `org_id` claim value:

```python
from auth0.v3.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier

domain = 'myaccount.auth0.com'
client_id = 'exampleid'

# After authenticating
id_token = auth_result['id_token']

jwks_url = 'https://{}/.well-known/jwks.json'.format(domain)
issuer = 'https://{}/'.format(domain)

sv = AsymmetricSignatureVerifier(jwks_url)  # Reusable instance
tv = TokenVerifier(signature_verifier=sv, issuer=issuer, audience=client_id)

# pass the expected organization the user logged in to:
tv.verify(id_token, organization='org_abc')

```

#### Accept user invitations

Accept a user invitation by specifying the `invitation` property when calling `authorize()`. Note that you must also specify the ``organization`` if providing an ``invitation``.
The ID of the invitation and organization are available as query parameters on the invitation URL, e.g., ``https://your-domain.auth0.com/login?invitation=invitation_id&organization=org_id&organization_name=org_name``

```python
from auth0.v3.authentication.authorize_client import AuthorizeClient

client = AuthorizeClient('my.domain.com')

client.authorize(client_id='client_id',
        redirect_uri='http://localhost',
        organization='org_abc',
        invitation="invitation_123")
```

#### Authorizing users from an Organization

If an `org_id` claim is present in the Access Token, then the claim should be validated by the API to ensure that the value received is expected or known.

In particular:

- The issuer (`iss`) claim should be checked to ensure the token was issued by Auth0
- The organization ID (`org_id`) claim should be checked to ensure it is a value that is already known to the application. This could be validated against a known list of organization IDs, or perhaps checked in conjunction with the current request URL. e.g. the sub-domain may hint at what organization should be used to validate the Access Token.

Normally, validating the issuer would be enough to ensure that the token was issued by Auth0. In the case of organizations, additional checks should be made so that the organization within an Auth0 tenant is expected.

If the claim cannot be validated, then the application should deem the token invalid.

The snippet below attempts to illustrate how this verification could look like using the external [PyJWT](https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa) library. This dependency will take care of pulling the RS256 Public Key that was used by the server to sign the Access Token. It will also validate its signature, expiration, and the audience value. After the basic verification, get the `org_id` claim and check it against the expected value. The code assumes your application is configured to sign tokens using the RS256 algorithm. Check the [Validate JSON Web Tokens](https://auth0.com/docs/tokens/json-web-tokens/validate-json-web-tokens) article to learn more about this verification.

```python
import jwt  # PyJWT
from jwt import PyJWKClient

access_token = # access token from the request
url = 'https://{YOUR AUTH0 DOMAIN}/.well-known/jwks.json'
jwks_client = PyJWKClient(url)
signing_key = jwks_client.get_signing_key_from_jwt(access_token)
data = jwt.decode(
    access_token,
    signing_key.key,
    algorithms=['RS256'],
    audience='{YOUR API AUDIENCE}'
)

organization = # expected organization ID
if data['org_id'] != organization:
    raise Exception('Organization (org_id) claim mismatch')

# if this line is reached, validation is successful
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

### Error handling

When consuming methods from the API clients, the requests could fail for a number of reasons:
- Invalid data sent as part of the request: An `Auth0Error` is raised with the error code and description.
- Global or Client Rate Limit reached: A `RateLimitError` is raised and the time at which the limit
resets is exposed in the `reset_at` property. When the header is unset, this value will be `-1`.
- Network timeouts: Adjustable by passing a `timeout` argument to the client. See the [rate limit docs](https://auth0.com/docs/policies/rate-limits) for details.

### Asynchronous environments

This SDK provides async methods built on top of [asyncio](https://docs.python.org/3/library/asyncio.html). To make them available you must have Python >=3.6 and the [aiohttp](https://docs.aiohttp.org/en/stable/) module installed.

Then additional methods with the `_async` suffix will be added to modules created by the `management.Auth0` class or to classes that are passed to the `asyncify` method. For example:

```python
import asyncio
import aiohttp
from auth0.v3.asyncify import asyncify
from auth0.v3.management import Auth0, Users, Connections
from auth0.v3.authentication import Users as AuthUsers

auth0 = Auth0('domain', 'mgmt_api_token')

async def main():
    # users = auth0.users.all() <= sync
    users = await auth0.users.all_async() # <= async

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