# V4 Migration Guide

Guide to migrating from `3.x` to `4.x`

- [Python <3.6 is no longer supported](#python-36-is-no-longer-supported)
- [Client ID and Client Secret are now specified in the constructor for Authentication Clients](#client-id-and-client-secret-are-now-specified-in-the-constructor-for-authentication-clients)
- [AuthorizeClient and Logout have been removed](#authorizeclient-and-logout-have-been-removed)

## Python <3.6 is no longer supported

Python 3.5 and Python 2 are EOL and are no longer supported. 

## Client ID and Client Secret are now specified in the constructor for Authentication Clients

### Before

```py
from auth0.v3.authentication import GetToken

get_token = GetToken('myaccount.auth0.com')

get_token.client_credentials('my-client-id', 'my-client-secret', 'my-api')
```

### After

```py
from auth0.v3.authentication import GetToken

# `client_secret` is optional (you can now use `client_assertion_signing_key` as an alternative) 
get_token = GetToken('myaccount.auth0.com', 'my-client-id', client_secret='my-client-secret')

get_token.client_credentials('my-api')
```

## AuthorizeClient and Logout have been removed

The authorize and logout requests need to be done in a user agent, so it didn't make sense to include them in a REST client.