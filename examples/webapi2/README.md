##auth0-py

Example of integrating Auth0 with a Python Web App.

## Install

### Getting virtualenv

Install virtualenv (this step can be done using `easy_install` too):

```sh
pip install virtualenv
```

Create an environment:

```sh
virtualenv auth0env
```

### Installing dependencies

Activate your virtualenv environment:

```sh
source auth0env/bin/activate
```

Install dependencies:

```sh
pip install webob webapp2 paste
```

## Usage

Run the sample app:
```sh
python sample.py
```

## What is Auth0?

Auth0 helps you to:

* Add authentication with [multiple authentication sources](https://docs.auth0.com/identityproviders), either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, amont others**, or enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional **[username/password databases](https://docs.auth0.com/mysql-connection-tutorial)**.
* Add support for **[linking different user accounts](https://docs.auth0.com/link-accounts)** with the same user.
* Support for generating signed [Json Web Tokens](https://docs.auth0.com/jwt) to call your APIs and **flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through [JavaScript rules](https://docs.auth0.com/rules).

## Create a free account in Auth0

1. Go to [Auth0](https://auth0.com) and click Sign Up.
2. Use Google, GitHub or Microsoft Account to login.

