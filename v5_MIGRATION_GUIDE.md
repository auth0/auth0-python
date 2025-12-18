# v5 Migration Guide

A guide to migrating the Auth0 Python SDK from v4 to v5.

- [Overall changes](#overall-changes)
  - [Python versions](#python-versions)
  - [Authentication API](#authentication-api)
  - [Management API](#management-api)
- [Specific changes to the Management API](#specific-changes-to-the-management-api)
  - [Client initialization](#client-initialization)
  - [Return types: Pydantic models](#return-types-pydantic-models)
  - [Pagination](#pagination)

## Overall changes

### Python versions

v5 supports Python 3.8 and above.

### Authentication API

This major version change does not affect the Authentication API. Any code written for the Authentication API in v4 should work in v5.

### Management API

v5 introduces significant improvements to the Management API by migrating to [Fern](https://github.com/fern-api/fern) as our code generation tool. This brings several benefits:

- **Type safety**: All responses are now Pydantic models with full type hints.
- **IDE support**: Autocomplete and inline documentation for all API methods and response fields.
- **Automatic token management**: Built-in support for client credentials with automatic token caching and refresh.
- **Improved pagination**: New `SyncPager` and `AsyncPager` classes for easy iteration across paginated results.
- **Better resource organization**: Sub-resources are organized into sub-clients for a more intuitive API structure.

## Specific changes to the Management API

### Client initialization

v5 introduces a `ManagementClient` class with support for both token-based and client credentials authentication.

#### Token-based authentication

```python
# v4
from auth0.management import Auth0

domain = 'your-tenant.auth0.com'
token = 'MGMT_API_TOKEN'
auth0 = Auth0(domain, token)

# Access users
user = auth0.users.get('user_id')
```

```python
# v5
from auth0.management import ManagementClient

client = ManagementClient(
    domain="your-tenant.auth0.com",
    token="MGMT_API_TOKEN",
)

# Access users
user = client.users.get("user_id")
```

#### Client credentials authentication (new in v5)

v5 supports automatic token management when using client credentials. The token is automatically fetched, cached, and refreshed before expiration:

```python
# v5 with client credentials
from auth0.management import ManagementClient

client = ManagementClient(
    domain="your-tenant.auth0.com",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

# Token is automatically fetched and cached
# No need to manually obtain or refresh tokens
user = client.users.get("user_id")
```

#### Configuration options

```python
# v4
from auth0.management import Auth0
from auth0.rest import RestClientOptions

options = RestClientOptions(
    telemetry=True,
    timeout=5.0,
    retries=3
)
auth0 = Auth0(domain, token, rest_options=options)
```

```python
# v5
from auth0.management import ManagementClient

client = ManagementClient(
    domain="your-tenant.auth0.com",
    token="MGMT_API_TOKEN",
    timeout=60.0,  # Timeout in seconds
    headers={"X-Custom-Header": "value"},  # Custom headers
)
```

### Return types: Pydantic models

The most significant change is that all API responses are now **Pydantic models** instead of raw dictionaries. This provides type safety, IDE autocomplete, and validation.

#### Accessing response data

```python
# v4: Dictionary access
user = auth0.users.get('user_id')
print(user['email'])           # Dict key access
print(user.get('nickname'))    # Safe access with .get()

# Check if key exists
if 'app_metadata' in user:
    print(user['app_metadata'])
```

```python
# v5: Attribute access
user = client.users.get("user_id")
print(user.email)              # Attribute access
print(user.nickname)           # Direct attribute access (None if not present)

# Access nested data
if user.app_metadata:
    print(user.app_metadata)
```

#### Converting to dictionaries

If you need dictionary access for compatibility with existing code, use `model_dump()`:

```python
# v5: Convert to dict
user = client.users.get("user_id")
user_dict = user.model_dump()  # Returns a dictionary

# Now you can use dict-style access
print(user_dict['email'])
```

#### Benefits of Pydantic models

1. **IDE autocomplete**: Type `user.` and see all available fields
2. **Type checking**: Catch errors at development time with mypy or pyright
3. **Validation**: Data is validated against the schema
4. **Immutability**: Response objects are frozen by default

### Pagination

v5 introduces `SyncPager` (and `AsyncPager` for async) to simplify working with paginated endpoints.

#### v4 pagination pattern

```python
# v4: Manual pagination
all_users = []
page = 0

while True:
    result = auth0.users.list(page=page, per_page=50, include_totals=True)
    all_users.extend(result['users'])

    if len(all_users) >= result['total']:
        break
    page += 1

# Process all users
for user in all_users:
    print(user['email'])
```

#### v5 pagination patterns

**Automatic iteration** - The simplest approach, iterates across all pages automatically:

```python
# v5: Automatic iteration across all pages
for user in client.users.list():
    print(user.email)
```

**Page-by-page iteration** - When you need to process pages individually:

```python
# v5: Page-by-page iteration
for page in client.users.list().iter_pages():
    print(f"Processing {len(page.items)} users")
    for user in page.items:
        print(user.email)
```

**Manual pagination** - For explicit control over pagination:

```python
# v5: Manual pagination with explicit parameters
pager = client.users.list(page=0, per_page=50)

# Access current page items
for user in pager.items:
    print(user.email)

# Check if there are more pages
if pager.has_next:
    next_pager = pager.next_page()
    for user in next_pager.items:
        print(user.email)
```

#### Async pagination

For async code, use `AsyncManagementClient` with async iteration:

```python
# v5: Async pagination
from auth0.management import AsyncManagementClient

client = AsyncManagementClient(
    domain="your-tenant.auth0.com",
    token="MGMT_API_TOKEN",
)

# Async iteration
async for user in client.users.list():
    print(user.email)

# Async page-by-page
async for page in client.users.list().iter_pages():
    for user in page.items:
        print(user.email)
```
