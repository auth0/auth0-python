**************
Auth0 - Python
**************

|pypi| |build| |coverage| |license|

In this repository, you'll find all the information about integrating Auth0 with Python.


==============
What is Auth0?
==============

Auth0 helps you to:

* Add authentication with `multiple authentication sources <https://auth0.com/docs/identityproviders>`_,
  either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others**,
  or enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional `username/password databases <https://auth0.com/docs/connections/database/mysql>`_.
* Add support for `linking different user accounts <https://auth0.com/docs/link-accounts>`_ with the same user.
* Support for generating signed `JSON Web Tokens <https://auth0.com/docs/jwt>`_ to call your APIs and **flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through `JavaScript rules <https://auth0.com/docs/rules>`_.


===========================
Create a free Auth0 Account
===========================

1. Go to `Auth0`_ and click Sign Up.
2. Use Google, GitHub or Microsoft Account to log in.

============
Installation
============

You can install the auth0 Python SDK using the following command.

.. code-block::

    pip install auth0-python

For python3, use the following command

.. code-block::
    
    pip3 install auth0-python

Python 3.2 and 3.3 have reached `EOL <https://en.wikipedia.org/wiki/CPython#Version_history>`_ and support will be removed in the near future.

====================
Management SDK Usage
====================

To use the management library you will need to instantiate an Auth0 object with a domain and a `Management API v2 token <https://auth0.com/docs/api/management/v2/tokens>`_. Please note that these token last 24 hours, so if you need it constantly you should ask for it programmatically using the client credentials grant with a `non interactive client <https://auth0.com/docs/api/management/v2/tokens#1-create-and-authorize-a-client>`_ authorized to access the API. For example:

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
closely as possible the `API documentation <https://auth0.com/docs/api/v2>`_.

========================
Authentication SDK Usage
========================

The Authentication SDK is divided into components mimicking the structure of the
`API's documentation <https://auth0.com/docs/auth-api>`_.
For example:

.. code-block:: python

    from auth0.v3.authentication import Social

    social = Social('myaccount.auth0.com')

    s.login(client_id='...', access_token='...', connection='facebook')

Available Management Endpoints
==============================

- Blacklists() ( ``Auth0().blacklists`` )
- Clients() ( ``Auth0().clients`` )
- ClientGrants() ( ``Auth0().client_grants`` )
- Connections() ( ``Auth0().connections`` )
- DeviceCredentials() ( ``Auth0().device_credentials`` )
- Emails() ( ``Auth0().emails`` )
- EmailTemplates() ( ``Auth0().email_templates`` )
- Guardian() ( ``Auth0().guardian`` )
- Jobs() ( ``Auth0().jobs`` )
- Logs() ( ``Auth0().logs`` )
- ResourceServers() (``Auth0().resource_servers`` )
- Rules() ( ``Auth0().rules`` )
- Stats() ( ``Auth0().stats`` )
- Tenants() ( ``Auth0().tenants`` )
- Tickets() ( ``Auth0().tickets`` )
- UserBlocks() (``Auth0().user_blocks`` )
- Users() ( ``Auth0().users`` )
- UsersByEmail() ( ``Auth0().users_by_email`` )

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
    

==========
Change Log
==========

Please see `CHANGELOG.md <https://github.com/auth0/auth0-python/blob/master/CHANGELOG.md>`_.

===============
Issue Reporting
===============

If you have found a bug or if you have a feature request, please report them at this repository issues section.
Please do not report security vulnerabilities on the public GitHub issue tracker.
The `Responsible Disclosure Program <https://auth0.com/whitehat>`_ details the procedure for disclosing security issues.

======
Author
======

`Auth0`_

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
