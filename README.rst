**************
Auth0 - Python
**************

|pypi| |unix_build| |windows_build| |coverage|

In this repository, you'll find all the information about integrating Auth0 with Python.

Check out the examples that we have in here in our examples folder. Each of them has a README on how to run them and on how to use them.


==============
What is Auth0?
==============

Auth0 helps you to:

* Add authentication with `multiple authentication sources <https://docs.auth0.com/identityproviders>`_,
  either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, amont others**,
  or enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional **[username/password databases](https://docs.auth0.com/mysql-connection-tutorial)**.
* Add support for **`linking different user accounts <https://docs.auth0.com/link-accounts>`_** with the same user.
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


======
Author
======

`Auth0`_

==========
Contribute
==========

Please see `CONTRIBUTING.rst <https://github.com/sophilabs/auth0-python/blob/v2/CONTRIBUTING.rst>`_.


==========
Change Log
==========

Please see `CHANGELOG.rst <https://github.com/sophilabs/auth0-python/blob/v2/CHANGELOG.rst>`_.


=======
License
=======

This project is licensed under the MIT license. See the `LICENSE.rst <https://github.com/sophilabs/auth0-python/blob/v2/LICENSE.rst>`_
file for more info.

.. _Auth0: https://auth0.com

.. |pypi| image:: https://img.shields.io/pypi/v/auth0.svg?style=flat-square&label=latest%20version
    :target: https://pypi.python.org/pypi/auth0
    :alt: Latest version released on PyPi

.. |coverage| image:: https://coveralls.io/repos/sophilabs/auth0-python/badge.svg?branch=v2&service=github
    :target: https://coveralls.io/github/sophilabs/auth0-python?branch=v2
    :alt: Test coverage

.. |build| image:: https://img.shields.io/travis/sophilabs/auth0-python/v2.svg?style=flat-square&label=build
    :target: http://travis-ci.org/sophilabs/auth0-python
    :alt: Build status of the v2 branch
