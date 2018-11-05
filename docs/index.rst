.. Auth0 - Python documentation master file, created by
   sphinx-quickstart on Sat Nov 28 10:38:36 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Auth0 - Python's documentation!
==========================================

==============
What is Auth0?
==============

Auth0 helps you to:

* Add authentication with `multiple authentication sources <https://docs.auth0.com/identityproviders>`_,
  either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others**,
  or enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional `username/password databases <https://docs.auth0.com/mysql-connection-tutorial>`_.
* Add support for `linking different user accounts <https://docs.auth0.com/link-accounts>`_ with the same user.
* Support for generating signed `Json Web Tokens <https://docs.auth0.com/jwt>`_ to call your APIs and **flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through `JavaScript rules <https://docs.auth0.com/rules>`_.

===========================
Create a free Auth0 Account
===========================

1. Go to `Auth0`_ and click Sign Up.
2. Use Google, GitHub or Microsoft Account to login.

===============
Issue Reporting
===============

If you have found a bug or if you have a feature request, please report them at this repository issues section.
Please do not report security vulnerabilities on the public GitHub issue tracker.
The `Responsible Disclosure Program <https://auth0.com/whitehat>`_ details the procedure for disclosing security issues.

============
Installation
============

You can install the auth0 python SDK issuing the following command.

.. code-block:: shell

    pip install auth0-python

====================
Management SDK Usage
====================

To use the management library you will need to instantiate an Auth0 object with a domain and a token.


.. code-block:: python

    from auth0.v2.management import Auth0

    domain = 'myaccount.auth0.com'
    token = '{A_JWT_TOKEN}' # You can generate one of these by using the
                            # token generator at: https://auth0.com/docs/api/v2

    auth0 = Auth0('myuser.auth0.com', token)

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

That's it! using the ``get`` method of the connections endpoint we can verify
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

All endpoints follow a similar structure to the ``connections`` one, and try to follow as
closely as possible the `API documentation <https://auth0.com/docs/api/v2>`_.

========================
Authentication SDK Usage
========================

The Authentication SDK is divided into components mimicking the structure of the
`API's documentation <https://auth0.com/docs/auth-api>`_.
For example:

.. code-block:: python

    from auth0.v2.authentication import Social

    social = Social('myaccount.auth0.com')

    s.login(client_id='...', acces_token='...', connection='facebook')


Contents:
_________

Management API.

.. toctree::
   :maxdepth: 2

   blacklists
   clients
   connections
   device_credentials
   emails
   jobs
   rules
   stats
   tenants
   tickets
   users

Authentication API.

.. toctree::
   :maxdepth: 2

   auth_users
   database
   delegated
   enterprise
   link
   passwordless
   social

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Auth0: https://auth0.com
