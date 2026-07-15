# v6 Migration Guide

A guide to migrating the Auth0 Python SDK from v5 to v6.

- [Overall changes](#overall-changes)
- [Breaking changes](#breaking-changes)
  - [Federated connections tokensets removed](#federated-connections-tokensets-removed)
  - [`federated_connections_access_tokens` field removed](#federated_connections_access_tokens-field-removed)
  - [`read:federated_connections_tokens` / `delete:federated_connections_tokens` scopes removed](#readfederated_connections_tokens--deletefederated_connections_tokens-scopes-removed)
  - [`ClientSessionTransferDelegationDeviceBindingEnum` narrowed](#clientsessiontransferdelegationdevicebindingenum-narrowed)
  - [`ConnectionAttributeIdentifier` split into three types](#connectionattributeidentifier-split-into-three-types)
  - [`PhoneProviderProtectionBackoffStrategyEnum` value renamed](#phoneproviderprotectionbackoffstrategyenum-value-renamed)
  - [`ListRolesOffsetPaginatedResponseContent` pagination fields now required](#listrolesoffsetpaginatedresponsecontent-pagination-fields-now-required)
- [New features](#new-features)
  - [Network ACL: `auth0_managed` field](#network-acl-auth0_managed-field)
  - [Organizations: role members endpoint](#organizations-role-members-endpoint)
  - [Organizations: third-party client access](#organizations-third-party-client-access)
  - [Other additions](#other-additions)

## Overall changes

v6 removes one deprecated Management API surface (federated connections
tokensets) and tightens a handful of generated types to match the current
Auth0 Management API contract. Most applications will only be affected if
they use the specific types or endpoints listed below.

The Authentication API is not affected by this release.

## Breaking changes

### Federated connections tokensets removed

The `users.federated_connections_tokensets` sub-client and its `list`/`delete`
methods have been removed, along with the `FederatedConnectionTokenSet` and
`ConnectionFederatedConnectionsAccessTokens` types. This endpoint is no longer
part of the Auth0 Management API.

```python
# v5
client.users.federated_connections_tokensets.list(id="user_id")
client.users.federated_connections_tokensets.delete(id="user_id", tokenset_id="tokenset_id")
```

```python
# v6
# No replacement — the endpoint has been removed from the Management API.
```

If you depend on this functionality, do not upgrade until you have confirmed
an alternative with Auth0 support.

### `federated_connections_access_tokens` field removed

The optional `federated_connections_access_tokens` field has been removed
from:

- `ConnectionOptionsAzureAd`
- `ConnectionOptionsCommonOidc`
- `ConnectionOptionsGoogleApps`
- `ConnectionPropertiesOptions`
- `UpdateConnectionOptions`

Any code reading or setting this field on the above types will need to
remove that usage; passing it will simply be dropped as an unrecognized
field.

### `read:federated_connections_tokens` / `delete:federated_connections_tokens` scopes removed

These two values are no longer valid members of `OauthScope`. Remove any
references to them when requesting or checking scopes.

### `ClientSessionTransferDelegationDeviceBindingEnum` narrowed

The `"asn"` literal value has been removed. The enum now only accepts `"ip"`:

```python
# v5
ClientSessionTransferDelegationDeviceBindingEnum = typing.Union[typing.Literal["ip", "asn"], typing.Any]
```

```python
# v6
ClientSessionTransferDelegationDeviceBindingEnum = typing.Union[typing.Literal["ip"], typing.Any]
```

If you were setting this value to `"asn"`, update it to `"ip"` — this matches
the current Management API's accepted values.

### `ConnectionAttributeIdentifier` split into three types

`ConnectionAttributeIdentifier` has been removed with no compatibility alias.
It is replaced by three narrower types, one per attribute:

| Attribute field | v5 type | v6 type | Shape |
| --- | --- | --- | --- |
| `EmailAttribute.identifier` | `ConnectionAttributeIdentifier` | `EmailAttributeIdentifier` | `{active?, default_method?: DefaultMethodEmailIdentifierEnum}` |
| `PhoneAttribute.identifier` | `ConnectionAttributeIdentifier` | `PhoneAttributeIdentifier` | `{active?, default_method?: DefaultMethodPhoneNumberIdentifierEnum}` |
| `UsernameAttribute.identifier` | `ConnectionAttributeIdentifier` | `UsernameAttributeIdentifier` | `{active?}` (no `default_method`) |

```python
# v5
from auth0.management.types import ConnectionAttributeIdentifier

identifier = ConnectionAttributeIdentifier(active=True, default_method="email")
```

```python
# v6
from auth0.management.types import EmailAttributeIdentifier

identifier = EmailAttributeIdentifier(active=True, default_method="email")
```

`EmailAttributeIdentifier` has the same shape as the old
`ConnectionAttributeIdentifier` and is a drop-in replacement for code that
was only ever used with `EmailAttribute`. Code using
`ConnectionAttributeIdentifier` with `PhoneAttribute` or `UsernameAttribute`
must switch to `PhoneAttributeIdentifier` or `UsernameAttributeIdentifier`
respectively; `UsernameAttributeIdentifier` does not support
`default_method`.

### `PhoneProviderProtectionBackoffStrategyEnum` value renamed

The `"none"` literal has been replaced with `"default"`:

```python
# v5
PhoneProviderProtectionBackoffStrategyEnum = typing.Union[typing.Literal["exponential", "none"], typing.Any]
```

```python
# v6
PhoneProviderProtectionBackoffStrategyEnum = typing.Union[typing.Literal["exponential", "default"], typing.Any]
```

Replace any use of `"none"` with `"default"`.

### `ListRolesOffsetPaginatedResponseContent` pagination fields now required

`start`, `limit`, and `total` are no longer optional:

```python
# v5
start: typing.Optional[float] = None
limit: typing.Optional[float] = None
total: typing.Optional[float] = None
```

```python
# v6
start: float
limit: float
total: float
```

Deserializing a role-list response that is missing any of these fields now
raises `pydantic.ValidationError` instead of silently defaulting to `None`.
This matches the Management API, which always returns these fields for this
endpoint.

## New features

### Network ACL: `auth0_managed` field

`NetworkAclMatch` gains an optional `auth0_managed: Optional[List[str]]`
field (serialized as `auth0_managed`), available on both the `match` and
`not_match` rule blocks. Use it to reference Auth0-managed lists when
matching or excluding traffic:

```python
from auth0.management.types import NetworkAclMatch

match = NetworkAclMatch(auth_0_managed=["tor-exit-nodes"])
```

The Python attribute is `auth_0_managed`; it serializes to `auth0_managed`
over the wire. Both spellings are accepted as the constructor keyword.

### Organizations: role members endpoint

New sub-clients `organizations.roles` and `organizations.roles.members`
expose `GET /api/v2/organizations/{id}/roles/{role_id}/members`:

```python
for member in client.organizations.roles.members.list(id="org_id", role_id="role_id"):
    print(member)
```

This returns a `SyncPager`/`AsyncPager` of `RoleMember`, wrapping
`ListOrganizationRoleMembersResponseContent`.

### Organizations: third-party client access

`create()`/`update()` and all organization response types gain
`third_party_client_access: Optional[OrganizationThirdPartyClientAccessEnum]`
(`Literal["block", "allow"]`), controlling whether third-party clients can
access the organization.

### Other additions

- **Grants**: `UserGrant.organization_id: Optional[str]` (read-only), returned
  from `GET /grants`.
- **Connections**: `discovery_url` / `oidc_metadata` are now available on
  `samlp` connections (previously OIDC-only), via new `ConnectionsDiscoveryUrl`
  / `ConnectionsOidcMetadata` on `ConnectionPropertiesOptions` and
  `UpdateConnectionOptions`.
- **Event Streams**: new event-type values `connection.created`,
  `connection.deleted`, `connection.updated` on `EventStreamEventTypeEnum`,
  `EventStreamDeliveryEventTypeEnum`, `EventStreamSubscribeEventsEventTypeEnum`,
  and `EventStreamTestEventTypeEnum`; new
  `EventStreamCloudEventConnection{Created,Deleted,Updated}*` payload types;
  and `EventStreamSubscribeEventsResponseContent` extended with the
  connection event variants.
- **Token Vault**: new `grants: Optional[List[TokenVaultPrivilegedAccessGrant]]`
  on the privileged-access credential/public-key types.
  `TokenVaultPrivilegedAccessGrant`: `{connection: str, scopes: List[str]}`.
- **Errors**: new error body types `NotFoundErrorBody`/`NotFoundErrorBodyError`
  and `TooManyRequestsErrorBody`/`TooManyRequestsErrorBodyError`.
- **CloudEvent**: `specversion` is now typed as
  `EventStreamCloudEventSpecVersionEnum` (`Literal["1.0"]` + `Any` fallback)
  instead of `str`, across group/org/user CloudEvent types.
