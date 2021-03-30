**************
Auth0 - Python
**************

|pypi| |build| |coverage| |license|

In this repository, you'll find all the information about integrating Auth0 with Python.

============
Installation
============

You can install the auth0 Python SDK using the following command.

.. code-block:: python

    pip install auth0-python

For python3, use the following command

.. code-block:: python
    
    pip3 install auth0-python

Python 3.2 and 3.3 have reached `EOL <https://en.wikipedia.org/wiki/CPython#Version_history>`__ and support will be removed in the near future.

========================
Authentication SDK Usage
========================

The Authentication SDK is organized into components that mirror the structure of the
`API documentation <https://auth0.com/docs/auth-api>`__.
For example:

.. code-block:: python

    from auth0.v3.authentication import Social

    social = Social('myaccount.auth0.com')

    social.login(client_id='...', access_token='...', connection='facebook')


If you need to sign up a user using their email and password, you can use the Database object.

.. code-block:: python

    from auth0.v3.authentication import Database

    database = Database('myaccount.auth0.com'')

    database.signup(client_id='...', email='user@domain.com', password='secr3t', connection='Username-Password-Authentication')


If you need to authenticate a user using their email and password, you can use the ``GetToken`` object, which enables making requests to the ``/oauth/token`` endpoint.

.. code-block:: python

    from auth0.v3.authentication import GetToken

    token = GetToken('myaccount.auth0.com')

    token.login(client_id='...', client_secret='...', username='user@domain.com', password='secr3t', realm='Username-Password-Authentication')


===================
ID Token validation
===================

Upon successful authentication, the credentials received may include an ``id_token``, if the authentication request contained the ``openid`` scope. The ``id_token`` contains information associated with the authenticated user. You can read more about ID tokens `here <https://auth0.com/docs/tokens/concepts/id-tokens>`__.

Before you access its contents, you must verify that the ID token has not been tampered with and that it is meant for your application to consume. The ``TokenVerifier`` class can be used to perform this verification.

To create a ``TokenVerifier``, the following arguments are required:

- A ``SignatureVerifier`` instance, which is responsible for verifying the token's algorithm name and signature.
- The expected issuer value, which typically matches the Auth0 domain prefixed with ``https://`` and suffixed with ``/``.
- The expected audience value, which typically matches the Auth0 application client ID.

The type of ``SignatureVerifier`` used depends upon the signing algorithm used by your Auth0 application. You can view this value in your application settings under ``Advanced settings | OAuth | JsonWebToken Signature Algorithm``. Auth0 recommends using the RS256 asymmetric signing algorithm. You can read more about signing algorithms `here <https://auth0.com/docs/tokens/signing-algorithms>`__.

For asymmetric algorithms like RS256, use the ``AsymmetricSignatureVerifier`` class, passing
the public URL where the certificates for the public keys can be found. This will typically be your Auth0 domain with the ``/.well-known/jwks.json`` path appended to it. For example, ``https://your-domain.auth0.com/.well-known/jwks.json``.

For symmetric algorithms like HS256, use the ``SymmetricSignatureVerifier`` class, passing the value of the client secret of your Auth0 application.

The following example demonstrates the verification of an ID token signed with the RS256 signing algorithm:

.. code-block:: python
    
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
    
If the token verification fails, a ``TokenValidationError`` will be raised. In that scenario, the ID token should be deemed invalid and its contents should not be trusted.

===========================
Organizations
===========================

`Organizations <https://auth0.com/docs/organizations>`__ is a set of features that provide better support for developers who build and maintain SaaS and Business-to-Business (B2B) applications.

Using Organizations, you can:
* Represent teams, business customers, partner companies, or any logical grouping of users that should have different ways of accessing your applications, as organizations.
* Manage their membership in a variety of ways, including user invitation.
* Configure branded, federated login flows for each organization.
* Implement role-based access control, such that users can have different roles when authenticating in the context of different organizations.
* Build administration capabilities into your products, using Organizations APIs, so that those businesses can manage their own organizations.

Note that Organizations is currently only available to customers on our Enterprise and Startup subscription plans.

-------------------------
Log in to an organization
-------------------------

Log in to an organization by specifying the ``organization`` property when calling ``authorize()``:

.. code-block:: python

    from auth0.v3.authentication.authorize_client import AuthorizeClient
    
    client = AuthorizeClient('my.domain.com')

    client.authorize(client_id='client_id',
                redirect_uri='http://localhost',
                organization="org_abc")

When logging into an organization, it is important to ensure the ``org_id`` claim of the ID Token matches the expected organization value. The ``TokenVerifier`` can be be used to ensure the ID Token contains the expected ``org_id`` claim value:

.. code-block:: python
    
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

-----------------------
Accept user invitations
-----------------------

Accept a user invitation by specifying the ``invitation`` property when calling ``authorize()``. Note that you must also specify the ``organization`` if providing an ``invitation``.
The ID of the invitation and organization are available as query parameters on the invitation URL, e.g., ``https://your-domain.auth0.com/login?invitation=invitation_id&organization=org_id&organization_name=org_name``

.. code-block:: python

    from auth0.v3.authentication.authorize_client import AuthorizeClient

    client = AuthorizeClient('my.domain.com')

    client.authorize(client_id='client_id',
            redirect_uri='http://localhost',
            organization='org_abc',
            invitation="invitation_123")

--------------------------------------
Authorizing users from an Organization
--------------------------------------

If an ``org_id`` claim is present in the Access Token, then the claim should be validated by the API to ensure that the value received is expected or known.

In particular:

- The issuer (``iss``) claim should be checked to ensure the token was issued by Auth0
- The organization ID (``org_id``) claim should be checked to ensure it is a value that is already known to the application. This could be validated against a known list of organization IDs, or perhaps checked in conjunction with the current request URL. e.g. the sub-domain may hint at what organization should be used to validate the Access Token.

Normally, validating the issuer would be enough to ensure that the token was issued by Auth0. In the case of organizations, additional checks should be made so that the organization within an Auth0 tenant is expected.

If the claim cannot be validated, then the application should deem the token invalid.

The snippet below attempts to illustrate how this verification could look like using the external `PyJWT <https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa>`__ library. This dependency will take care of pulling the RS256 Public Key that was used by the server to sign the Access Token. It will also validate its signature, expiration, and the audience value. After the basic verification, get the ``org_id`` claim and check it against the expected value. The code assumes your application is configured to sign tokens using the RS256 algorithm. Check the `Validate JSON Web Tokens <https://auth0.com/docs/tokens/json-web-tokens/validate-json-web-tokens>`__ article to learn more about this verification.

.. code-block:: python

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
  

====================
Management SDK Usage
====================

To use the management library you will need to instantiate an Auth0 object with a domain and a `Management API v2 token <https://auth0.com/docs/api/management/v2/tokens>`__. Please note that these token last 24 hours, so if you need it constantly you should ask for it programmatically using the client credentials grant with a `non interactive client <https://auth0.com/docs/api/management/v2/tokens#1-create-and-authorize-a-client>`__ authorized to access the API. For example:

.. code-block:: python

    from auth0.v3.authentication import GetToken

    domain = 'myaccount.auth0.com'
    non_interactive_client_id = 'exampleid'
    non_interactive_client_secret = 'examplesecret'

    get_token = GetToken(domain)
    token = get_token.client_credentials(non_interactive_client_id,
        non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
    mgmt_api_token = token['access_token']


Then use the token you've obtained as follows:

.. code-block:: python

    from auth0.v3.management import Auth0

    domain = 'myaccount.auth0.com'
    mgmt_api_token = 'MGMT_API_TOKEN'

    auth0 = Auth0(domain, mgmt_api_token)

The ``Auth0()`` object is now ready to take orders!
Let's see how we can use this to get all available connections.
(this action requires the token to have the following scope: ``read:connections``)

.. code-block:: python

    auth0.connections.all()

Which will yield a list of connections similar to this:

.. code-block:: python

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

Modifying an existing connection is equally as easy. Let's change the name
of connection ``'con_ErZf9LpXQDE0cNBr'``.
(The token will need scope: ``update:connections`` to make this one work)

.. code-block:: python

    auth0.connections.update('con_ErZf9LpXQDE0cNBr', {'name': 'MyNewName'})

That's it! Using the ``get`` method of the connections endpoint we can verify
that the rename actually happened.

.. code-block:: python

    modified_connection = auth0.connections.get('con_ErZf9LpXQDE0cNBr')

Which returns something like this

.. code-block:: python

    {
        'enabled_clients': [u'rOsnWgtw23nje2QCDuDJNVpxlsCylSLE'],
        'id': u'con_ErZf9LpXQDE0cNBr',
        'name': u'MyNewName',
        'options': {u'profile': True, u'scope': [u'profile']},
        'strategy': u'amazon'
    }

Success!

All endpoints follow a similar structure to ``connections``, and try to follow as
closely as possible the `API documentation <https://auth0.com/docs/api/v2>`__.

==============
Error Handling
==============

When consuming methods from the API clients, the requests could fail for a number of reasons:
- Invalid data sent as part of the request: An ``Auth0Error` is raised with the error code and description.
- Global or Client Rate Limit reached: A ``RateLimitError`` is raised and the time at which the limit
resets is exposed in the ``reset_at`` property. When the header is unset, this value will be ``-1``.
- Network timeouts: Adjustable by passing a ``timeout`` argument to the client. See the `rate limit docs <https://auth0.com/docs/policies/rate-limits>`__ for details.

==================================
Available Authentication Endpoints
==================================

- Users ( ``authentication.Users`` )
- Database ( ``authentication.Database`` )
- Delegated ( ``authentication.Delegated`` )
- Enterprise ( ``authentication.Enterprise`` )
- Passwordless ( ``authentication.Passwordless`` )
- Social ( ``authentication.Social`` )
- API Authorization - Get Token ( ``authentication.GetToken``)
- API Authorization - Authorization Code Grant (``authentication.AuthorizeClient``)

==============================
Available Management Endpoints
==============================

- Blacklists() ( ``Auth0().blacklists`` )
- Clients() ( ``Auth0().clients`` )
- ClientGrants() ( ``Auth0().client_grants`` )
- CustomDomains() ( ``Auth0().custom_domains`` )
- Connections() ( ``Auth0().connections`` )
- DeviceCredentials() ( ``Auth0().device_credentials`` )
- Emails() ( ``Auth0().emails`` )
- EmailTemplates() ( ``Auth0().email_templates`` )
- Grants() ( ``Auth0().grants`` )
- Guardian() ( ``Auth0().guardian`` )
- Jobs() ( ``Auth0().jobs`` )
- Logs() ( ``Auth0().logs`` )
- LogStreams() ( ``Auth0().log_streams`` )
- Organizations() ( ``Auth0().organizations`` )
- ResourceServers() (``Auth0().resource_servers`` )
- Roles() ( ``Auth0().roles`` )
- Rules() ( ``Auth0().rules`` )
- RulesConfigs() ( ``Auth0().rules_configs`` )
- Stats() ( ``Auth0().stats`` )
- Tenants() ( ``Auth0().tenants`` )
- Tickets() ( ``Auth0().tickets`` )
- UserBlocks() (``Auth0().user_blocks`` )
- Users() ( ``Auth0().users`` )
- UsersByEmail() ( ``Auth0().users_by_email`` )

==========
Change Log
==========

Please see `CHANGELOG.md <https://github.com/auth0/auth0-python/blob/master/CHANGELOG.md>`__.

===============
Issue Reporting
===============

If you have found a bug or if you have a feature request, please report them at this repository issues section.
Please do not report security vulnerabilities on the public GitHub issue tracker.
The `Responsible Disclosure Program <https://auth0.com/whitehat>`__ details the procedure for disclosing security issues.

==============
What is Auth0?
==============

Auth0 helps you to:

* Add authentication with `multiple authentication sources <https://auth0.com/docs/identityproviders>`__,
  either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others**,
  or enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional `username/password databases <https://auth0.com/docs/connections/database/mysql>`__.
* Add support for `linking different user accounts <https://auth0.com/docs/link-accounts>`__ with the same user.
* Support for generating signed `JSON Web Tokens <https://auth0.com/docs/jwt>`__ to call your APIs and **flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through `JavaScript rules <https://auth0.com/docs/rules>`__.

===========================
Create a free Auth0 Account
===========================

1. Go to `Auth0 <https://auth0.com/>`__ and click Sign Up.
2. Use Google, GitHub or Microsoft Account to log in.

=======
License
=======

This project is licensed under the MIT license. See the `LICENSE <https://github.com/auth0/auth0-python/blob/master/LICENSE>`_
file for more info.

.. _Auth0: https://auth0.com

.. |pypi| image:: https://img.shields.io/pypi/v/auth0-python.svg?style=flat-square&label=latest%20version
    :target: https://pypi.org/project/auth0-python/
    :alt: Latest version released on PyPI

.. |build| image:: https://img.shields.io/circleci/project/github/auth0/auth0-python.svg?style=flat-square&label=circleci
    :target: https://circleci.com/gh/auth0/auth0-python
    :alt: Build status

.. |coverage| image:: https://img.shields.io/codecov/c/github/auth0/auth0-python.svg?style=flat-square&label=codecov
    :target: https://codecov.io/gh/auth0/auth0-python
    :alt: Test coverage

.. |license| image:: https://img.shields.io/:license-mit-blue.svg?style=flat-square
    :target: https://opensource.org/licenses/MIT
    :alt: License
