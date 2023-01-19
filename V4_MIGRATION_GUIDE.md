# V4 Migration Guide

Guide to migrating from `3.x` to `4.x`

- [Python <3.7 is no longer supported](#python-37-is-no-longer-supported)
- [The `v3` subfolder has been removed](#the-v3-subfolder-has-been-removed)
- [Client ID and client secret are now specified in the constructor for authentication clients](#client-id-and-client-secret-are-now-specified-in-the-constructor-for-authentication-clients)
- [AuthorizeClient and Logout have been removed](#authorizeclient-and-logout-have-been-removed)
- [Methods that call deprecated endpoints have been removed](#methods-that-call-deprecated-endpoints-have-been-removed)

## Python <3.7 is no longer supported

Python <=3.6 and Python 2 are EOL and are no longer supported. 

Also note the new Python [Support Policy](https://github.com/auth0/auth0-python#support-policy)

## The `v3` subfolder has been removed

Versioning the import paths was not necessary and made major upgrades unnecessarily complex, so this has been removed and all files have been moved up a directory.

### Before

```python
from auth0.v3.management import Auth0

auth0 = Auth0(domain, mgmt_api_token)
```

### After

```python
from auth0.management import Auth0

auth0 = Auth0(domain, mgmt_api_token)
```

## Client ID and client secret are now specified in the constructor for authentication clients

### Before

```py
from auth0.authentication import GetToken

get_token = GetToken('my-domain.us.auth0.com')

get_token.client_credentials('my-client-id', 'my-client-secret', 'my-api')
```

### After

```py
from auth0.authentication import GetToken

# `client_secret` is optional (you can now use `client_assertion_signing_key` as an alternative) 
get_token = GetToken('my-domain.us.auth0.com', 'my-client-id', client_secret='my-client-secret')

get_token.client_credentials('my-api')
```

## AuthorizeClient and Logout have been removed

The authorize and logout requests need to be done in a user agent, so it didn't make sense to include them in a REST client.

## Methods that call deprecated endpoints have been removed

The following methods have been removed:

### Authentication

- `database.login` - Use `get_token.login`
- `passwordless.sms_login` - Use `get_token.passwordless_login`
- `users.tokeninfo` - `users.userinfo`

### Management

- `users.delete_all_users` - Use `users.delete`
- `jobs.get_results` - Use `jobs.get`