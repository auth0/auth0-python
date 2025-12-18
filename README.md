# Auth0 Python Library

![Auth0 SDK for Python](https://cdn.auth0.com/website/sdks/banners/auth0-python-banner.png)

![Release](https://img.shields.io/pypi/v/auth0-python)
[![Codecov](https://img.shields.io/codecov/c/github/auth0/auth0-python)](https://codecov.io/gh/auth0/auth0-python)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/auth0/auth0-python)
![Downloads](https://img.shields.io/pypi/dw/auth0-python)
[![License](https://img.shields.io/:license-MIT-blue.svg?style=flat)](https://opensource.org/licenses/MIT)
[![CircleCI](https://img.shields.io/circleci/build/github/auth0/auth0-python)](https://circleci.com/gh/auth0/auth0-python)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fauth0%2Fauth0-python)

The Auth0 Python library provides convenient access to the Auth0 APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Authentication API](#authentication-api)
- [Management API](#management-api)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Feedback](#feedback)

## Installation

> ⚠️ **This is a beta release (v5.0.0-beta)** of a major rewrite with breaking changes. See the [Migration Guide](v5_MIGRATION_GUIDE.md) for upgrade instructions from v4.x.

**Install the v5 beta:**

```sh
pip install auth0-python==5.0.0b0
```

**Requirements:**
- Python ≥3.8 (Python 3.7 support has been dropped)

## Reference

A full reference for this library is available [here](https://github.com/auth0/auth0-python/blob/HEAD/./reference.md).

## Authentication API

The Authentication API is used for authentication flows such as obtaining tokens via client credentials, authorization codes, or resource owner password grants:

```python
from auth0.authentication import GetToken

token_client = GetToken(
    domain="your-tenant.auth0.com",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

# Get an access token using client credentials
token_response = token_client.client_credentials(
    audience="https://your-tenant.auth0.com/api/v2/"
)
access_token = token_response["access_token"]
```

## Management API

### Recommended: Using ManagementClient

The `ManagementClient` is the recommended way to interact with the Auth0 Management API. It provides a simpler interface using just your Auth0 domain, and supports automatic token management with client credentials:

```python
from auth0.management import ManagementClient

# With an existing token
client = ManagementClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
)

# Or with client credentials (automatic token acquisition and refresh)
client = ManagementClient(
    domain="your-tenant.auth0.com",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
```

For async usage:

```python
import asyncio
from auth0.management import AsyncManagementClient

client = AsyncManagementClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
)

async def main() -> None:
    users = await client.users.list()
    print(users)

asyncio.run(main())
```

### Using a Token from the Authentication API

You can obtain a token using the Authentication API and use it with the Management API client:

```python
from auth0.authentication import GetToken
from auth0.management import Auth0

domain = "your-tenant.auth0.com"

# Get a token using the Authentication API
token_client = GetToken(
    domain=domain,
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
token_response = token_client.client_credentials(
    audience=f"https://{domain}/api/v2/"
)
access_token = token_response["access_token"]

# Use the token with the Management API client
client = Auth0(
    base_url=f"https://{domain}/api/v2",
    token=access_token,
)
```

### Using the Base Client

Alternatively, you can use the `Auth0` client directly with a full base URL:

```python
from auth0.management import ActionTrigger, Auth0

client = Auth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
)
client.actions.create(
    name="name",
    supported_triggers=[
        ActionTrigger(
            id="id",
        )
    ],
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from auth0.management import ActionTrigger, AsyncAuth0

client = AsyncAuth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.actions.create(
        name="name",
        supported_triggers=[
            ActionTrigger(
                id="id",
            )
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from auth0.management.core.api_error import ApiError

try:
    client.actions.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from auth0.management import Auth0

client = Auth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
)
response = client.actions.list(
    trigger_id="post-login",
    action_name="actionName",
    deployed=True,
    page=1,
    per_page=1,
    installed=True,
)
for item in response:
    print(item)
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    print(page)
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.actions.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from auth0.management import Auth0

client = Auth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
)
response = client.actions.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.actions.list(...)
print(pager.response)  # access the typed response for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.actions.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from auth0.management import Auth0

client = Auth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
    timeout=20.0,
)


# Override timeout for a specific method
client.actions.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from auth0.management import Auth0

client = Auth0(
    base_url="https://YOUR_TENANT.auth0.com/api/v2",
    token="YOUR_TOKEN",
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Feedback

### Contributing

We appreciate feedback and contribution to this repo! Before you get started, please see the following:

- [Auth0's general contribution guidelines](https://github.com/auth0/open-source-template/blob/master/GENERAL-CONTRIBUTING.md)
- [Auth0's code of conduct guidelines](https://github.com/auth0/open-source-template/blob/master/CODE-OF-CONDUCT.md)

### Raise an issue

To provide feedback or report a bug, please [raise an issue on our issue tracker](https://github.com/auth0/auth0-python/issues).

### Vulnerability Reporting

Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/responsible-disclosure-policy) details the procedure for disclosing security issues.

---

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.auth0.com/website/sdks/logos/auth0_light_mode.png"   width="150">
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.auth0.com/website/sdks/logos/auth0_dark_mode.png" width="150">
    <img alt="Auth0 Logo" src="https://cdn.auth0.com/website/sdks/logos/auth0_light_mode.png" width="150">
  </picture>
</p>
<p align="center">Auth0 is an easy to implement, adaptable authentication and authorization platform. To learn more checkout <a href="https://auth0.com/why-auth0">Why Auth0</a></p>
<p align="center">
This project is licensed under the MIT license. See the <a href="https://github.com/auth0/auth0-python/blob/master/LICENSE"> LICENSE</a> file for more info
</p>
