# Reference
## Actions
<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">list</a>(...) -&gt; AsyncPager[Action, ListActionsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.list(
    trigger_id="triggerId",
    action_name="actionName",
    deployed=True,
    page=1,
    per_page=1,
    installed=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `typing.Optional[ActionTriggerTypeEnum]` — An actions extensibility point.
    
</dd>
</dl>

<dl>
<dd>

**action_name:** `typing.Optional[str]` — The name of the action to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**deployed:** `typing.Optional[bool]` — Optional filter to only retrieve actions that are deployed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Use this field to request a specific page of the list results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — The maximum number of results to be returned by the server in single response. 20 by default
    
</dd>
</dl>

<dl>
<dd>

**installed:** `typing.Optional[bool]` — Optional. When true, return only installed actions. When false, return only custom actions. Returns all actions by default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateActionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an action. Once an action is created, it must be deployed, and then bound to a trigger before it will be executed as part of a flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import ActionTrigger, Auth0

client = Auth0(
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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of an action.
    
</dd>
</dl>

<dl>
<dd>

**supported_triggers:** `typing.Sequence[ActionTrigger]` — The list of triggers that this action supports. At this time, an action can only target a single trigger at a time.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The source code of the action.
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[typing.Sequence[ActionVersionDependency]]` — The list of third party npm modules, and their versions, that this action depends on.
    
</dd>
</dl>

<dl>
<dd>

**runtime:** `typing.Optional[str]` — The Node runtime. For example: `node22`, defaults to `node22`
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Sequence[ActionSecretRequest]]` — The list of secrets that are included in an action or a version of an action.
    
</dd>
</dl>

<dl>
<dd>

**modules:** `typing.Optional[typing.Sequence[ActionModuleReference]]` — The list of action modules and their versions used by this action.
    
</dd>
</dl>

<dl>
<dd>

**deploy:** `typing.Optional[bool]` — True if the action should be deployed after creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetActionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an action by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the action to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an action and all of its associated versions. An action must be unbound from all triggers before it can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.delete(
    id="id",
    force=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the action to delete.
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — Force action deletion detaching bindings
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateActionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing action. If this action is currently bound to a trigger, updating it will <strong>not</strong> affect any user flows until the action is deployed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the action to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of an action.
    
</dd>
</dl>

<dl>
<dd>

**supported_triggers:** `typing.Optional[typing.Sequence[ActionTrigger]]` — The list of triggers that this action supports. At this time, an action can only target a single trigger at a time.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The source code of the action.
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[typing.Sequence[ActionVersionDependency]]` — The list of third party npm modules, and their versions, that this action depends on.
    
</dd>
</dl>

<dl>
<dd>

**runtime:** `typing.Optional[str]` — The Node runtime. For example: `node22`, defaults to `node22`
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Sequence[ActionSecretRequest]]` — The list of secrets that are included in an action or a version of an action.
    
</dd>
</dl>

<dl>
<dd>

**modules:** `typing.Optional[typing.Sequence[ActionModuleReference]]` — The list of action modules and their versions used by this action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">deploy</a>(...) -&gt; AsyncHttpResponse[DeployActionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy an action. Deploying an action will create a new immutable version of the action. If the action is currently bound to a trigger, then the system will begin executing the newly deployed version of the action immediately. Otherwise, the action will only be executed as a part of a flow once it is bound to that flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.deploy(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of an action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/auth0/management/actions/client.py">test</a>(...) -&gt; AsyncHttpResponse[TestActionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test an action. After updating an action, it can be tested prior to being deployed to ensure it behaves as expected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.test(
    id="id",
    payload={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the action to test.
    
</dd>
</dl>

<dl>
<dd>

**payload:** `TestActionPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Branding
<details><summary><code>client.branding.<a href="src/auth0/management/branding/client.py">get</a>() -&gt; AsyncHttpResponse[GetBrandingResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve branding settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.<a href="src/auth0/management/branding/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBrandingResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update branding settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**colors:** `typing.Optional[UpdateBrandingColors]` 
    
</dd>
</dl>

<dl>
<dd>

**favicon_url:** `typing.Optional[str]` — URL for the favicon. Must use HTTPS.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — URL for the logo. Must use HTTPS.
    
</dd>
</dl>

<dl>
<dd>

**font:** `typing.Optional[UpdateBrandingFont]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ClientGrants
<details><summary><code>client.client_grants.<a href="src/auth0/management/client_grants/client.py">list</a>(...) -&gt; AsyncPager[ClientGrantResponseContent, ListClientGrantPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of <a href="https://auth0.com/docs/get-started/applications/application-access-to-apis-client-grants">client grants</a>, including the scopes associated with the application/API pair.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.client_grants.list(
    from_="from",
    take=1,
    audience="audience",
    client_id="client_id",
    allow_any_organization=True,
    subject_type="client",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[str]` — Optional filter on audience.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Optional filter on client_id.
    
</dd>
</dl>

<dl>
<dd>

**allow_any_organization:** `typing.Optional[ClientGrantAllowAnyOrganizationEnum]` — Optional filter on allow_any_organization.
    
</dd>
</dl>

<dl>
<dd>

**subject_type:** `typing.Optional[ClientGrantSubjectTypeEnum]` — The type of application access the client grant allows.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_grants.<a href="src/auth0/management/client_grants/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateClientGrantResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a client grant for a machine-to-machine login flow. To learn more, read <a href="https://www.auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow">Client Credential Flow</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.client_grants.create(
    client_id="client_id",
    audience="audience",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `str` — The audience (API identifier) of this client grant
    
</dd>
</dl>

<dl>
<dd>

**organization_usage:** `typing.Optional[ClientGrantOrganizationUsageEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_any_organization:** `typing.Optional[bool]` — If enabled, any organization can be used with this grant. If disabled (default), the grant must be explicitly assigned to the desired organizations.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[typing.Sequence[str]]` — Scopes allowed for this client grant.
    
</dd>
</dl>

<dl>
<dd>

**subject_type:** `typing.Optional[ClientGrantSubjectTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization_details_types:** `typing.Optional[typing.Sequence[str]]` — Types of authorization_details allowed for this client grant.
    
</dd>
</dl>

<dl>
<dd>

**allow_all_scopes:** `typing.Optional[bool]` — If enabled, all scopes configured on the resource server are allowed for this grant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_grants.<a href="src/auth0/management/client_grants/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetClientGrantResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single <a href="https://auth0.com/docs/get-started/applications/application-access-to-apis-client-grants">client grant</a>, including the
scopes associated with the application/API pair.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.client_grants.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the client grant to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_grants.<a href="src/auth0/management/client_grants/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the <a href="https://www.auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow">Client Credential Flow</a> from your machine-to-machine application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.client_grants.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client grant to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_grants.<a href="src/auth0/management/client_grants/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateClientGrantResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a client grant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.client_grants.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client grant to update.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[typing.Sequence[str]]` — Scopes allowed for this client grant.
    
</dd>
</dl>

<dl>
<dd>

**organization_usage:** `typing.Optional[ClientGrantOrganizationNullableUsageEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_any_organization:** `typing.Optional[bool]` — Controls allowing any organization to be used with this grant
    
</dd>
</dl>

<dl>
<dd>

**authorization_details_types:** `typing.Optional[typing.Sequence[str]]` — Types of authorization_details allowed for this client grant.
    
</dd>
</dl>

<dl>
<dd>

**allow_all_scopes:** `typing.Optional[bool]` — If enabled, all scopes configured on the resource server are allowed for this grant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clients
<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">list</a>(...) -&gt; AsyncPager[Client, ListClientsOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve clients (applications and SSO integrations) matching provided filters. A list of fields to include or exclude may also be specified.
For more information, read <a href="https://www.auth0.com/docs/get-started/applications"> Applications in Auth0</a> and <a href="https://www.auth0.com/docs/authenticate/single-sign-on"> Single Sign-On</a>.

<ul>
  <li>
    The following can be retrieved with any scope:
    <code>client_id</code>, <code>app_type</code>, <code>name</code>, and <code>description</code>.
  </li>
  <li>
    The following properties can only be retrieved with the <code>read:clients</code> or
    <code>read:client_keys</code> scope:
    <code>callbacks</code>, <code>oidc_logout</code>, <code>allowed_origins</code>,
    <code>web_origins</code>, <code>tenant</code>, <code>global</code>, <code>config_route</code>,
    <code>callback_url_template</code>, <code>jwt_configuration</code>,
    <code>jwt_configuration.lifetime_in_seconds</code>, <code>jwt_configuration.secret_encoded</code>,
    <code>jwt_configuration.scopes</code>, <code>jwt_configuration.alg</code>, <code>api_type</code>,
    <code>logo_uri</code>, <code>allowed_clients</code>, <code>owners</code>, <code>custom_login_page</code>,
    <code>custom_login_page_off</code>, <code>sso</code>, <code>addons</code>, <code>form_template</code>,
    <code>custom_login_page_codeview</code>, <code>resource_servers</code>, <code>client_metadata</code>,
    <code>mobile</code>, <code>mobile.android</code>, <code>mobile.ios</code>, <code>allowed_logout_urls</code>,
    <code>token_endpoint_auth_method</code>, <code>is_first_party</code>, <code>oidc_conformant</code>,
    <code>is_token_endpoint_ip_header_trusted</code>, <code>initiate_login_uri</code>, <code>grant_types</code>,
    <code>refresh_token</code>, <code>refresh_token.rotation_type</code>, <code>refresh_token.expiration_type</code>,
    <code>refresh_token.leeway</code>, <code>refresh_token.token_lifetime</code>, <code>refresh_token.policies</code>, <code>organization_usage</code>,
    <code>organization_require_behavior</code>.
  </li>
  <li>
    The following properties can only be retrieved with the
    <code>read:client_keys</code> or <code>read:client_credentials</code> scope:
    <code>encryption_key</code>, <code>encryption_key.pub</code>, <code>encryption_key.cert</code>,
    <code>client_secret</code>, <code>client_authentication_methods</code> and <code>signing_key</code>.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.clients.list(
    fields="fields",
    include_fields=True,
    page=1,
    per_page=1,
    include_totals=True,
    is_global=True,
    is_first_party=True,
    app_type="app_type",
    q="q",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Default value is 50, maximum value is 100
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**is_global:** `typing.Optional[bool]` — Optional filter on the global client parameter.
    
</dd>
</dl>

<dl>
<dd>

**is_first_party:** `typing.Optional[bool]` — Optional filter on whether or not a client is a first-party client.
    
</dd>
</dl>

<dl>
<dd>

**app_type:** `typing.Optional[str]` — Optional filter by a comma-separated list of application types.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Advanced Query in <a href="http://www.lucenetutorial.com/lucene-query-syntax.html">Lucene</a> syntax.<br /><b>Permitted Queries</b>:<br /><ul><li><i>client_grant.organization_id:{organization_id}</i></li><li><i>client_grant.allow_any_organization:true</i></li></ul><b>Additional Restrictions</b>:<br /><ul><li>Cannot be used in combination with other filters</li><li>Requires use of the <i>from</i> and <i>take</i> paging parameters (checkpoint paginatinon)</li><li>Reduced rate limits apply. See <a href="https://auth0.com/docs/troubleshoot/customer-support/operational-policies/rate-limit-policy/rate-limit-configurations/enterprise-public">Rate Limit Configurations</a></li></ul><i><b>Note</b>: Recent updates may not be immediately reflected in query results</i>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateClientResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new client (application or SSO integration). For more information, read <a href="https://www.auth0.com/docs/get-started/auth0-overview/create-applications">Create Applications</a>
<a href="https://www.auth0.com/docs/authenticate/single-sign-on/api-endpoints-for-single-sign-on>">API Endpoints for Single Sign-On</a>. 

Notes: 
- We recommend leaving the `client_secret` parameter unspecified to allow the generation of a safe secret.
- The <code>client_authentication_methods</code> and <code>token_endpoint_auth_method</code> properties are mutually exclusive. Use 
<code>client_authentication_methods</code> to configure the client with Private Key JWT authentication method. Otherwise, use <code>token_endpoint_auth_method</code>
to configure the client with client secret (basic or post) or with no authentication method (none).
- When using <code>client_authentication_methods</code> to configure the client with Private Key JWT authentication method, specify fully defined credentials. 
These credentials will be automatically enabled for Private Key JWT authentication on the client. 
- To configure <code>client_authentication_methods</code>, the <code>create:client_credentials</code> scope is required.
- To configure <code>client_authentication_methods</code>, the property <code>jwt_configuration.alg</code> must be set to RS256.

<div class="alert alert-warning">SSO Integrations created via this endpoint will accept login requests and share user profile information.</div>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of this client (min length: 1 character, does not allow `<` or `>`).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Free text description of this client (max length: 140 characters).
    
</dd>
</dl>

<dl>
<dd>

**logo_uri:** `typing.Optional[str]` — URL of the logo to display for this client. Recommended size is 150x150 pixels.
    
</dd>
</dl>

<dl>
<dd>

**callbacks:** `typing.Optional[typing.Sequence[str]]` — Comma-separated list of URLs whitelisted for Auth0 to use as a callback to the client after authentication.
    
</dd>
</dl>

<dl>
<dd>

**oidc_logout:** `typing.Optional[ClientOidcBackchannelLogoutSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**oidc_backchannel_logout:** `typing.Optional[ClientOidcBackchannelLogoutSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**session_transfer:** `typing.Optional[ClientSessionTransferConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[typing.Sequence[str]]` — Comma-separated list of URLs allowed to make requests from JavaScript to Auth0 API (typically used with CORS). By default, all your callback URLs will be allowed. This field allows you to enter other origins if necessary. You can also use wildcards at the subdomain level (e.g., https://*.contoso.com). Query strings and hash information are not taken into account when validating these URLs.
    
</dd>
</dl>

<dl>
<dd>

**web_origins:** `typing.Optional[typing.Sequence[str]]` — Comma-separated list of allowed origins for use with <a href='https://auth0.com/docs/cross-origin-authentication'>Cross-Origin Authentication</a>, <a href='https://auth0.com/docs/flows/concepts/device-auth'>Device Flow</a>, and <a href='https://auth0.com/docs/protocols/oauth2#how-response-mode-works'>web message response mode</a>.
    
</dd>
</dl>

<dl>
<dd>

**client_aliases:** `typing.Optional[typing.Sequence[str]]` — List of audiences/realms for SAML protocol. Used by the wsfed addon.
    
</dd>
</dl>

<dl>
<dd>

**allowed_clients:** `typing.Optional[typing.Sequence[str]]` — List of allow clients and API ids that are allowed to make delegation requests. Empty means all all your clients are allowed.
    
</dd>
</dl>

<dl>
<dd>

**allowed_logout_urls:** `typing.Optional[typing.Sequence[str]]` — Comma-separated list of URLs that are valid to redirect to after logout from Auth0. Wildcards are allowed for subdomains.
    
</dd>
</dl>

<dl>
<dd>

**grant_types:** `typing.Optional[typing.Sequence[str]]` — List of grant types supported for this application. Can include `authorization_code`, `implicit`, `refresh_token`, `client_credentials`, `password`, `http://auth0.com/oauth/grant-type/password-realm`, `http://auth0.com/oauth/grant-type/mfa-oob`, `http://auth0.com/oauth/grant-type/mfa-otp`, `http://auth0.com/oauth/grant-type/mfa-recovery-code`, `urn:openid:params:grant-type:ciba`, `urn:ietf:params:oauth:grant-type:device_code`, and `urn:auth0:params:oauth:grant-type:token-exchange:federated-connection-access-token`.
    
</dd>
</dl>

<dl>
<dd>

**token_endpoint_auth_method:** `typing.Optional[ClientTokenEndpointAuthMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_token_endpoint_ip_header_trusted:** `typing.Optional[bool]` — If true, trust that the IP specified in the `auth0-forwarded-for` header is the end-user's IP for brute-force-protection on token endpoint.
    
</dd>
</dl>

<dl>
<dd>

**app_type:** `typing.Optional[ClientAppTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_first_party:** `typing.Optional[bool]` — Whether this client a first party client or not
    
</dd>
</dl>

<dl>
<dd>

**oidc_conformant:** `typing.Optional[bool]` — Whether this client conforms to <a href='https://auth0.com/docs/api-auth/tutorials/adoption'>strict OIDC specifications</a> (true) or uses legacy features (false).
    
</dd>
</dl>

<dl>
<dd>

**jwt_configuration:** `typing.Optional[ClientJwtConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**encryption_key:** `typing.Optional[ClientEncryptionKey]` 
    
</dd>
</dl>

<dl>
<dd>

**sso:** `typing.Optional[bool]` — Applies only to SSO clients and determines whether Auth0 will handle Single Sign On (true) or whether the Identity Provider will (false).
    
</dd>
</dl>

<dl>
<dd>

**cross_origin_authentication:** `typing.Optional[bool]` — Whether this client can be used to make cross-origin authentication requests (true) or it is not allowed to make such requests (false).
    
</dd>
</dl>

<dl>
<dd>

**cross_origin_loc:** `typing.Optional[str]` — URL of the location in your site where the cross origin verification takes place for the cross-origin auth flow when performing Auth in your own domain instead of Auth0 hosted login page.
    
</dd>
</dl>

<dl>
<dd>

**sso_disabled:** `typing.Optional[bool]` — <code>true</code> to disable Single Sign On, <code>false</code> otherwise (default: <code>false</code>)
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page_on:** `typing.Optional[bool]` — <code>true</code> if the custom login page is to be used, <code>false</code> otherwise. Defaults to <code>true</code>
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page:** `typing.Optional[str]` — The content (HTML, CSS, JS) of the custom login page.
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page_preview:** `typing.Optional[str]` — The content (HTML, CSS, JS) of the custom login page. (Used on Previews)
    
</dd>
</dl>

<dl>
<dd>

**form_template:** `typing.Optional[str]` — HTML form template to be used for WS-Federation.
    
</dd>
</dl>

<dl>
<dd>

**addons:** `typing.Optional[ClientAddons]` 
    
</dd>
</dl>

<dl>
<dd>

**client_metadata:** `typing.Optional[ClientMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**mobile:** `typing.Optional[ClientMobile]` 
    
</dd>
</dl>

<dl>
<dd>

**initiate_login_uri:** `typing.Optional[str]` — Initiate login uri, must be https
    
</dd>
</dl>

<dl>
<dd>

**native_social_login:** `typing.Optional[NativeSocialLogin]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[ClientRefreshTokenConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**default_organization:** `typing.Optional[ClientDefaultOrganization]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_usage:** `typing.Optional[ClientOrganizationUsageEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_require_behavior:** `typing.Optional[ClientOrganizationRequireBehaviorEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_discovery_methods:** `typing.Optional[typing.Sequence[ClientOrganizationDiscoveryEnum]]` — Defines the available methods for organization discovery during the `pre_login_prompt`. Users can discover their organization either by `email`, `organization_name` or both.
    
</dd>
</dl>

<dl>
<dd>

**client_authentication_methods:** `typing.Optional[ClientCreateAuthenticationMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**require_pushed_authorization_requests:** `typing.Optional[bool]` — Makes the use of Pushed Authorization Requests mandatory for this client
    
</dd>
</dl>

<dl>
<dd>

**require_proof_of_possession:** `typing.Optional[bool]` — Makes the use of Proof-of-Possession mandatory for this client
    
</dd>
</dl>

<dl>
<dd>

**signed_request_object:** `typing.Optional[ClientSignedRequestObjectWithPublicKey]` 
    
</dd>
</dl>

<dl>
<dd>

**compliance_level:** `typing.Optional[ClientComplianceLevelEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_non_verifiable_callback_uri_confirmation_prompt:** `typing.Optional[bool]` 

Controls whether a confirmation prompt is shown during login flows when the redirect URI uses non-verifiable callback URIs (for example, a custom URI schema such as `myapp://`, or `localhost`).
If set to true, a confirmation prompt will not be shown. We recommend that this is set to false for improved protection from malicious apps.
See https://auth0.com/docs/secure/security-guidance/measures-against-app-impersonation for more information.
    
</dd>
</dl>

<dl>
<dd>

**token_exchange:** `typing.Optional[ClientTokenExchangeConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**par_request_expiry:** `typing.Optional[int]` — Specifies how long, in seconds, a Pushed Authorization Request URI remains valid
    
</dd>
</dl>

<dl>
<dd>

**token_quota:** `typing.Optional[CreateTokenQuota]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_server_identifier:** `typing.Optional[str]` — The identifier of the resource server that this client is linked to.
    
</dd>
</dl>

<dl>
<dd>

**express_configuration:** `typing.Optional[ExpressConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**async_approval_notification_channels:** `typing.Optional[ClientAsyncApprovalNotificationsChannelsApiPostConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetClientResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve client details by ID. Clients are SSO connections or Applications linked with your Auth0 tenant. A list of fields to include or exclude may also be specified. 
For more information, read <a href="https://www.auth0.com/docs/get-started/applications"> Applications in Auth0</a> and <a href="https://www.auth0.com/docs/authenticate/single-sign-on"> Single Sign-On</a>.
<ul>
  <li>
    The following properties can be retrieved with any of the scopes:
    <code>client_id</code>, <code>app_type</code>, <code>name</code>, and <code>description</code>.
  </li>
  <li>
    The following properties can only be retrieved with the <code>read:clients</code> or
    <code>read:client_keys</code> scopes:
    <code>callbacks</code>, <code>oidc_logout</code>, <code>allowed_origins</code>,
    <code>web_origins</code>, <code>tenant</code>, <code>global</code>, <code>config_route</code>,
    <code>callback_url_template</code>, <code>jwt_configuration</code>,
    <code>jwt_configuration.lifetime_in_seconds</code>, <code>jwt_configuration.secret_encoded</code>,
    <code>jwt_configuration.scopes</code>, <code>jwt_configuration.alg</code>, <code>api_type</code>,
    <code>logo_uri</code>, <code>allowed_clients</code>, <code>owners</code>, <code>custom_login_page</code>,
    <code>custom_login_page_off</code>, <code>sso</code>, <code>addons</code>, <code>form_template</code>,
    <code>custom_login_page_codeview</code>, <code>resource_servers</code>, <code>client_metadata</code>,
    <code>mobile</code>, <code>mobile.android</code>, <code>mobile.ios</code>, <code>allowed_logout_urls</code>,
    <code>token_endpoint_auth_method</code>, <code>is_first_party</code>, <code>oidc_conformant</code>,
    <code>is_token_endpoint_ip_header_trusted</code>, <code>initiate_login_uri</code>, <code>grant_types</code>,
    <code>refresh_token</code>, <code>refresh_token.rotation_type</code>, <code>refresh_token.expiration_type</code>,
    <code>refresh_token.leeway</code>, <code>refresh_token.token_lifetime</code>, <code>refresh_token.policies</code>, <code>organization_usage</code>,
    <code>organization_require_behavior</code>.
  </li>
  <li>
    The following properties can only be retrieved with the <code>read:client_keys</code> or <code>read:client_credentials</code> scopes:
    <code>encryption_key</code>, <code>encryption_key.pub</code>, <code>encryption_key.cert</code>,
    <code>client_secret</code>, <code>client_authentication_methods</code> and <code>signing_key</code>.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.get(
    id="id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a client and related configuration (rules, connections, etc).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateClientResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a client's settings. For more information, read <a href="https://www.auth0.com/docs/get-started/applications"> Applications in Auth0</a> and <a href="https://www.auth0.com/docs/authenticate/single-sign-on"> Single Sign-On</a>.

Notes:
- The `client_secret` and `signing_key` attributes can only be updated with the `update:client_keys` scope.
- The <code>client_authentication_methods</code> and <code>token_endpoint_auth_method</code> properties are mutually exclusive. Use <code>client_authentication_methods</code> to configure the client with Private Key JWT authentication method. Otherwise, use <code>token_endpoint_auth_method</code> to configure the client with client secret (basic or post) or with no authentication method (none).
- When using <code>client_authentication_methods</code> to configure the client with Private Key JWT authentication method, only specify the credential IDs that were generated when creating the credentials on the client.
- To configure <code>client_authentication_methods</code>, the <code>update:client_credentials</code> scope is required.
- To configure <code>client_authentication_methods</code>, the property <code>jwt_configuration.alg</code> must be set to RS256.
- To change a client's <code>is_first_party</code> property to <code>false</code>, the <code>organization_usage</code> and <code>organization_require_behavior</code> properties must be unset.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the client. Must contain at least one character. Does not allow '<' or '>'.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Free text description of the purpose of the Client. (Max character length: <code>140</code>)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — The secret used to sign tokens for the client
    
</dd>
</dl>

<dl>
<dd>

**logo_uri:** `typing.Optional[str]` — The URL of the client logo (recommended size: 150x150)
    
</dd>
</dl>

<dl>
<dd>

**callbacks:** `typing.Optional[typing.Sequence[str]]` — A set of URLs that are valid to call back from Auth0 when authenticating users
    
</dd>
</dl>

<dl>
<dd>

**oidc_logout:** `typing.Optional[ClientOidcBackchannelLogoutSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**oidc_backchannel_logout:** `typing.Optional[ClientOidcBackchannelLogoutSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**session_transfer:** `typing.Optional[ClientSessionTransferConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[typing.Sequence[str]]` — A set of URLs that represents valid origins for CORS
    
</dd>
</dl>

<dl>
<dd>

**web_origins:** `typing.Optional[typing.Sequence[str]]` — A set of URLs that represents valid web origins for use with web message response mode
    
</dd>
</dl>

<dl>
<dd>

**grant_types:** `typing.Optional[typing.Sequence[str]]` — A set of grant types that the client is authorized to use. Can include `authorization_code`, `implicit`, `refresh_token`, `client_credentials`, `password`, `http://auth0.com/oauth/grant-type/password-realm`, `http://auth0.com/oauth/grant-type/mfa-oob`, `http://auth0.com/oauth/grant-type/mfa-otp`, `http://auth0.com/oauth/grant-type/mfa-recovery-code`, `urn:openid:params:grant-type:ciba`, `urn:ietf:params:oauth:grant-type:device_code`, and `urn:auth0:params:oauth:grant-type:token-exchange:federated-connection-access-token`.
    
</dd>
</dl>

<dl>
<dd>

**client_aliases:** `typing.Optional[typing.Sequence[str]]` — List of audiences for SAML protocol
    
</dd>
</dl>

<dl>
<dd>

**allowed_clients:** `typing.Optional[typing.Sequence[str]]` — Ids of clients that will be allowed to perform delegation requests. Clients that will be allowed to make delegation request. By default, all your clients will be allowed. This field allows you to specify specific clients
    
</dd>
</dl>

<dl>
<dd>

**allowed_logout_urls:** `typing.Optional[typing.Sequence[str]]` — URLs that are valid to redirect to after logout from Auth0
    
</dd>
</dl>

<dl>
<dd>

**jwt_configuration:** `typing.Optional[ClientJwtConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**encryption_key:** `typing.Optional[ClientEncryptionKey]` 
    
</dd>
</dl>

<dl>
<dd>

**sso:** `typing.Optional[bool]` — <code>true</code> to use Auth0 instead of the IdP to do Single Sign On, <code>false</code> otherwise (default: <code>false</code>)
    
</dd>
</dl>

<dl>
<dd>

**cross_origin_authentication:** `typing.Optional[bool]` — <code>true</code> if this client can be used to make cross-origin authentication requests, <code>false</code> otherwise if cross origin is disabled
    
</dd>
</dl>

<dl>
<dd>

**cross_origin_loc:** `typing.Optional[str]` — URL for the location in your site where the cross origin verification takes place for the cross-origin auth flow when performing Auth in your own domain instead of Auth0 hosted login page.
    
</dd>
</dl>

<dl>
<dd>

**sso_disabled:** `typing.Optional[bool]` — <code>true</code> to disable Single Sign On, <code>false</code> otherwise (default: <code>false</code>)
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page_on:** `typing.Optional[bool]` — <code>true</code> if the custom login page is to be used, <code>false</code> otherwise.
    
</dd>
</dl>

<dl>
<dd>

**token_endpoint_auth_method:** `typing.Optional[ClientTokenEndpointAuthMethodOrNullEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_token_endpoint_ip_header_trusted:** `typing.Optional[bool]` — If true, trust that the IP specified in the `auth0-forwarded-for` header is the end-user's IP for brute-force-protection on token endpoint.
    
</dd>
</dl>

<dl>
<dd>

**app_type:** `typing.Optional[ClientAppTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_first_party:** `typing.Optional[bool]` — Whether this client a first party client or not
    
</dd>
</dl>

<dl>
<dd>

**oidc_conformant:** `typing.Optional[bool]` — Whether this client will conform to strict OIDC specifications
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page:** `typing.Optional[str]` — The content (HTML, CSS, JS) of the custom login page
    
</dd>
</dl>

<dl>
<dd>

**custom_login_page_preview:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**token_quota:** `typing.Optional[UpdateTokenQuota]` 
    
</dd>
</dl>

<dl>
<dd>

**form_template:** `typing.Optional[str]` — Form template for WS-Federation protocol
    
</dd>
</dl>

<dl>
<dd>

**addons:** `typing.Optional[ClientAddons]` 
    
</dd>
</dl>

<dl>
<dd>

**client_metadata:** `typing.Optional[ClientMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**mobile:** `typing.Optional[ClientMobile]` 
    
</dd>
</dl>

<dl>
<dd>

**initiate_login_uri:** `typing.Optional[str]` — Initiate login uri, must be https
    
</dd>
</dl>

<dl>
<dd>

**native_social_login:** `typing.Optional[NativeSocialLogin]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[ClientRefreshTokenConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**default_organization:** `typing.Optional[ClientDefaultOrganization]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_usage:** `typing.Optional[ClientOrganizationUsagePatchEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_require_behavior:** `typing.Optional[ClientOrganizationRequireBehaviorPatchEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_discovery_methods:** `typing.Optional[typing.Sequence[ClientOrganizationDiscoveryEnum]]` — Defines the available methods for organization discovery during the `pre_login_prompt`. Users can discover their organization either by `email`, `organization_name` or both.
    
</dd>
</dl>

<dl>
<dd>

**client_authentication_methods:** `typing.Optional[ClientAuthenticationMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**require_pushed_authorization_requests:** `typing.Optional[bool]` — Makes the use of Pushed Authorization Requests mandatory for this client
    
</dd>
</dl>

<dl>
<dd>

**require_proof_of_possession:** `typing.Optional[bool]` — Makes the use of Proof-of-Possession mandatory for this client
    
</dd>
</dl>

<dl>
<dd>

**signed_request_object:** `typing.Optional[ClientSignedRequestObjectWithCredentialId]` 
    
</dd>
</dl>

<dl>
<dd>

**compliance_level:** `typing.Optional[ClientComplianceLevelEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_non_verifiable_callback_uri_confirmation_prompt:** `typing.Optional[bool]` 

Controls whether a confirmation prompt is shown during login flows when the redirect URI uses non-verifiable callback URIs (for example, a custom URI schema such as `myapp://`, or `localhost`).
If set to true, a confirmation prompt will not be shown. We recommend that this is set to false for improved protection from malicious apps.
See https://auth0.com/docs/secure/security-guidance/measures-against-app-impersonation for more information.
    
</dd>
</dl>

<dl>
<dd>

**token_exchange:** `typing.Optional[ClientTokenExchangeConfigurationOrNull]` 
    
</dd>
</dl>

<dl>
<dd>

**par_request_expiry:** `typing.Optional[int]` — Specifies how long, in seconds, a Pushed Authorization Request URI remains valid
    
</dd>
</dl>

<dl>
<dd>

**express_configuration:** `typing.Optional[ExpressConfigurationOrNull]` 
    
</dd>
</dl>

<dl>
<dd>

**async_approval_notification_channels:** `typing.Optional[ClientAsyncApprovalNotificationsChannelsApiPatchConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/auth0/management/clients/client.py">rotate_secret</a>(...) -&gt; AsyncHttpResponse[RotateClientSecretResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate a client secret.

This endpoint cannot be used with clients configured with Private Key JWT authentication method (client_authentication_methods configured with private_key_jwt). The generated secret is NOT base64 encoded.

For more information, read <a href="https://www.auth0.com/docs/get-started/applications/rotate-client-secret">Rotate Client Secrets</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.rotate_secret(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client that will rotate secrets.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConnectionProfiles
<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">list</a>(...) -&gt; AsyncPager[ConnectionProfile, ListConnectionProfilesPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of Connection Profiles. This endpoint supports Checkpoint pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.connection_profiles.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 5.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateConnectionProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Connection Profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `ConnectionProfileName` 
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[ConnectionProfileOrganization]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_name_prefix_template:** `typing.Optional[ConnectionNamePrefixTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_features:** `typing.Optional[ConnectionProfileEnabledFeatures]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_config:** `typing.Optional[ConnectionProfileConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**strategy_overrides:** `typing.Optional[ConnectionProfileStrategyOverrides]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">list_templates</a>() -&gt; AsyncHttpResponse[ListConnectionProfileTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of Connection Profile Templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.list_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">get_template</a>(...) -&gt; AsyncHttpResponse[GetConnectionProfileTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a Connection Profile Template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.get_template(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection-profile-template to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetConnectionProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single Connection Profile specified by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection-profile to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single Connection Profile specified by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection-profile to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection_profiles.<a href="src/auth0/management/connection_profiles/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateConnectionProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a specific Connection Profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connection_profiles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection profile to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[ConnectionProfileName]` 
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[ConnectionProfileOrganization]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_name_prefix_template:** `typing.Optional[ConnectionNamePrefixTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_features:** `typing.Optional[ConnectionProfileEnabledFeatures]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_config:** `typing.Optional[ConnectionProfileConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**strategy_overrides:** `typing.Optional[ConnectionProfileStrategyOverrides]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections
<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">list</a>(...) -&gt; AsyncPager[ConnectionForList, ListConnectionsCheckpointPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed list of all <a href="https://auth0.com/docs/authenticate/identity-providers">connections</a> that match the specified strategy. If no strategy is provided, all connections within your tenant are retrieved. This action can accept a list of fields to include or exclude from the resulting list of connections. 

This endpoint supports two types of pagination:
<ul>
<li>Offset pagination</li>
<li>Checkpoint pagination</li>
</ul>

Checkpoint pagination must be used if you need to retrieve more than 1000 connections.

<h2>Checkpoint Pagination</h2>

To search by checkpoint, use the following parameters:
<ul>
<li><code>from</code>: Optional id from which to start selection.</li>
<li><code>take</code>: The total amount of entries to retrieve when using the from parameter. Defaults to 50.</li>
</ul>

<b>Note</b>: The first time you call this endpoint using checkpoint pagination, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no pages are remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.connections.list(
    from_="from",
    take=1,
    name="name",
    fields="fields",
    include_fields=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `typing.Optional[
    typing.Union[
        ConnectionStrategyEnum, typing.Sequence[ConnectionStrategyEnum]
    ]
]` — Provide strategies to only retrieve connections with such strategies
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Provide the name of the connection to retrieve
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — <code>true</code> if the fields specified are to be included in the result, <code>false</code> otherwise (defaults to <code>true</code>)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new connection according to the JSON object received in <code>body</code>.

<b>Note:</b> If a connection with the same name was recently deleted and had a large number of associated users, the deletion may still be processing. Creating a new connection with that name before the deletion completes may fail or produce unexpected results. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.create(
    name="name",
    strategy="ad",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the connection. Must start and end with an alphanumeric character and can only contain alphanumeric characters and '-'. Max length 128
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `ConnectionIdentityProviderEnum` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Connection name used in the new universal login experience
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ConnectionPropertiesOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_clients:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED property. Use the PATCH /v2/connections/{id}/clients endpoint to enable the connection for a set of clients.
    
</dd>
</dl>

<dl>
<dd>

**is_domain_connection:** `typing.Optional[bool]` — <code>true</code> promotes to a domain-level connection so that third-party applications can use it. <code>false</code> does not promote the connection, so only first-party applications with the connection enabled can use it. (Defaults to <code>false</code>.)
    
</dd>
</dl>

<dl>
<dd>

**show_as_button:** `typing.Optional[bool]` — Enables showing a button for the connection in the login page (new experience only). If false, it will be usable only by HRD. (Defaults to <code>false</code>.)
    
</dd>
</dl>

<dl>
<dd>

**realms:** `typing.Optional[typing.Sequence[str]]` — Defines the realms for which the connection will be used (ie: email domains). If the array is empty or the property is not specified, the connection name will be added as realm.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[ConnectionsMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**authentication:** `typing.Optional[ConnectionAuthenticationPurpose]` 
    
</dd>
</dl>

<dl>
<dd>

**connected_accounts:** `typing.Optional[ConnectionConnectedAccountsPurpose]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specified <a href="https://auth0.com/docs/authenticate/identity-providers">connection</a> along with options that can be used for identity provider configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.get(
    id="id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — <code>true</code> if the fields specified are to be included in the result, <code>false</code> otherwise (defaults to <code>true</code>)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a specific <a href="https://auth0.com/docs/authenticate/identity-providers">connection</a> from your tenant. This action cannot be undone. Once removed, users can no longer use this connection to authenticate.

<b>Note:</b> If your connection has a large amount of users associated with it, please be aware that this operation can be long running after the response is returned and may impact concurrent <a href="https://auth0.com/docs/api/management/v2/connections/post-connections">create connection</a> requests, if they use an identical connection name. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update details for a specific <a href="https://auth0.com/docs/authenticate/identity-providers">connection</a>, including option properties for identity provider configuration.

<b>Note</b>: If you use the <code>options</code> parameter, the entire <code>options</code> object is overriden. To avoid partial data or other issues, ensure all parameters are present when using this option.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to update
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The connection name used in the new universal login experience. If display_name is not included in the request, the field will be overwritten with the name value.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[UpdateConnectionOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_clients:** `typing.Optional[typing.Sequence[str]]` — DEPRECATED property. Use the PATCH /v2/connections/{id}/clients endpoint to enable or disable the connection for any clients.
    
</dd>
</dl>

<dl>
<dd>

**is_domain_connection:** `typing.Optional[bool]` — <code>true</code> promotes to a domain-level connection so that third-party applications can use it. <code>false</code> does not promote the connection, so only first-party applications with the connection enabled can use it. (Defaults to <code>false</code>.)
    
</dd>
</dl>

<dl>
<dd>

**show_as_button:** `typing.Optional[bool]` — Enables showing a button for the connection in the login page (new experience only). If false, it will be usable only by HRD. (Defaults to <code>false</code>.)
    
</dd>
</dl>

<dl>
<dd>

**realms:** `typing.Optional[typing.Sequence[str]]` — Defines the realms for which the connection will be used (ie: email domains). If the array is empty or the property is not specified, the connection name will be added as realm.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[ConnectionsMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**authentication:** `typing.Optional[ConnectionAuthenticationPurpose]` 
    
</dd>
</dl>

<dl>
<dd>

**connected_accounts:** `typing.Optional[ConnectionConnectedAccountsPurpose]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/auth0/management/connections/client.py">check_status</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the status of an ad/ldap connection referenced by its <code>ID</code>. <code>200 OK</code> http status code response is returned  when the connection is online, otherwise a <code>404</code> status code is returned along with an error message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.check_status(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection to check
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomDomains
<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListCustomDomainsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details on <a href="https://auth0.com/docs/custom-domains">custom domains</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.list(
    q="q",
    fields="fields",
    include_fields=True,
    sort="sort",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query in <a href ="http://www.lucenetutorial.com/lucene-query-syntax.html">Lucene query string syntax</a>.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Only <code>domain:1</code> (ascending order by domain) is supported at this time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateCustomDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new custom domain.

Note: The custom domain will need to be verified before it will accept
requests.

Optional attributes that can be updated:

- custom_client_ip_header
- tls_policy


TLS Policies:

- recommended - for modern usage this includes TLS 1.2 only
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.create(
    domain="domain",
    type="auth0_managed_certs",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — Domain name.
    
</dd>
</dl>

<dl>
<dd>

**type:** `CustomDomainProvisioningTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**verification_method:** `typing.Optional[CustomDomainVerificationMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**tls_policy:** `typing.Optional[CustomDomainTlsPolicyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_client_ip_header:** `typing.Optional[CustomDomainCustomClientIpHeader]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_metadata:** `typing.Optional[DomainMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**relying_party_identifier:** `typing.Optional[str]` — Relying Party ID (rpId) to be used for Passkeys on this custom domain. If not provided, the full domain will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetCustomDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a custom domain configuration and status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the custom domain to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom domain and stop serving requests for it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the custom domain to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateCustomDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a custom domain.

These are the attributes that can be updated:

- custom_client_ip_header
- tls_policy

<h5>Updating CUSTOM_CLIENT_IP_HEADER for a custom domain</h5>To update the <code>custom_client_ip_header</code> for a domain, the body to
send should be:
<pre><code>{ "custom_client_ip_header": "cf-connecting-ip" }</code></pre>

<h5>Updating TLS_POLICY for a custom domain</h5>To update the <code>tls_policy</code> for a domain, the body to send should be:
<pre><code>{ "tls_policy": "recommended" }</code></pre>


TLS Policies:

- recommended - for modern usage this includes TLS 1.2 only


Some considerations:

- The TLS ciphers and protocols available in each TLS policy follow industry recommendations, and may be updated occasionally.
- The <code>compatible</code> TLS policy is no longer supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the custom domain to update
    
</dd>
</dl>

<dl>
<dd>

**tls_policy:** `typing.Optional[CustomDomainTlsPolicyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_client_ip_header:** `typing.Optional[CustomDomainCustomClientIpHeader]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_metadata:** `typing.Optional[DomainMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**relying_party_identifier:** `typing.Optional[str]` — Relying Party ID (rpId) to be used for Passkeys on this custom domain. Set to null to remove the rpId and fall back to using the full domain.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">test</a>(...) -&gt; AsyncHttpResponse[TestCustomDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the test process on a custom domain.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.test(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the custom domain to test.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_domains.<a href="src/auth0/management/custom_domains/client.py">verify</a>(...) -&gt; AsyncHttpResponse[VerifyCustomDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the verification process on a custom domain.

Note: Check the <code>status</code> field to see its verification status. Once verification is complete, it may take up to 10 minutes before the custom domain can start accepting requests.

For <code>self_managed_certs</code>, when the custom domain is verified for the first time, the response will also include the <code>cname_api_key</code> which you will need to configure your proxy. This key must be kept secret, and is used to validate the proxy requests.

<a href="https://auth0.com/docs/custom-domains#step-2-verify-ownership">Learn more</a> about verifying custom domains that use Auth0 Managed certificates.
<a href="https://auth0.com/docs/custom-domains/self-managed-certificates#step-2-verify-ownership">Learn more</a> about verifying custom domains that use Self Managed certificates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.custom_domains.verify(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the custom domain to verify.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DeviceCredentials
<details><summary><code>client.device_credentials.<a href="src/auth0/management/device_credentials/client.py">list</a>(...) -&gt; AsyncPager[
    DeviceCredential, ListDeviceCredentialsOffsetPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve device credential information (<code>public_key</code>, <code>refresh_token</code>, or <code>rotating_refresh_token</code>) associated with a specific user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.device_credentials.list(
    page=1,
    per_page=1,
    include_totals=True,
    fields="fields",
    include_fields=True,
    user_id="user_id",
    client_id="client_id",
    type="public_key",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.  There is a maximum of 1000 results allowed from this endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — user_id of the devices to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — client_id of the devices to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DeviceCredentialTypeEnum]` — Type of credentials to retrieve. Must be `public_key`, `refresh_token` or `rotating_refresh_token`. The property will default to `refresh_token` when paging is requested
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_credentials.<a href="src/auth0/management/device_credentials/client.py">create_public_key</a>(...) -&gt; AsyncHttpResponse[CreatePublicKeyDeviceCredentialResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a device credential public key to manage refresh token rotation for a given <code>user_id</code>. Device Credentials APIs are designed for ad-hoc administrative use only and paging is by default enabled for GET requests.

When refresh token rotation is enabled, the endpoint becomes consistent. For more information, read <a href="https://auth0.com/docs/get-started/tenant-settings/signing-keys"> Signing Keys</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.device_credentials.create_public_key(
    device_name="device_name",
    type="public_key",
    value="value",
    device_id="device_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_name:** `str` — Name for this device easily recognized by owner.
    
</dd>
</dl>

<dl>
<dd>

**type:** `DeviceCredentialPublicKeyTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Base64 encoded string containing the credential.
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `str` — Unique identifier for the device. Recommend using <a href="http://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID">Android_ID</a> on Android and <a href="https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/index.html#//apple_ref/occ/instp/UIDevice/identifierForVendor">identifierForVendor</a>.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — client_id of the client (application) this credential is for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_credentials.<a href="src/auth0/management/device_credentials/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a device credential (such as a refresh token or public key) with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.device_credentials.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the credential to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EmailTemplates
<details><summary><code>client.email_templates.<a href="src/auth0/management/email_templates/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateEmailTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an email template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.email_templates.create(
    template="verify_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template:** `EmailTemplateNameEnum` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Body of the email template.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Senders `from` email address.
    
</dd>
</dl>

<dl>
<dd>

**result_url:** `typing.Optional[str]` — URL to redirect the user to after a successful action.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject line of the email.
    
</dd>
</dl>

<dl>
<dd>

**syntax:** `typing.Optional[str]` — Syntax of the template body.
    
</dd>
</dl>

<dl>
<dd>

**url_lifetime_in_seconds:** `typing.Optional[float]` — Lifetime in seconds that the link within the email will be valid for.
    
</dd>
</dl>

<dl>
<dd>

**include_email_in_redirect:** `typing.Optional[bool]` — Whether the `reset_email` and `verify_email` templates should include the user's email address as the `email` parameter in the returnUrl (true) or whether no email address should be included in the redirect (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the template is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_templates.<a href="src/auth0/management/email_templates/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetEmailTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an email template by pre-defined name. These names are `verify_email`, `verify_email_by_code`, `reset_email`, `reset_email_by_code`, `welcome_email`, `blocked_account`, `stolen_credentials`, `enrollment_email`, `mfa_oob_code`, `user_invitation`, and `async_approval`. The names `change_password`, and `password_reset` are also supported for legacy scenarios.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.email_templates.get(
    template_name="verify_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_name:** `EmailTemplateNameEnum` — Template name. Can be `verify_email`, `verify_email_by_code`, `reset_email`, `reset_email_by_code`, `welcome_email`, `blocked_account`, `stolen_credentials`, `enrollment_email`, `mfa_oob_code`, `user_invitation`, `async_approval`, `change_password` (legacy), or `password_reset` (legacy).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_templates.<a href="src/auth0/management/email_templates/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetEmailTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an email template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.email_templates.set(
    template_name="verify_email",
    template="verify_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_name:** `EmailTemplateNameEnum` — Template name. Can be `verify_email`, `verify_email_by_code`, `reset_email`, `reset_email_by_code`, `welcome_email`, `blocked_account`, `stolen_credentials`, `enrollment_email`, `mfa_oob_code`, `user_invitation`, `async_approval`, `change_password` (legacy), or `password_reset` (legacy).
    
</dd>
</dl>

<dl>
<dd>

**template:** `EmailTemplateNameEnum` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Body of the email template.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Senders `from` email address.
    
</dd>
</dl>

<dl>
<dd>

**result_url:** `typing.Optional[str]` — URL to redirect the user to after a successful action.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject line of the email.
    
</dd>
</dl>

<dl>
<dd>

**syntax:** `typing.Optional[str]` — Syntax of the template body.
    
</dd>
</dl>

<dl>
<dd>

**url_lifetime_in_seconds:** `typing.Optional[float]` — Lifetime in seconds that the link within the email will be valid for.
    
</dd>
</dl>

<dl>
<dd>

**include_email_in_redirect:** `typing.Optional[bool]` — Whether the `reset_email` and `verify_email` templates should include the user's email address as the `email` parameter in the returnUrl (true) or whether no email address should be included in the redirect (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the template is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email_templates.<a href="src/auth0/management/email_templates/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateEmailTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify an email template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.email_templates.update(
    template_name="verify_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_name:** `EmailTemplateNameEnum` — Template name. Can be `verify_email`, `verify_email_by_code`, `reset_email`, `reset_email_by_code`, `welcome_email`, `blocked_account`, `stolen_credentials`, `enrollment_email`, `mfa_oob_code`, `user_invitation`, `async_approval`, `change_password` (legacy), or `password_reset` (legacy).
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[EmailTemplateNameEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Body of the email template.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Senders `from` email address.
    
</dd>
</dl>

<dl>
<dd>

**result_url:** `typing.Optional[str]` — URL to redirect the user to after a successful action.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject line of the email.
    
</dd>
</dl>

<dl>
<dd>

**syntax:** `typing.Optional[str]` — Syntax of the template body.
    
</dd>
</dl>

<dl>
<dd>

**url_lifetime_in_seconds:** `typing.Optional[float]` — Lifetime in seconds that the link within the email will be valid for.
    
</dd>
</dl>

<dl>
<dd>

**include_email_in_redirect:** `typing.Optional[bool]` — Whether the `reset_email` and `verify_email` templates should include the user's email address as the `email` parameter in the returnUrl (true) or whether no email address should be included in the redirect (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the template is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EventStreams
<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">list</a>(...) -&gt; AsyncPager[EventStreamResponseContent, ListEventStreamsResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.event_streams.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateEventStreamResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    CreateEventStreamWebHookRequestContent,
    EventStreamWebhookBasicAuth,
    EventStreamWebhookConfiguration,
    EventStreamWebhookDestination,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.create(
    request=CreateEventStreamWebHookRequestContent(
        destination=EventStreamWebhookDestination(
            type="webhook",
            configuration=EventStreamWebhookConfiguration(
                webhook_endpoint="webhook_endpoint",
                webhook_authorization=EventStreamWebhookBasicAuth(
                    method="basic",
                    username="username",
                ),
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EventStreamsCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetEventStreamResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateEventStreamResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the event stream.
    
</dd>
</dl>

<dl>
<dd>

**subscriptions:** `typing.Optional[typing.Sequence[EventStreamSubscription]]` — List of event types subscribed to in this stream.
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[EventStreamDestinationPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[EventStreamStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.<a href="src/auth0/management/event_streams/client.py">test</a>(...) -&gt; AsyncHttpResponse[CreateEventStreamTestEventResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.test(
    id="id",
    event_type="user.created",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `EventStreamTestEventTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[TestEventDataContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flows
<details><summary><code>client.flows.<a href="src/auth0/management/flows/client.py">list</a>(...) -&gt; AsyncPager[FlowSummary, ListFlowsOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.flows.list(
    page=1,
    per_page=1,
    include_totals=True,
    synchronous=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**hydrate:** `typing.Optional[
    typing.Union[
        ListFlowsRequestParametersHydrateEnum,
        typing.Sequence[ListFlowsRequestParametersHydrateEnum],
    ]
]` — hydration param
    
</dd>
</dl>

<dl>
<dd>

**synchronous:** `typing.Optional[bool]` — flag to filter by sync/async flows
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.<a href="src/auth0/management/flows/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateFlowResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[FlowAction]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.<a href="src/auth0/management/flows/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetFlowResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow identifier
    
</dd>
</dl>

<dl>
<dd>

**hydrate:** `typing.Optional[
    typing.Union[
        GetFlowRequestParametersHydrateEnum,
        typing.Sequence[GetFlowRequestParametersHydrateEnum],
    ]
]` — hydration param
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.<a href="src/auth0/management/flows/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.<a href="src/auth0/management/flows/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateFlowResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow identifier
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[FlowAction]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Forms
<details><summary><code>client.forms.<a href="src/auth0/management/forms/client.py">list</a>(...) -&gt; AsyncPager[FormSummary, ListFormsOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.forms.list(
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**hydrate:** `typing.Optional[
    typing.Union[
        FormsRequestParametersHydrateEnum,
        typing.Sequence[FormsRequestParametersHydrateEnum],
    ]
]` — Query parameter to hydrate the response with additional data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/auth0/management/forms/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateFormResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.forms.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[FormMessages]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[FormLanguages]` 
    
</dd>
</dl>

<dl>
<dd>

**translations:** `typing.Optional[FormTranslations]` 
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Optional[FormNodeList]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[FormStartNode]` 
    
</dd>
</dl>

<dl>
<dd>

**ending:** `typing.Optional[FormEndingNode]` 
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[FormStyle]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/auth0/management/forms/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetFormResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.forms.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the form to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**hydrate:** `typing.Optional[
    typing.Union[
        FormsRequestParametersHydrateEnum,
        typing.Sequence[FormsRequestParametersHydrateEnum],
    ]
]` — Query parameter to hydrate the response with additional data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/auth0/management/forms/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.forms.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the form to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/auth0/management/forms/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateFormResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.forms.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the form to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[FormMessagesNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[FormLanguagesNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**translations:** `typing.Optional[FormTranslationsNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Optional[FormNodeListNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[FormStartNodeNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**ending:** `typing.Optional[FormEndingNodeNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[FormStyleNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserGrants
<details><summary><code>client.user_grants.<a href="src/auth0/management/user_grants/client.py">list</a>(...) -&gt; AsyncPager[UserGrant, ListUserGrantsOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the <a href="https://auth0.com/docs/api-auth/which-oauth-flow-to-use">grants</a> associated with your account. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.user_grants.list(
    per_page=1,
    page=1,
    include_totals=True,
    user_id="user_id",
    client_id="client_id",
    audience="audience",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — user_id of the grants to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — client_id of the grants to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[str]` — audience of the grants to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_grants.<a href="src/auth0/management/user_grants/client.py">delete_by_user_id</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a grant associated with your account. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_grants.delete_by_user_id(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — user_id of the grant to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_grants.<a href="src/auth0/management/user_grants/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a grant associated with your account. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_grants.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the grant to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/auth0/management/groups/client.py">list</a>(...) -&gt; AsyncPager[Group, ListGroupsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all groups in your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.groups.list(
    connection_id="connection_id",
    name="name",
    external_id="external_id",
    fields="fields",
    include_fields=True,
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — Filter groups by connection ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter groups by name.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — Filter groups by external ID.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/auth0/management/groups/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetGroupResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a group by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.groups.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the group (service-generated).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Hooks
<details><summary><code>client.hooks.<a href="src/auth0/management/hooks/client.py">list</a>(...) -&gt; AsyncPager[Hook, ListHooksOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all <a href="https://auth0.com/docs/hooks">hooks</a>. Accepts a list of fields to include or exclude in the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.hooks.list(
    page=1,
    per_page=1,
    include_totals=True,
    enabled=True,
    fields="fields",
    trigger_id="credentials-exchange",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Optional filter on whether a hook is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**trigger_id:** `typing.Optional[HookTriggerIdEnum]` — Retrieves hooks that match the trigger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.<a href="src/auth0/management/hooks/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateHookResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new hook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.create(
    name="name",
    script="script",
    trigger_id="credentials-exchange",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of this hook.
    
</dd>
</dl>

<dl>
<dd>

**script:** `str` — Code to be executed when this hook runs.
    
</dd>
</dl>

<dl>
<dd>

**trigger_id:** `HookTriggerIdEnum` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether this hook will be executed (true) or ignored (false).
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[HookDependencies]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.<a href="src/auth0/management/hooks/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetHookResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve <a href="https://auth0.com/docs/hooks">a hook</a> by its ID. Accepts a list of fields to include in the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.get(
    id="id",
    fields="fields",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.<a href="src/auth0/management/hooks/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a hook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.<a href="src/auth0/management/hooks/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateHookResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing hook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this hook.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Optional[str]` — Code to be executed when this hook runs.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether this hook will be executed (true) or ignored (false).
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[HookDependencies]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/auth0/management/jobs/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetJobResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a job. Useful to check its status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.jobs.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LogStreams
<details><summary><code>client.log_streams.<a href="src/auth0/management/log_streams/client.py">list</a>() -&gt; AsyncHttpResponse[typing.List[LogStreamResponseSchema]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details on <a href="https://auth0.com/docs/logs/streams">log streams</a>.
<h5>Sample Response</h5><pre><code>[{
	"id": "string",
	"name": "string",
	"type": "eventbridge",
	"status": "active|paused|suspended",
	"sink": {
		"awsAccountId": "string",
		"awsRegion": "string",
		"awsPartnerEventSource": "string"
	}
}, {
	"id": "string",
	"name": "string",
	"type": "http",
	"status": "active|paused|suspended",
	"sink": {
		"httpContentFormat": "JSONLINES|JSONARRAY",
		"httpContentType": "string",
		"httpEndpoint": "string",
		"httpAuthorization": "string"
	}
},
{
	"id": "string",
	"name": "string",
	"type": "eventgrid",
	"status": "active|paused|suspended",
	"sink": {
		"azureSubscriptionId": "string",
		"azureResourceGroup": "string",
		"azureRegion": "string",
		"azurePartnerTopic": "string"
	}
},
{
	"id": "string",
	"name": "string",
	"type": "splunk",
	"status": "active|paused|suspended",
	"sink": {
		"splunkDomain": "string",
		"splunkToken": "string",
		"splunkPort": "string",
		"splunkSecure": "boolean"
	}
},
{
	"id": "string",
	"name": "string",
	"type": "sumo",
	"status": "active|paused|suspended",
	"sink": {
		"sumoSourceAddress": "string",
	}
},
{
	"id": "string",
	"name": "string",
	"type": "datadog",
	"status": "active|paused|suspended",
	"sink": {
		"datadogRegion": "string",
		"datadogApiKey": "string"
	}
}]</code></pre>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.log_streams.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_streams.<a href="src/auth0/management/log_streams/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateLogStreamResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a log stream.
<h5>Log Stream Types</h5> The <code>type</code> of log stream being created determines the properties required in the <code>sink</code> payload.
<h5>HTTP Stream</h5> For an <code>http</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "http",
	"sink": {
		"httpEndpoint": "string",
		"httpContentType": "string",
		"httpContentFormat": "JSONLINES|JSONARRAY",
		"httpAuthorization": "string"
	}
}</code></pre>
Response: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "http",
	"status": "active",
	"sink": {
		"httpEndpoint": "string",
		"httpContentType": "string",
		"httpContentFormat": "JSONLINES|JSONARRAY",
		"httpAuthorization": "string"
	}
}</code></pre>
<h5>Amazon EventBridge Stream</h5> For an <code>eventbridge</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "eventbridge",
	"sink": {
		"awsRegion": "string",
		"awsAccountId": "string"
	}
}</code></pre>
The response will include an additional field <code>awsPartnerEventSource</code> in the <code>sink</code>: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "eventbridge",
	"status": "active",
	"sink": {
		"awsAccountId": "string",
		"awsRegion": "string",
		"awsPartnerEventSource": "string"
	}
}</code></pre>
<h5>Azure Event Grid Stream</h5> For an <code>Azure Event Grid</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "eventgrid",
	"sink": {
		"azureSubscriptionId": "string",
		"azureResourceGroup": "string",
		"azureRegion": "string"
	}
}</code></pre>
Response: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "http",
	"status": "active",
	"sink": {
		"azureSubscriptionId": "string",
		"azureResourceGroup": "string",
		"azureRegion": "string",
		"azurePartnerTopic": "string"
	}
}</code></pre>
<h5>Datadog Stream</h5> For a <code>Datadog</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "datadog",
	"sink": {
		"datadogRegion": "string",
		"datadogApiKey": "string"
	}
}</code></pre>
Response: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "datadog",
	"status": "active",
	"sink": {
		"datadogRegion": "string",
		"datadogApiKey": "string"
	}
}</code></pre>
<h5>Splunk Stream</h5> For a <code>Splunk</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "splunk",
	"sink": {
		"splunkDomain": "string",
		"splunkToken": "string",
		"splunkPort": "string",
		"splunkSecure": "boolean"
	}
}</code></pre>
Response: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "splunk",
	"status": "active",
	"sink": {
		"splunkDomain": "string",
		"splunkToken": "string",
		"splunkPort": "string",
		"splunkSecure": "boolean"
	}
}</code></pre>
<h5>Sumo Logic Stream</h5> For a <code>Sumo Logic</code> Stream, the <code>sink</code> properties are listed in the payload below
Request: <pre><code>{
	"name": "string",
	"type": "sumo",
	"sink": {
		"sumoSourceAddress": "string",
	}
}</code></pre>
Response: <pre><code>{
	"id": "string",
	"name": "string",
	"type": "sumo",
	"status": "active",
	"sink": {
		"sumoSourceAddress": "string",
	}
}</code></pre>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, CreateLogStreamHttpRequestBody, LogStreamHttpSink

client = Auth0(
    token="YOUR_TOKEN",
)
client.log_streams.create(
    request=CreateLogStreamHttpRequestBody(
        type="http",
        sink=LogStreamHttpSink(
            http_endpoint="httpEndpoint",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateLogStreamRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_streams.<a href="src/auth0/management/log_streams/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetLogStreamResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a log stream configuration and status.
<h5>Sample responses</h5><h5>Amazon EventBridge Log Stream</h5><pre><code>{
	"id": "string",
	"name": "string",
	"type": "eventbridge",
	"status": "active|paused|suspended",
	"sink": {
		"awsAccountId": "string",
		"awsRegion": "string",
		"awsPartnerEventSource": "string"
	}
}</code></pre> <h5>HTTP Log Stream</h5><pre><code>{
	"id": "string",
	"name": "string",
	"type": "http",
	"status": "active|paused|suspended",
	"sink": {
		"httpContentFormat": "JSONLINES|JSONARRAY",
		"httpContentType": "string",
		"httpEndpoint": "string",
		"httpAuthorization": "string"
	}
}</code></pre> <h5>Datadog Log Stream</h5><pre><code>{
	"id": "string",
	"name": "string",
	"type": "datadog",
	"status": "active|paused|suspended",
	"sink": {
		"datadogRegion": "string",
		"datadogApiKey": "string"
	}

}</code></pre><h5>Mixpanel</h5>
	
	Request: <pre><code>{
	  "name": "string",
	  "type": "mixpanel",
	  "sink": {
		"mixpanelRegion": "string", // "us" | "eu",
		"mixpanelProjectId": "string",
		"mixpanelServiceAccountUsername": "string",
		"mixpanelServiceAccountPassword": "string"
	  }
	} </code></pre>
	
	
	Response: <pre><code>{
		"id": "string",
		"name": "string",
		"type": "mixpanel",
		"status": "active",
		"sink": {
		  "mixpanelRegion": "string", // "us" | "eu",
		  "mixpanelProjectId": "string",
		  "mixpanelServiceAccountUsername": "string",
		  "mixpanelServiceAccountPassword": "string" // the following is redacted on return
		}
	  } </code></pre>

	<h5>Segment</h5>

	Request: <pre><code> {
	  "name": "string",
	  "type": "segment",
	  "sink": {
		"segmentWriteKey": "string"
	  }
	}</code></pre>
	
	Response: <pre><code>{
	  "id": "string",
	  "name": "string",
	  "type": "segment",
	  "status": "active",
	  "sink": {
		"segmentWriteKey": "string"
	  }
	} </code></pre>
	
<h5>Splunk Log Stream</h5><pre><code>{
	"id": "string",
	"name": "string",
	"type": "splunk",
	"status": "active|paused|suspended",
	"sink": {
		"splunkDomain": "string",
		"splunkToken": "string",
		"splunkPort": "string",
		"splunkSecure": "boolean"
	}
}</code></pre> <h5>Sumo Logic Log Stream</h5><pre><code>{
	"id": "string",
	"name": "string",
	"type": "sumo",
	"status": "active|paused|suspended",
	"sink": {
		"sumoSourceAddress": "string",
	}
}</code></pre> <h5>Status</h5> The <code>status</code> of a log stream maybe any of the following:
1. <code>active</code> - Stream is currently enabled.
2. <code>paused</code> - Stream is currently user disabled and will not attempt log delivery.
3. <code>suspended</code> - Stream is currently disabled because of errors and will not attempt log delivery.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.log_streams.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the log stream to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_streams.<a href="src/auth0/management/log_streams/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a log stream.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.log_streams.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the log stream to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_streams.<a href="src/auth0/management/log_streams/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateLogStreamResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a log stream.
<h4>Examples of how to use the PATCH endpoint.</h4> The following fields may be updated in a PATCH operation: <ul><li>name</li><li>status</li><li>sink</li></ul> Note: For log streams of type <code>eventbridge</code> and <code>eventgrid</code>, updating the <code>sink</code> is not permitted.
<h5>Update the status of a log stream</h5><pre><code>{
	"status": "active|paused"
}</code></pre>
<h5>Update the name of a log stream</h5><pre><code>{
	"name": "string"
}</code></pre>
<h5>Update the sink properties of a stream of type <code>http</code></h5><pre><code>{
  "sink": {
    "httpEndpoint": "string",
    "httpContentType": "string",
    "httpContentFormat": "JSONARRAY|JSONLINES",
    "httpAuthorization": "string"
  }
}</code></pre>
<h5>Update the sink properties of a stream of type <code>datadog</code></h5><pre><code>{
  "sink": {
		"datadogRegion": "string",
		"datadogApiKey": "string"
  }
}</code></pre>
<h5>Update the sink properties of a stream of type <code>splunk</code></h5><pre><code>{
  "sink": {
    "splunkDomain": "string",
    "splunkToken": "string",
    "splunkPort": "string",
    "splunkSecure": "boolean"
  }
}</code></pre>
<h5>Update the sink properties of a stream of type <code>sumo</code></h5><pre><code>{
  "sink": {
    "sumoSourceAddress": "string"
  }
}</code></pre> 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.log_streams.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the log stream to get
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — log stream name
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[LogStreamStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_priority:** `typing.Optional[bool]` — True for priority log streams, false for non-priority
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[LogStreamFilter]]` — Only logs events matching these filters will be delivered by the stream. If omitted or empty, all events will be delivered.
    
</dd>
</dl>

<dl>
<dd>

**pii_config:** `typing.Optional[LogStreamPiiConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**sink:** `typing.Optional[LogStreamSinkPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Logs
<details><summary><code>client.logs.<a href="src/auth0/management/logs/client.py">list</a>(...) -&gt; AsyncPager[Log, ListLogOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve log entries that match the specified search criteria (or all log entries if no criteria specified).

Set custom search criteria using the <code>q</code> parameter, or search from a specific log ID (<i>"search from checkpoint"</i>).

For more information on all possible event types, their respective acronyms, and descriptions, see <a href="https://auth0.com/docs/logs/log-event-type-codes">Log Event Type Codes</a>.

<h5>To set custom search criteria, use the following parameters:</h5>

<ul>
    <li><b>q:</b> Search Criteria using <a href="https://auth0.com/docs/logs/log-search-query-syntax">Query String Syntax</a></li>
    <li><b>page:</b> Page index of the results to return. First page is 0.</li>
    <li><b>per_page:</b> Number of results per page.</li>
    <li><b>sort:</b> Field to use for sorting appended with `:1` for ascending and `:-1` for descending. e.g. `date:-1`</li>
    <li><b>fields:</b> Comma-separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields.</li>
    <li><b>include_fields:</b> Whether specified fields are to be included (true) or excluded (false).</li>
    <li><b>include_totals:</b> Return results inside an object that contains the total result count (true) or as a direct array of results (false, default). <b>Deprecated:</b> this field is deprecated and should be removed from use. See <a href="https://auth0.com/docs/product-lifecycle/deprecations-and-migrations/migrate-to-tenant-log-search-v3#pagination">Search Engine V3 Breaking Changes</a></li>
</ul>

For more information on the list of fields that can be used in <code>fields</code> and <code>sort</code>, see <a href="https://auth0.com/docs/logs/log-search-query-syntax#searchable-fields">Searchable Fields</a>.

Auth0 <a href="https://auth0.com/docs/logs/retrieve-log-events-using-mgmt-api#limitations">limits the number of logs</a> you can return by search criteria to 100 logs per request. Furthermore, you may paginate only through 1,000 search results. If you exceed this threshold, please redefine your search or use the <a href="https://auth0.com/docs/logs/retrieve-log-events-using-mgmt-api#retrieve-logs-by-checkpoint">get logs by checkpoint method</a>.

<h5>To search from a checkpoint log ID, use the following parameters:</h5>
<ul>
    <li><b>from:</b> Log Event ID from which to start retrieving logs. You can limit the number of logs returned using the <code>take</code> parameter. If you use <code>from</code> at the same time as <code>q</code>, <code>from</code> takes precedence and <code>q</code> is ignored.</li>
    <li><b>take:</b> Number of entries to retrieve when using the <code>from</code> parameter.</li>
</ul>

<strong>Important:</strong> When fetching logs from a checkpoint log ID, any parameter other than <code>from</code> and <code>take</code> will be ignored, and date ordering is not guaranteed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.logs.list(
    page=1,
    per_page=1,
    sort="sort",
    fields="fields",
    include_fields=True,
    include_totals=True,
    search="search",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` —  Number of results per page. Paging is disabled if parameter not sent. Default: <code>50</code>. Max value: <code>100</code>
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to use for sorting appended with <code>:1</code>  for ascending and <code>:-1</code> for descending. e.g. <code>date:-1</code>
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for <code>include_fields</code>) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (<code>true</code>) or excluded (<code>false</code>)
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results as an array when false (default). Return results inside an object that also contains a total result count when true.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Retrieves logs that match the specified search criteria. This parameter can be combined with all the others in the /api/logs endpoint but is specified separately for clarity.
If no fields are provided a case insensitive 'starts with' search is performed on all of the following fields: client_name, connection, user_name. Otherwise, you can specify multiple fields and specify the search using the %field%:%search%, for example: application:node user:"John@contoso.com".
Values specified without quotes are matched using a case insensitive 'starts with' search. If quotes are used a case insensitve exact search is used. If multiple fields are used, the AND operator is used to join the clauses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/auth0/management/logs/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetLogResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an individual log event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.logs.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — log_id of the log to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NetworkAcls
<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">list</a>(...) -&gt; AsyncPager[
    NetworkAclsResponseContent, ListNetworkAclsOffsetPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all access control list entries for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.network_acls.list(
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Use this field to request a specific page of the list results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — The amount of results per page.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">create</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new access control list for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, NetworkAclAction, NetworkAclRule

client = Auth0(
    token="YOUR_TOKEN",
)
client.network_acls.create(
    description="description",
    active=True,
    priority=1.1,
    rule=NetworkAclRule(
        action=NetworkAclAction(),
        scope="management",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` — Indicates whether or not this access control list is actively being used
    
</dd>
</dl>

<dl>
<dd>

**priority:** `float` — Indicates the order in which the ACL will be evaluated relative to other ACL rules.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `NetworkAclRule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetNetworkAclsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific access control list entry for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.network_acls.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the access control list to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetNetworkAclsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update existing access control list for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, NetworkAclAction, NetworkAclRule

client = Auth0(
    token="YOUR_TOKEN",
)
client.network_acls.set(
    id="id",
    description="description",
    active=True,
    priority=1.1,
    rule=NetworkAclRule(
        action=NetworkAclAction(),
        scope="management",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the ACL to update.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` — Indicates whether or not this access control list is actively being used
    
</dd>
</dl>

<dl>
<dd>

**priority:** `float` — Indicates the order in which the ACL will be evaluated relative to other ACL rules.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `NetworkAclRule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete existing access control list for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.network_acls.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the ACL to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_acls.<a href="src/auth0/management/network_acls/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateNetworkAclResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update existing access control list for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.network_acls.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the ACL to update.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Indicates whether or not this access control list is actively being used
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[float]` — Indicates the order in which the ACL will be evaluated relative to other ACL rules.
    
</dd>
</dl>

<dl>
<dd>

**rule:** `typing.Optional[NetworkAclRule]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">list</a>(...) -&gt; AsyncPager[Organization, ListOrganizationsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list of all Organizations available in your tenant. For more information, see Auth0 Organizations.

This endpoint supports two types of pagination:
<ul>
<li>Offset pagination</li>
<li>Checkpoint pagination</li>
</ul>

Checkpoint pagination must be used if you need to retrieve more than 1000 organizations.

<h2>Checkpoint Pagination</h2>

To search by checkpoint, use the following parameters:
<ul>
<li><code>from</code>: Optional id from which to start selection.</li>
<li><code>take</code>: The total number of entries to retrieve when using the <code>from</code> parameter. Defaults to 50.</li>
</ul>

<b>Note</b>: The first time you call this endpoint using checkpoint pagination, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no pages are remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.list(
    from_="from",
    take=1,
    sort="sort",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Use <code>field:order</code> where order is <code>1</code> for ascending and <code>-1</code> for descending. e.g. <code>created_at:1</code>. We currently support sorting by the following fields: <code>name</code>, <code>display_name</code> and <code>created_at</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateOrganizationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Organization within your tenant.  To learn more about Organization settings, behavior, and configuration options, review <a href="https://auth0.com/docs/manage-users/organizations/create-first-organization">Create Your First Organization</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of this organization.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Friendly name of this organization.
    
</dd>
</dl>

<dl>
<dd>

**branding:** `typing.Optional[OrganizationBranding]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[OrganizationMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_connections:** `typing.Optional[typing.Sequence[ConnectionForOrganization]]` — Connections that will be enabled for this organization. See POST enabled_connections endpoint for the object format. (Max of 10 connections allowed)
    
</dd>
</dl>

<dl>
<dd>

**token_quota:** `typing.Optional[CreateTokenQuota]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">get_by_name</a>(...) -&gt; AsyncHttpResponse[GetOrganizationByNameResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single Organization specified by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.get_by_name(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — name of the organization to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetOrganizationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single Organization specified by ID. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an Organization from your tenant.  This action cannot be undone. 

<b>Note</b>: Members are automatically disassociated from an Organization when it is deleted. However, this action does <b>not</b> delete these users from your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/auth0/management/organizations/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateOrganizationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a specific <a href="https://auth0.com/docs/manage-users/organizations/configure-organizations/create-organizations">Organization</a>, such as name and display name, branding options, and metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization to update.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Friendly name of this organization.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of this organization.
    
</dd>
</dl>

<dl>
<dd>

**branding:** `typing.Optional[OrganizationBranding]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[OrganizationMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**token_quota:** `typing.Optional[UpdateTokenQuota]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts
<details><summary><code>client.prompts.<a href="src/auth0/management/prompts/client.py">get_settings</a>() -&gt; AsyncHttpResponse[GetSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the Universal Login configuration of your tenant. This includes the <a href="https://auth0.com/docs/authenticate/login/auth0-universal-login/identifier-first">Identifier First Authentication</a> and <a href="https://auth0.com/docs/secure/multi-factor-authentication/fido-authentication-with-webauthn/configure-webauthn-device-biometrics-for-mfa">WebAuthn with Device Biometrics for MFA</a> features.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.get_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/auth0/management/prompts/client.py">update_settings</a>(...) -&gt; AsyncHttpResponse[UpdateSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the Universal Login configuration of your tenant. This includes the <a href="https://auth0.com/docs/authenticate/login/auth0-universal-login/identifier-first">Identifier First Authentication</a> and <a href="https://auth0.com/docs/secure/multi-factor-authentication/fido-authentication-with-webauthn/configure-webauthn-device-biometrics-for-mfa">WebAuthn with Device Biometrics for MFA</a> features.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.update_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**universal_login_experience:** `typing.Optional[UniversalLoginExperienceEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**identifier_first:** `typing.Optional[bool]` — Whether identifier first is enabled or not
    
</dd>
</dl>

<dl>
<dd>

**webauthn_platform_first_factor:** `typing.Optional[bool]` — Use WebAuthn with Device Biometrics as the first authentication factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RefreshTokens
<details><summary><code>client.refresh_tokens.<a href="src/auth0/management/refresh_tokens/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetRefreshTokenResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve refresh token information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.refresh_tokens.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID refresh token to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refresh_tokens.<a href="src/auth0/management/refresh_tokens/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a refresh token by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.refresh_tokens.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the refresh token to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refresh_tokens.<a href="src/auth0/management/refresh_tokens/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateRefreshTokenResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a refresh token by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.refresh_tokens.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the refresh token to update.
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_metadata:** `typing.Optional[RefreshTokenMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ResourceServers
<details><summary><code>client.resource_servers.<a href="src/auth0/management/resource_servers/client.py">list</a>(...) -&gt; AsyncPager[ResourceServer, ListResourceServerOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all APIs associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.resource_servers.list(
    page=1,
    per_page=1,
    include_totals=True,
    include_fields=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifiers:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — An optional filter on the resource server identifier. Must be URL encoded and may be specified multiple times (max 10).<br /><b>e.g.</b> <i>../resource-servers?identifiers=id1&identifiers=id2</i>
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_servers.<a href="src/auth0/management/resource_servers/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateResourceServerResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new API associated with your tenant. Note that all new APIs must be registered with Auth0. For more information, read <a href="https://www.auth0.com/docs/get-started/apis"> APIs</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.resource_servers.create(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique identifier for the API used as the audience parameter on authorization calls. Can not be changed once set.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Friendly name for this resource server. Can not contain `<` or `>` characters.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Sequence[ResourceServerScope]]` — List of permissions (scopes) that this API uses.
    
</dd>
</dl>

<dl>
<dd>

**signing_alg:** `typing.Optional[SigningAlgorithmEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**signing_secret:** `typing.Optional[str]` — Secret used to sign tokens when using symmetric algorithms (HS256).
    
</dd>
</dl>

<dl>
<dd>

**allow_offline_access:** `typing.Optional[bool]` — Whether refresh tokens can be issued for this API (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**token_lifetime:** `typing.Optional[int]` — Expiration value (in seconds) for access tokens issued for this API from the token endpoint.
    
</dd>
</dl>

<dl>
<dd>

**token_dialect:** `typing.Optional[ResourceServerTokenDialectSchemaEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_consent_for_verifiable_first_party_clients:** `typing.Optional[bool]` — Whether to skip user consent for applications flagged as first party (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**enforce_policies:** `typing.Optional[bool]` — Whether to enforce authorization policies (true) or to ignore them (false).
    
</dd>
</dl>

<dl>
<dd>

**token_encryption:** `typing.Optional[ResourceServerTokenEncryption]` 
    
</dd>
</dl>

<dl>
<dd>

**consent_policy:** `typing.Optional[ResourceServerConsentPolicyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization_details:** `typing.Optional[typing.Sequence[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**proof_of_possession:** `typing.Optional[ResourceServerProofOfPossession]` 
    
</dd>
</dl>

<dl>
<dd>

**subject_type_authorization:** `typing.Optional[ResourceServerSubjectTypeAuthorization]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_servers.<a href="src/auth0/management/resource_servers/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetResourceServerResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve <a href="https://auth0.com/docs/apis">API</a> details with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.resource_servers.get(
    id="id",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID or audience of the resource server to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_servers.<a href="src/auth0/management/resource_servers/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing API by ID. For more information, read <a href="https://www.auth0.com/docs/get-started/apis/api-settings">API Settings</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.resource_servers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID or the audience of the resource server to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource_servers.<a href="src/auth0/management/resource_servers/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateResourceServerResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change an existing API setting by resource server ID. For more information, read <a href="https://www.auth0.com/docs/get-started/apis/api-settings">API Settings</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.resource_servers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID or audience of the resource server to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Friendly name for this resource server. Can not contain `<` or `>` characters.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Sequence[ResourceServerScope]]` — List of permissions (scopes) that this API uses.
    
</dd>
</dl>

<dl>
<dd>

**signing_alg:** `typing.Optional[SigningAlgorithmEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**signing_secret:** `typing.Optional[str]` — Secret used to sign tokens when using symmetric algorithms (HS256).
    
</dd>
</dl>

<dl>
<dd>

**skip_consent_for_verifiable_first_party_clients:** `typing.Optional[bool]` — Whether to skip user consent for applications flagged as first party (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**allow_offline_access:** `typing.Optional[bool]` — Whether refresh tokens can be issued for this API (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**token_lifetime:** `typing.Optional[int]` — Expiration value (in seconds) for access tokens issued for this API from the token endpoint.
    
</dd>
</dl>

<dl>
<dd>

**token_dialect:** `typing.Optional[ResourceServerTokenDialectSchemaEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**enforce_policies:** `typing.Optional[bool]` — Whether authorization policies are enforced (true) or not enforced (false).
    
</dd>
</dl>

<dl>
<dd>

**token_encryption:** `typing.Optional[ResourceServerTokenEncryption]` 
    
</dd>
</dl>

<dl>
<dd>

**consent_policy:** `typing.Optional[ResourceServerConsentPolicyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization_details:** `typing.Optional[typing.Sequence[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**proof_of_possession:** `typing.Optional[ResourceServerProofOfPossession]` 
    
</dd>
</dl>

<dl>
<dd>

**subject_type_authorization:** `typing.Optional[ResourceServerSubjectTypeAuthorization]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/auth0/management/roles/client.py">list</a>(...) -&gt; AsyncPager[Role, ListRolesOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list of user roles created in your tenant.

<b>Note</b>: The returned list does not include standard roles available for tenant members, such as Admin or Support Access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.roles.list(
    per_page=1,
    page=1,
    include_totals=True,
    name_filter="name_filter",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**name_filter:** `typing.Optional[str]` — Optional filter on name (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/auth0/management/roles/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateRoleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a user role for <a href="https://auth0.com/docs/manage-users/access-control/rbac">Role-Based Access Control</a>.

<b>Note</b>: New roles are not associated with any permissions by default. To assign existing permissions to your role, review Associate Permissions with a Role. To create new permissions, review Add API Permissions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the role.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the role.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/auth0/management/roles/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetRoleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a specific <a href="https://auth0.com/docs/manage-users/access-control/rbac">user role</a> specified by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/auth0/management/roles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific <a href="https://auth0.com/docs/manage-users/access-control/rbac">user role</a> from your tenant. Once deleted, it is removed from any user who was previously assigned that role. This action cannot be undone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/auth0/management/roles/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateRoleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the details of a specific <a href="https://auth0.com/docs/manage-users/access-control/rbac">user role</a> specified by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this role.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of this role.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rules
<details><summary><code>client.rules.<a href="src/auth0/management/rules/client.py">list</a>(...) -&gt; AsyncPager[Rule, ListRulesOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a filtered list of <a href="https://auth0.com/docs/rules">rules</a>. Accepts a list of fields to include or exclude.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.rules.list(
    page=1,
    per_page=1,
    include_totals=True,
    enabled=True,
    fields="fields",
    include_fields=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Optional filter on whether a rule is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules.<a href="src/auth0/management/rules/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateRuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a <a href="https://auth0.com/docs/rules#create-a-new-rule-using-the-management-api">new rule</a>.

Note: Changing a rule's stage of execution from the default <code>login_success</code> can change the rule's function signature to have user omitted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules.create(
    name="name",
    script="script",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of this rule.
    
</dd>
</dl>

<dl>
<dd>

**script:** `str` — Code to be executed when this rule runs.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[float]` — Order that this rule should execute in relative to other rules. Lower-valued rules execute first.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the rule is enabled (true), or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules.<a href="src/auth0/management/rules/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetRuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve <a href="https://auth0.com/docs/rules">rule</a> details. Accepts a list of fields to include or exclude in the result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules.get(
    id="id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the rule to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules.<a href="src/auth0/management/rules/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the rule to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules.<a href="src/auth0/management/rules/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateRuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the rule to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Optional[str]` — Code to be executed when this rule runs.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this rule.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[float]` — Order that this rule should execute in relative to other rules. Lower-valued rules execute first.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the rule is enabled (true), or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RulesConfigs
<details><summary><code>client.rules_configs.<a href="src/auth0/management/rules_configs/client.py">list</a>() -&gt; AsyncHttpResponse[typing.List[RulesConfig]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve rules config variable keys.

    Note: For security, config variable values cannot be retrieved outside rule execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules_configs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules_configs.<a href="src/auth0/management/rules_configs/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetRulesConfigResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a rules config variable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules_configs.set(
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the rules config variable to set (max length: 127 characters).
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value for a rules config variable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rules_configs.<a href="src/auth0/management/rules_configs/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a rules config variable identified by its key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.rules_configs.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the rules config variable to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SelfServiceProfiles
<details><summary><code>client.self_service_profiles.<a href="src/auth0/management/self_service_profiles/client.py">list</a>(...) -&gt; AsyncPager[SelfServiceProfile, ListSelfServiceProfilesPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves self-service profiles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.self_service_profiles.list(
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.<a href="src/auth0/management/self_service_profiles/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateSelfServiceProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a self-service profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the self-service Profile.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the self-service Profile.
    
</dd>
</dl>

<dl>
<dd>

**branding:** `typing.Optional[SelfServiceProfileBrandingProperties]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_strategies:** `typing.Optional[typing.Sequence[SelfServiceProfileAllowedStrategyEnum]]` — List of IdP strategies that will be shown to users during the Self-Service SSO flow. Possible values: [`oidc`, `samlp`, `waad`, `google-apps`, `adfs`, `okta`, `auth0-samlp`, `okta-samlp`, `keycloak-samlp`, `pingfederate`]
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `typing.Optional[typing.Sequence[SelfServiceProfileUserAttribute]]` — List of attributes to be mapped that will be shown to the user during the SS-SSO flow.
    
</dd>
</dl>

<dl>
<dd>

**user_attribute_profile_id:** `typing.Optional[str]` — ID of the user-attribute-profile to associate with this self-service profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.<a href="src/auth0/management/self_service_profiles/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetSelfServiceProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a self-service profile by Id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.<a href="src/auth0/management/self_service_profiles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a self-service profile by Id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.<a href="src/auth0/management/self_service_profiles/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateSelfServiceProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a self-service profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the self-service Profile.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[SelfServiceProfileDescription]` 
    
</dd>
</dl>

<dl>
<dd>

**branding:** `typing.Optional[SelfServiceProfileBranding]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_strategies:** `typing.Optional[typing.Sequence[SelfServiceProfileAllowedStrategyEnum]]` — List of IdP strategies that will be shown to users during the Self-Service SSO flow. Possible values: [`oidc`, `samlp`, `waad`, `google-apps`, `adfs`, `okta`, `auth0-samlp`, `okta-samlp`, `keycloak-samlp`, `pingfederate`]
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `typing.Optional[SelfServiceProfileUserAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**user_attribute_profile_id:** `typing.Optional[str]` — ID of the user-attribute-profile to associate with this self-service profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sessions
<details><summary><code>client.sessions.<a href="src/auth0/management/sessions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetSessionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve session information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.sessions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of session to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/auth0/management/sessions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a session by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.sessions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the session to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/auth0/management/sessions/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateSessionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update session information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.sessions.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the session to update.
    
</dd>
</dl>

<dl>
<dd>

**session_metadata:** `typing.Optional[SessionMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/auth0/management/sessions/client.py">revoke</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes a session by ID and all associated refresh tokens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.sessions.revoke(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the session to revoke.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Stats
<details><summary><code>client.stats.<a href="src/auth0/management/stats/client.py">get_active_users_count</a>() -&gt; AsyncHttpResponse[GetActiveUsersCountStatsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the number of active users that logged in during the last 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.stats.get_active_users_count()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.stats.<a href="src/auth0/management/stats/client.py">get_daily</a>(...) -&gt; AsyncHttpResponse[typing.List[DailyStats]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the number of logins, signups and breached-password detections (subscription required) that occurred each day within a specified date range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.stats.get_daily(
    from_="from",
    to="to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional first day of the date range (inclusive) in YYYYMMDD format.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Optional last day of the date range (inclusive) in YYYYMMDD format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SupplementalSignals
<details><summary><code>client.supplemental_signals.<a href="src/auth0/management/supplemental_signals/client.py">get</a>() -&gt; AsyncHttpResponse[GetSupplementalSignalsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the supplemental signals configuration for a tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.supplemental_signals.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.supplemental_signals.<a href="src/auth0/management/supplemental_signals/client.py">patch</a>(...) -&gt; AsyncHttpResponse[PatchSupplementalSignalsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the supplemental signals configuration for a tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.supplemental_signals.patch(
    akamai_enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**akamai_enabled:** `bool` — Indicates if incoming Akamai Headers should be processed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tickets
<details><summary><code>client.tickets.<a href="src/auth0/management/tickets/client.py">verify_email</a>(...) -&gt; AsyncHttpResponse[VerifyEmailTicketResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an email verification ticket for a given user. An email verification ticket is a generated URL that the user can consume to verify their email address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.tickets.verify_email(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — user_id of for whom the ticket should be created.
    
</dd>
</dl>

<dl>
<dd>

**result_url:** `typing.Optional[str]` — URL the user will be redirected to in the classic Universal Login experience once the ticket is used. Cannot be specified when using client_id or organization_id.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — ID of the client (application). If provided for tenants using the New Universal Login experience, the email template and UI displays application details, and the user is prompted to redirect to the application's <a target='' href='https://auth0.com/docs/authenticate/login/auth0-universal-login/configure-default-login-routes#completing-the-password-reset-flow'>default login route</a> after the ticket is used. client_id is required to use the <a target='' href='https://auth0.com/docs/customize/actions/flows-and-triggers/post-change-password-flow'>Password Reset Post Challenge</a> trigger.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — (Optional) Organization ID – the ID of the Organization. If provided, organization parameters will be made available to the email template and organization branding will be applied to the prompt. In addition, the redirect link in the prompt will include organization_id and organization_name query string parameters.
    
</dd>
</dl>

<dl>
<dd>

**ttl_sec:** `typing.Optional[int]` — Number of seconds for which the ticket is valid before expiration. If unspecified or set to 0, this value defaults to 432000 seconds (5 days).
    
</dd>
</dl>

<dl>
<dd>

**include_email_in_redirect:** `typing.Optional[bool]` — Whether to include the email address as part of the returnUrl in the reset_email (true), or not (false).
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/auth0/management/tickets/client.py">change_password</a>(...) -&gt; AsyncHttpResponse[ChangePasswordTicketResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a password change ticket for a given user. A password change ticket is a generated URL that the user can consume to start a reset password flow.

Note: This endpoint does not verify the given user’s identity. If you call this endpoint within your application, you must design your application to verify the user’s identity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.tickets.change_password()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**result_url:** `typing.Optional[str]` — URL the user will be redirected to in the classic Universal Login experience once the ticket is used. Cannot be specified when using client_id or organization_id.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — user_id of for whom the ticket should be created.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — ID of the client (application). If provided for tenants using the New Universal Login experience, the email template and UI displays application details, and the user is prompted to redirect to the application's <a target='' href='https://auth0.com/docs/authenticate/login/auth0-universal-login/configure-default-login-routes#completing-the-password-reset-flow'>default login route</a> after the ticket is used. client_id is required to use the <a target='' href='https://auth0.com/docs/customize/actions/flows-and-triggers/post-change-password-flow'>Password Reset Post Challenge</a> trigger.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — (Optional) Organization ID – the ID of the Organization. If provided, organization parameters will be made available to the email template and organization branding will be applied to the prompt. In addition, the redirect link in the prompt will include organization_id and organization_name query string parameters.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — ID of the connection. If provided, allows the user to be specified using email instead of user_id. If you set this value, you must also send the email parameter. You cannot send user_id when specifying a connection_id.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the user for whom the tickets should be created. Requires the connection_id parameter. Cannot be specified when using user_id.
    
</dd>
</dl>

<dl>
<dd>

**ttl_sec:** `typing.Optional[int]` — Number of seconds for which the ticket is valid before expiration. If unspecified or set to 0, this value defaults to 432000 seconds (5 days).
    
</dd>
</dl>

<dl>
<dd>

**mark_email_as_verified:** `typing.Optional[bool]` — Whether to set the email_verified attribute to true (true) or whether it should not be updated (false).
    
</dd>
</dl>

<dl>
<dd>

**include_email_in_redirect:** `typing.Optional[bool]` — Whether to include the email address as part of the returnUrl in the reset_email (true), or not (false).
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[ChangePasswordTicketIdentity]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TokenExchangeProfiles
<details><summary><code>client.token_exchange_profiles.<a href="src/auth0/management/token_exchange_profiles/client.py">list</a>(...) -&gt; AsyncPager[
    TokenExchangeProfileResponseContent, ListTokenExchangeProfileResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all Token Exchange Profiles available in your tenant.

By using this feature, you agree to the applicable Free Trial terms in <a href="https://www.okta.com/legal/">Okta’s Master Subscription Agreement</a>. It is your responsibility to securely validate the user’s subject_token. See <a href="https://auth0.com/docs/authenticate/custom-token-exchange">User Guide</a> for more details.

This endpoint supports Checkpoint pagination. To search by checkpoint, use the following parameters:
<ul>
<li><code>from</code>: Optional id from which to start selection.</li>
<li><code>take</code>: The total amount of entries to retrieve when using the from parameter. Defaults to 50.</li>
</ul>

<b>Note</b>: The first time you call this endpoint using checkpoint pagination, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no pages are remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.token_exchange_profiles.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_exchange_profiles.<a href="src/auth0/management/token_exchange_profiles/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateTokenExchangeProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Token Exchange Profile within your tenant.

By using this feature, you agree to the applicable Free Trial terms in <a href="https://www.okta.com/legal/">Okta’s Master Subscription Agreement</a>. It is your responsibility to securely validate the user’s subject_token. See <a href="https://auth0.com/docs/authenticate/custom-token-exchange">User Guide</a> for more details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.token_exchange_profiles.create(
    name="name",
    subject_token_type="subject_token_type",
    action_id="action_id",
    type="custom_authentication",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Friendly name of this profile.
    
</dd>
</dl>

<dl>
<dd>

**subject_token_type:** `str` — Subject token type for this profile. When receiving a token exchange request on the Authentication API, the corresponding token exchange profile with a matching subject_token_type will be executed. This must be a URI.
    
</dd>
</dl>

<dl>
<dd>

**action_id:** `str` — The ID of the Custom Token Exchange action to execute for this profile, in order to validate the subject_token. The action must use the custom-token-exchange trigger.
    
</dd>
</dl>

<dl>
<dd>

**type:** `TokenExchangeProfileTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_exchange_profiles.<a href="src/auth0/management/token_exchange_profiles/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetTokenExchangeProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single Token Exchange Profile specified by ID.

By using this feature, you agree to the applicable Free Trial terms in <a href="https://www.okta.com/legal/">Okta’s Master Subscription Agreement</a>. It is your responsibility to securely validate the user’s subject_token. See <a href="https://auth0.com/docs/authenticate/custom-token-exchange">User Guide</a> for more details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.token_exchange_profiles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Token Exchange Profile to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_exchange_profiles.<a href="src/auth0/management/token_exchange_profiles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Token Exchange Profile within your tenant.

By using this feature, you agree to the applicable Free Trial terms in <a href="https://www.okta.com/legal/">Okta's Master Subscription Agreement</a>. It is your responsibility to securely validate the user's subject_token. See <a href="https://auth0.com/docs/authenticate/custom-token-exchange">User Guide</a> for more details.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.token_exchange_profiles.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Token Exchange Profile to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token_exchange_profiles.<a href="src/auth0/management/token_exchange_profiles/client.py">update</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Token Exchange Profile within your tenant.

By using this feature, you agree to the applicable Free Trial terms in <a href="https://www.okta.com/legal/">Okta's Master Subscription Agreement</a>. It is your responsibility to securely validate the user's subject_token. See <a href="https://auth0.com/docs/authenticate/custom-token-exchange">User Guide</a> for more details.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.token_exchange_profiles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Token Exchange Profile to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Friendly name of this profile.
    
</dd>
</dl>

<dl>
<dd>

**subject_token_type:** `typing.Optional[str]` — Subject token type for this profile. When receiving a token exchange request on the Authentication API, the corresponding token exchange profile with a matching subject_token_type will be executed. This must be a URI.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserAttributeProfiles
<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">list</a>(...) -&gt; AsyncPager[
    UserAttributeProfile, ListUserAttributeProfilesPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of User Attribute Profiles. This endpoint supports Checkpoint pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.user_attribute_profiles.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 5.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateUserAttributeProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single User Attribute Profile specified by ID. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, UserAttributeProfileUserAttributeAdditionalProperties

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.create(
    name="name",
    user_attributes={
        "key": UserAttributeProfileUserAttributeAdditionalProperties(
            description="description",
            label="label",
            profile_required=True,
            auth_0_mapping="auth0_mapping",
        )
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `UserAttributeProfileName` 
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `UserAttributeProfileUserAttributes` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[UserAttributeProfileUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">list_templates</a>() -&gt; AsyncHttpResponse[ListUserAttributeProfileTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of User Attribute Profile Templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.list_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">get_template</a>(...) -&gt; AsyncHttpResponse[GetUserAttributeProfileTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a User Attribute Profile Template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.get_template(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user-attribute-profile-template to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetUserAttributeProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single User Attribute Profile specified by ID. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user-attribute-profile to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single User Attribute Profile specified by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user-attribute-profile to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_attribute_profiles.<a href="src/auth0/management/user_attribute_profiles/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateUserAttributeProfileResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a specific User attribute profile, such as name, user_id and user_attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_attribute_profiles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user attribute profile to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[UserAttributeProfileName]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[UserAttributeProfilePatchUserId]` 
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `typing.Optional[UserAttributeProfileUserAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserBlocks
<details><summary><code>client.user_blocks.<a href="src/auth0/management/user_blocks/client.py">list_by_identifier</a>(...) -&gt; AsyncHttpResponse[ListUserBlocksByIdentifierResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all <a href="https://auth0.com/docs/secure/attack-protection/brute-force-protection">Brute-force Protection</a> blocks for a user with the given identifier (username, phone number, or email).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_blocks.list_by_identifier(
    identifier="identifier",
    consider_brute_force_enablement=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Should be any of a username, phone number, or email.
    
</dd>
</dl>

<dl>
<dd>

**consider_brute_force_enablement:** `typing.Optional[bool]` 


          If true and Brute Force Protection is enabled and configured to block logins, will return a list of blocked IP addresses.
          If true and Brute Force Protection is disabled, will return an empty list.
        
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_blocks.<a href="src/auth0/management/user_blocks/client.py">delete_by_identifier</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove all <a href="https://auth0.com/docs/secure/attack-protection/brute-force-protection">Brute-force Protection</a> blocks for the user with the given identifier (username, phone number, or email).

Note: This endpoint does not unblock users that were <a href="https://auth0.com/docs/user-profile#block-and-unblock-a-user">blocked by a tenant administrator</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_blocks.delete_by_identifier(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Should be any of a username, phone number, or email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_blocks.<a href="src/auth0/management/user_blocks/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListUserBlocksResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all <a href="https://auth0.com/docs/secure/attack-protection/brute-force-protection">Brute-force Protection</a> blocks for the user with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_blocks.list(
    id="id",
    consider_brute_force_enablement=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — user_id of the user blocks to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**consider_brute_force_enablement:** `typing.Optional[bool]` 


          If true and Brute Force Protection is enabled and configured to block logins, will return a list of blocked IP addresses.
          If true and Brute Force Protection is disabled, will return an empty list.
        
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_blocks.<a href="src/auth0/management/user_blocks/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove all <a href="https://auth0.com/docs/secure/attack-protection/brute-force-protection">Brute-force Protection</a> blocks for the user with the given ID.

Note: This endpoint does not unblock users that were <a href="https://auth0.com/docs/user-profile#block-and-unblock-a-user">blocked by a tenant administrator</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.user_blocks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The user_id of the user to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">list</a>(...) -&gt; AsyncPager[UserResponseSchema, ListUsersOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of users. It is possible to:

- Specify a search criteria for users
- Sort the users to be returned
- Select the fields to be returned
- Specify the number of users to retrieve per page and the page index
 <!-- only v3 is available -->
The <code>q</code> query parameter can be used to get users that match the specified criteria <a href="https://auth0.com/docs/users/search/v3/query-syntax">using query string syntax.</a>

<a href="https://auth0.com/docs/users/search/v3">Learn more about searching for users.</a>

Read about <a href="https://auth0.com/docs/users/search/best-practices">best practices</a> when working with the API endpoints for retrieving users.

Auth0 limits the number of users you can return. If you exceed this threshold, please redefine your search, use the <a href="https://auth0.com/docs/api/management/v2#!/Jobs/post_users_exports">export job</a>, or the <a href="https://auth0.com/docs/extensions/user-import-export">User Import / Export</a> extension.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.list(
    page=1,
    per_page=1,
    include_totals=True,
    sort="sort",
    connection="connection",
    fields="fields",
    include_fields=True,
    q="q",
    search_engine="v1",
    primary_order=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Use <code>field:order</code> where order is <code>1</code> for ascending and <code>-1</code> for descending. e.g. <code>created_at:1</code>
    
</dd>
</dl>

<dl>
<dd>

**connection:** `typing.Optional[str]` — Connection filter. Only applies when using <code>search_engine=v1</code>. To filter by connection with <code>search_engine=v2|v3</code>, use <code>q=identities.connection:"connection_name"</code>
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Query in <a target='_new' href ='http://www.lucenetutorial.com/lucene-query-syntax.html'>Lucene query string syntax</a>. Some query types cannot be used on metadata fields, for details see <a href='https://auth0.com/docs/users/search/v3/query-syntax#searchable-fields'>Searchable Fields</a>.
    
</dd>
</dl>

<dl>
<dd>

**search_engine:** `typing.Optional[SearchEngineVersionsEnum]` — The version of the search engine
    
</dd>
</dl>

<dl>
<dd>

**primary_order:** `typing.Optional[bool]` — If true (default), results are returned in a deterministic order. If false, results may be returned in a non-deterministic order, which can enhance performance for complex queries targeting a small number of users. Set to false only when consistent ordering and pagination is not required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateUserResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user for a given <a href="https://auth0.com/docs/connections/database">database</a> or <a href="https://auth0.com/docs/connections/passwordless">passwordless</a> connection.

Note: <code>connection</code> is required but other parameters such as <code>email</code> and <code>password</code> are dependent upon the type of connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.create(
    connection="connection",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection:** `str` — Name of the connection this user should be created in.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The user's email.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — The user's phone number (following the E.164 recommendation).
    
</dd>
</dl>

<dl>
<dd>

**user_metadata:** `typing.Optional[UserMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**blocked:** `typing.Optional[bool]` — Whether this user was blocked by an administrator (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**email_verified:** `typing.Optional[bool]` — Whether this email address is verified (true) or unverified (false). User will receive a verification email after creation if `email_verified` is false or not specified
    
</dd>
</dl>

<dl>
<dd>

**phone_verified:** `typing.Optional[bool]` — Whether this phone number has been verified (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**app_metadata:** `typing.Optional[AppMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — The user's given name(s).
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — The user's family name(s).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The user's full name.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — The user's nickname.
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — A URI pointing to the user's picture.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — The external user's id provided by the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Initial password for this user. Only valid for auth0 connection strategy.
    
</dd>
</dl>

<dl>
<dd>

**verify_email:** `typing.Optional[bool]` — Whether the user will receive a verification email after creation (true) or no email (false). Overrides behavior of `email_verified` parameter.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — The user's username. Only valid if the connection requires a username.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">list_users_by_email</a>(...) -&gt; AsyncHttpResponse[typing.List[UserResponseSchema]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find users by email. If Auth0 is the identity provider (idP), the email address associated with a user is saved in lower case, regardless of how you initially provided it. 

For example, if you register a user as JohnSmith@example.com, Auth0 saves the user's email as johnsmith@example.com. 

Therefore, when using this endpoint, make sure that you are searching for users via email addresses using the correct case.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.list_users_by_email(
    fields="fields",
    include_fields=True,
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email address to search for (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetUserResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve user details. A list of fields to include or exclude may also be specified. For more information, see <a href="https://auth0.com/docs/manage-users/user-search/retrieve-users-with-get-users-endpoint">Retrieve Users with the Get Users Endpoint</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.get(
    id="id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a user by user ID. This action cannot be undone. For Auth0 Dashboard instructions, see <a href="https://auth0.com/docs/manage-users/user-accounts/delete-users">Delete Users</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateUserResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a user.

These are the attributes that can be updated at the root level:

<ul>
    <li>app_metadata</li>
    <li>blocked</li>
    <li>email</li>
    <li>email_verified</li>
    <li>family_name</li>
    <li>given_name</li>
    <li>name</li>
    <li>nickname</li>
    <li>password</li>
    <li>phone_number</li>
    <li>phone_verified</li>
    <li>picture</li>
    <li>username</li>
    <li>user_metadata</li>
    <li>verify_email</li>
</ul>

Some considerations:
<ul>
    <li>The properties of the new object will replace the old ones.</li>
    <li>The metadata fields are an exception to this rule (<code>user_metadata</code> and <code>app_metadata</code>). These properties are merged instead of being replaced but be careful, the merge only occurs on the first level.</li>
    <li>If you are updating <code>email</code>, <code>email_verified</code>, <code>phone_number</code>, <code>phone_verified</code>, <code>username</code> or <code>password</code> of a secondary identity, you need to specify the <code>connection</code> property too.</li>
    <li>If you are updating <code>email</code> or <code>phone_number</code> you can specify, optionally, the <code>client_id</code> property.</li>
    <li>Updating <code>email_verified</code> is not supported for enterprise and passwordless sms connections.</li>
    <li>Updating the <code>blocked</code> to <code>false</code> does not affect the user's blocked state from an excessive amount of incorrectly provided credentials. Use the "Unblock a user" endpoint from the "User Blocks" API to change the user's state.</li>
    <li>Supported attributes can be unset by supplying <code>null</code> as the value.</li>
</ul>

<h5>Updating a field (non-metadata property)</h5>
To mark the email address of a user as verified, the body to send should be:
<pre><code>{ "email_verified": true }</code></pre>

<h5>Updating a user metadata root property</h5>Let's assume that our test user has the following <code>user_metadata</code>:
<pre><code>{ "user_metadata" : { "profileCode": 1479 } }</code></pre>

To add the field <code>addresses</code> the body to send should be:
<pre><code>{ "user_metadata" : { "addresses": {"work_address": "100 Industrial Way"} }}</code></pre>

The modified object ends up with the following <code>user_metadata</code> property:<pre><code>{
  "user_metadata": {
    "profileCode": 1479,
    "addresses": { "work_address": "100 Industrial Way" }
  }
}</code></pre>

<h5>Updating an inner user metadata property</h5>If there's existing user metadata to which we want to add  <code>"home_address": "742 Evergreen Terrace"</code> (using the <code>addresses</code> property) we should send the whole <code>addresses</code> object. Since this is a first-level object, the object will be merged in, but its own properties will not be. The body to send should be:
<pre><code>{
  "user_metadata": {
    "addresses": {
      "work_address": "100 Industrial Way",
      "home_address": "742 Evergreen Terrace"
    }
  }
}</code></pre>

The modified object ends up with the following <code>user_metadata</code> property:
<pre><code>{
  "user_metadata": {
    "profileCode": 1479,
    "addresses": {
      "work_address": "100 Industrial Way",
      "home_address": "742 Evergreen Terrace"
    }
  }
}</code></pre>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to update.
    
</dd>
</dl>

<dl>
<dd>

**blocked:** `typing.Optional[bool]` — Whether this user was blocked by an administrator (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**email_verified:** `typing.Optional[bool]` — Whether this email address is verified (true) or unverified (false). If set to false the user will not receive a verification email unless `verify_email` is set to true.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of this user.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — The user's phone number (following the E.164 recommendation).
    
</dd>
</dl>

<dl>
<dd>

**phone_verified:** `typing.Optional[bool]` — Whether this phone number has been verified (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**user_metadata:** `typing.Optional[UserMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**app_metadata:** `typing.Optional[AppMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — Given name/first name/forename of this user.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — Family name/last name/surname of this user.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this user.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — Preferred nickname or alias of this user.
    
</dd>
</dl>

<dl>
<dd>

**picture:** `typing.Optional[str]` — URL to picture, photo, or avatar of this user.
    
</dd>
</dl>

<dl>
<dd>

**verify_email:** `typing.Optional[bool]` — Whether this user will receive a verification email after creation (true) or no email (false). Overrides behavior of `email_verified` parameter.
    
</dd>
</dl>

<dl>
<dd>

**verify_phone_number:** `typing.Optional[bool]` — Whether this user will receive a text after changing the phone number (true) or no text (false). Only valid when changing phone number for SMS connections.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — New password for this user. Only valid for database connections.
    
</dd>
</dl>

<dl>
<dd>

**connection:** `typing.Optional[str]` — Name of the connection to target for this user update.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Auth0 client ID. Only valid when updating email address.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — The user's username. Only valid if the connection requires a username.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">regenerate_recovery_code</a>(...) -&gt; AsyncHttpResponse[RegenerateUsersRecoveryCodeResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an existing multi-factor authentication (MFA) <a href="https://auth0.com/docs/secure/multi-factor-authentication/reset-user-mfa">recovery code</a> and generate a new one. If a user cannot access the original device or account used for MFA enrollment, they can use a recovery code to authenticate. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.regenerate_recovery_code(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to regenerate a multi-factor authentication recovery code for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/auth0/management/users/client.py">revoke_access</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes selected resources related to a user (sessions, refresh tokens, ...).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.revoke_access(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — ID of the session to revoke.
    
</dd>
</dl>

<dl>
<dd>

**preserve_refresh_tokens:** `typing.Optional[bool]` — Whether to preserve the refresh tokens associated with the session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Versions
<details><summary><code>client.actions.versions.<a href="src/auth0/management/actions/versions/client.py">list</a>(...) -&gt; AsyncPager[ActionVersion, ListActionVersionsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all of an action's versions. An action version is created whenever an action is deployed. An action version is immutable, once created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.versions.list(
    action_id="actionId",
    page=1,
    per_page=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — The ID of the action.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Use this field to request a specific page of the list results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — This field specify the maximum number of results to be returned by the server. 20 by default
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.versions.<a href="src/auth0/management/actions/versions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetActionVersionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific version of an action. An action version is created whenever an action is deployed. An action version is immutable, once created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.versions.get(
    action_id="actionId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — The ID of the action.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of the action version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.versions.<a href="src/auth0/management/actions/versions/client.py">deploy</a>(...) -&gt; AsyncHttpResponse[DeployActionVersionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs the equivalent of a roll-back of an action to an earlier, specified version. Creates a new, deployed action version that is identical to the specified version. If this action is currently bound to a trigger, the system will begin executing the newly-created version immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, DeployActionVersionRequestContent

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.versions.deploy(
    action_id="actionId",
    id="id",
    request=DeployActionVersionRequestContent(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — The ID of an action.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of an action version.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[DeployActionVersionRequestContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Executions
<details><summary><code>client.actions.executions.<a href="src/auth0/management/actions/executions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetActionExecutionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about a specific execution of a trigger. Relevant execution IDs will be included in tenant logs generated as part of that authentication flow. Executions will only be stored for 10 days after their creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.executions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the execution to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Modules
<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">list</a>(...) -&gt; AsyncPager[ActionModuleListItem, GetActionModulesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all Actions Modules with optional filtering and totals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.modules.list(
    page=1,
    per_page=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Paging is disabled if parameter not sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateActionModuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Actions Module for reusable code across actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.create(
    name="name",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the action module.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — The source code of the action module.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Sequence[ActionModuleSecretRequest]]` — The secrets to associate with the action module.
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[typing.Sequence[ActionModuleDependencyRequest]]` — The npm dependencies of the action module.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — The API version of the module.
    
</dd>
</dl>

<dl>
<dd>

**publish:** `typing.Optional[bool]` — Whether to publish the module immediately after creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetActionModuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific Actions Module by its unique identifier.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the action module to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an Actions Module. This will fail if the module is still in use by any actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the Actions Module to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateActionModuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties of an existing Actions Module, such as code, dependencies, or secrets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the action module to update.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The source code of the action module.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Sequence[ActionModuleSecretRequest]]` — The secrets to associate with the action module.
    
</dd>
</dl>

<dl>
<dd>

**dependencies:** `typing.Optional[typing.Sequence[ActionModuleDependencyRequest]]` — The npm dependencies of the action module.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">list_actions</a>(...) -&gt; AsyncPager[ActionModuleAction, GetActionModuleActionsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all actions that are using a specific Actions Module, showing which deployed action versions reference this Actions Module.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.modules.list_actions(
    id="id",
    page=1,
    per_page=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique ID of the module.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.<a href="src/auth0/management/actions/modules/client.py">rollback</a>(...) -&gt; AsyncHttpResponse[RollbackActionModuleResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rolls back an Actions Module's draft to a previously created version. This action copies the code, dependencies, and secrets from the specified version into the current draft.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.rollback(
    id="id",
    module_version_id="module_version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique ID of the module to roll back.
    
</dd>
</dl>

<dl>
<dd>

**module_version_id:** `str` — The unique ID of the module version to roll back to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Triggers
<details><summary><code>client.actions.triggers.<a href="src/auth0/management/actions/triggers/client.py">list</a>() -&gt; AsyncHttpResponse[ListActionTriggersResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the set of triggers currently available within actions. A trigger is an extensibility point to which actions can be bound.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.triggers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Modules Versions
<details><summary><code>client.actions.modules.versions.<a href="src/auth0/management/actions/modules/versions/client.py">list</a>(...) -&gt; AsyncPager[ActionModuleVersion, GetActionModuleVersionsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all published versions of a specific Actions Module.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.modules.versions.list(
    id="id",
    page=1,
    per_page=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique ID of the module.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Use this field to request a specific page of the list results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — The maximum number of results to be returned by the server in a single response. 20 by default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.versions.<a href="src/auth0/management/actions/modules/versions/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateActionModuleVersionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new immutable version of an Actions Module from the current draft version. This publishes the draft as a new version that can be referenced by actions, while maintaining the existing draft for continued development.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.versions.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the action module to create a version for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.modules.versions.<a href="src/auth0/management/actions/modules/versions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetActionModuleVersionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific, immutable version of an Actions Module.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.modules.versions.get(
    id="id",
    version_id="versionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique ID of the module.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` — The unique ID of the module version to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions Triggers Bindings
<details><summary><code>client.actions.triggers.bindings.<a href="src/auth0/management/actions/triggers/bindings/client.py">list</a>(...) -&gt; AsyncPager[ActionBinding, ListActionBindingsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the actions that are bound to a trigger. Once an action is created and deployed, it must be attached (i.e. bound) to a trigger so that it will be executed as part of a flow. The list of actions returned reflects the order in which they will be executed during the appropriate flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.actions.triggers.bindings.list(
    trigger_id="triggerId",
    page=1,
    per_page=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `ActionTriggerTypeEnum` — An actions extensibility point.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Use this field to request a specific page of the list results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — The maximum number of results to be returned in a single request. 20 by default
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.triggers.bindings.<a href="src/auth0/management/actions/triggers/bindings/client.py">update_many</a>(...) -&gt; AsyncHttpResponse[UpdateActionBindingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the actions that are bound (i.e. attached) to a trigger. Once an action is created and deployed, it must be attached (i.e. bound) to a trigger so that it will be executed as part of a flow. The order in which the actions are provided will determine the order in which they are executed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.actions.triggers.bindings.update_many(
    trigger_id="triggerId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trigger_id:** `ActionTriggerTypeEnum` — An actions extensibility point.
    
</dd>
</dl>

<dl>
<dd>

**bindings:** `typing.Optional[typing.Sequence[ActionBindingWithRef]]` — The actions that will be bound to this trigger. The order in which they are included will be the order in which they are executed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Anomaly Blocks
<details><summary><code>client.anomaly.blocks.<a href="src/auth0/management/anomaly/blocks/client.py">check_ip</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the given IP address is blocked via the <a href="https://auth0.com/docs/configure/attack-protection/suspicious-ip-throttling">Suspicious IP Throttling</a> due to multiple suspicious attempts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.anomaly.blocks.check_ip(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AnomalyIpFormat` — IP address to check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.anomaly.blocks.<a href="src/auth0/management/anomaly/blocks/client.py">unblock_ip</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a block imposed by <a href="https://auth0.com/docs/configure/attack-protection/suspicious-ip-throttling">Suspicious IP Throttling</a> for the given IP address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.anomaly.blocks.unblock_ip(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AnomalyIpFormat` — IP address to unblock.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttackProtection BotDetection
<details><summary><code>client.attack_protection.bot_detection.<a href="src/auth0/management/attack_protection/bot_detection/client.py">get</a>() -&gt; AsyncHttpResponse[GetBotDetectionSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the Bot Detection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.bot_detection.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attack_protection.bot_detection.<a href="src/auth0/management/attack_protection/bot_detection/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBotDetectionSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the Bot Detection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.bot_detection.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bot_detection_level:** `typing.Optional[BotDetectionLevelEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**challenge_password_policy:** `typing.Optional[BotDetectionChallengePolicyPasswordFlowEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**challenge_passwordless_policy:** `typing.Optional[BotDetectionChallengePolicyPasswordlessFlowEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**challenge_password_reset_policy:** `typing.Optional[BotDetectionChallengePolicyPasswordResetFlowEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**allowlist:** `typing.Optional[BotDetectionAllowlist]` 
    
</dd>
</dl>

<dl>
<dd>

**monitoring_mode_enabled:** `typing.Optional[BotDetectionMonitoringModeEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttackProtection BreachedPasswordDetection
<details><summary><code>client.attack_protection.breached_password_detection.<a href="src/auth0/management/attack_protection/breached_password_detection/client.py">get</a>() -&gt; AsyncHttpResponse[GetBreachedPasswordDetectionSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the Breached Password Detection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.breached_password_detection.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attack_protection.breached_password_detection.<a href="src/auth0/management/attack_protection/breached_password_detection/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBreachedPasswordDetectionSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update details of the Breached Password Detection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.breached_password_detection.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether or not breached password detection is active.
    
</dd>
</dl>

<dl>
<dd>

**shields:** `typing.Optional[typing.Sequence[BreachedPasswordDetectionShieldsEnum]]` 

Action to take when a breached password is detected during a login.
      Possible values: <code>block</code>, <code>user_notification</code>, <code>admin_notification</code>.
    
</dd>
</dl>

<dl>
<dd>

**admin_notification_frequency:** `typing.Optional[
    typing.Sequence[BreachedPasswordDetectionAdminNotificationFrequencyEnum]
]` 

When "admin_notification" is enabled, determines how often email notifications are sent.
        Possible values: <code>immediately</code>, <code>daily</code>, <code>weekly</code>, <code>monthly</code>.
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[BreachedPasswordDetectionMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[BreachedPasswordDetectionStage]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttackProtection BruteForceProtection
<details><summary><code>client.attack_protection.brute_force_protection.<a href="src/auth0/management/attack_protection/brute_force_protection/client.py">get</a>() -&gt; AsyncHttpResponse[GetBruteForceSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the Brute-force Protection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.brute_force_protection.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attack_protection.brute_force_protection.<a href="src/auth0/management/attack_protection/brute_force_protection/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBruteForceSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the Brute-force Protection configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.brute_force_protection.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether or not brute force attack protections are active.
    
</dd>
</dl>

<dl>
<dd>

**shields:** `typing.Optional[typing.Sequence[BruteForceProtectionShieldsEnum]]` 

Action to take when a brute force protection threshold is violated.
        Possible values: <code>block</code>, <code>user_notification</code>.
    
</dd>
</dl>

<dl>
<dd>

**allowlist:** `typing.Optional[typing.Sequence[str]]` — List of trusted IP addresses that will not have attack protection enforced against them.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[BruteForceProtectionModeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**max_attempts:** `typing.Optional[int]` — Maximum number of unsuccessful attempts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttackProtection Captcha
<details><summary><code>client.attack_protection.captcha.<a href="src/auth0/management/attack_protection/captcha/client.py">get</a>() -&gt; AsyncHttpResponse[GetAttackProtectionCaptchaResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the CAPTCHA configuration for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.captcha.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attack_protection.captcha.<a href="src/auth0/management/attack_protection/captcha/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateAttackProtectionCaptchaResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update existing CAPTCHA configuration for your client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.captcha.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**active_provider_id:** `typing.Optional[AttackProtectionCaptchaProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**arkose:** `typing.Optional[AttackProtectionUpdateCaptchaArkose]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_challenge:** `typing.Optional[AttackProtectionCaptchaAuthChallengeRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**hcaptcha:** `typing.Optional[AttackProtectionUpdateCaptchaHcaptcha]` 
    
</dd>
</dl>

<dl>
<dd>

**friendly_captcha:** `typing.Optional[AttackProtectionUpdateCaptchaFriendlyCaptcha]` 
    
</dd>
</dl>

<dl>
<dd>

**recaptcha_enterprise:** `typing.Optional[AttackProtectionUpdateCaptchaRecaptchaEnterprise]` 
    
</dd>
</dl>

<dl>
<dd>

**recaptcha_v_2:** `typing.Optional[AttackProtectionUpdateCaptchaRecaptchaV2]` 
    
</dd>
</dl>

<dl>
<dd>

**simple_captcha:** `typing.Optional[AttackProtectionCaptchaSimpleCaptchaResponseContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AttackProtection SuspiciousIpThrottling
<details><summary><code>client.attack_protection.suspicious_ip_throttling.<a href="src/auth0/management/attack_protection/suspicious_ip_throttling/client.py">get</a>() -&gt; AsyncHttpResponse[GetSuspiciousIpThrottlingSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the Suspicious IP Throttling configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.suspicious_ip_throttling.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attack_protection.suspicious_ip_throttling.<a href="src/auth0/management/attack_protection/suspicious_ip_throttling/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateSuspiciousIpThrottlingSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of the Suspicious IP Throttling configuration of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.attack_protection.suspicious_ip_throttling.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether or not suspicious IP throttling attack protections are active.
    
</dd>
</dl>

<dl>
<dd>

**shields:** `typing.Optional[typing.Sequence[SuspiciousIpThrottlingShieldsEnum]]` 

Action to take when a suspicious IP throttling threshold is violated.
          Possible values: <code>block</code>, <code>admin_notification</code>.
    
</dd>
</dl>

<dl>
<dd>

**allowlist:** `typing.Optional[SuspiciousIpThrottlingAllowlist]` 
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[SuspiciousIpThrottlingStage]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Branding Templates
<details><summary><code>client.branding.templates.<a href="src/auth0/management/branding/templates/client.py">get_universal_login</a>() -&gt; AsyncHttpResponse[GetUniversalLoginTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.templates.get_universal_login()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.templates.<a href="src/auth0/management/branding/templates/client.py">update_universal_login</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the Universal Login branding template.

<p>When <code>content-type</code> header is set to <code>application/json</code>:</p>
<pre>
{
  "template": "&lt;!DOCTYPE html&gt;{% assign resolved_dir = dir | default: "auto" %}&lt;html lang="{{locale}}" dir="{{resolved_dir}}"&gt;&lt;head&gt;{%- auth0:head -%}&lt;/head&gt;&lt;body class="_widget-auto-layout"&gt;{%- auth0:widget -%}&lt;/body&gt;&lt;/html&gt;"
}
</pre>

<p>
  When <code>content-type</code> header is set to <code>text/html</code>:
</p>
<pre>
&lt!DOCTYPE html&gt;
{% assign resolved_dir = dir | default: "auto" %}
&lt;html lang="{{locale}}" dir="{{resolved_dir}}"&gt;
  &lt;head&gt;
    {%- auth0:head -%}
  &lt;/head&gt;
  &lt;body class="_widget-auto-layout"&gt;
    {%- auth0:widget -%}
  &lt;/body&gt;
&lt;/html&gt;
</pre>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.templates.update_universal_login(
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateUniversalLoginTemplateRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.templates.<a href="src/auth0/management/branding/templates/client.py">delete_universal_login</a>() -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.templates.delete_universal_login()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Branding Themes
<details><summary><code>client.branding.themes.<a href="src/auth0/management/branding/themes/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateBrandingThemeResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create branding theme.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    BrandingThemeBorders,
    BrandingThemeColors,
    BrandingThemeFontBodyText,
    BrandingThemeFontButtonsText,
    BrandingThemeFontInputLabels,
    BrandingThemeFontLinks,
    BrandingThemeFonts,
    BrandingThemeFontSubtitle,
    BrandingThemeFontTitle,
    BrandingThemePageBackground,
    BrandingThemeWidget,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.themes.create(
    borders=BrandingThemeBorders(
        button_border_radius=1.1,
        button_border_weight=1.1,
        buttons_style="pill",
        input_border_radius=1.1,
        input_border_weight=1.1,
        inputs_style="pill",
        show_widget_shadow=True,
        widget_border_weight=1.1,
        widget_corner_radius=1.1,
    ),
    colors=BrandingThemeColors(
        body_text="body_text",
        error="error",
        header="header",
        icons="icons",
        input_background="input_background",
        input_border="input_border",
        input_filled_text="input_filled_text",
        input_labels_placeholders="input_labels_placeholders",
        links_focused_components="links_focused_components",
        primary_button="primary_button",
        primary_button_label="primary_button_label",
        secondary_button_border="secondary_button_border",
        secondary_button_label="secondary_button_label",
        success="success",
        widget_background="widget_background",
        widget_border="widget_border",
    ),
    fonts=BrandingThemeFonts(
        body_text=BrandingThemeFontBodyText(
            bold=True,
            size=1.1,
        ),
        buttons_text=BrandingThemeFontButtonsText(
            bold=True,
            size=1.1,
        ),
        font_url="font_url",
        input_labels=BrandingThemeFontInputLabels(
            bold=True,
            size=1.1,
        ),
        links=BrandingThemeFontLinks(
            bold=True,
            size=1.1,
        ),
        links_style="normal",
        reference_text_size=1.1,
        subtitle=BrandingThemeFontSubtitle(
            bold=True,
            size=1.1,
        ),
        title=BrandingThemeFontTitle(
            bold=True,
            size=1.1,
        ),
    ),
    page_background=BrandingThemePageBackground(
        background_color="background_color",
        background_image_url="background_image_url",
        page_layout="center",
    ),
    widget=BrandingThemeWidget(
        header_text_alignment="center",
        logo_height=1.1,
        logo_position="center",
        logo_url="logo_url",
        social_buttons_layout="bottom",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**borders:** `BrandingThemeBorders` 
    
</dd>
</dl>

<dl>
<dd>

**colors:** `BrandingThemeColors` 
    
</dd>
</dl>

<dl>
<dd>

**fonts:** `BrandingThemeFonts` 
    
</dd>
</dl>

<dl>
<dd>

**page_background:** `BrandingThemePageBackground` 
    
</dd>
</dl>

<dl>
<dd>

**widget:** `BrandingThemeWidget` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.themes.<a href="src/auth0/management/branding/themes/client.py">get_default</a>() -&gt; AsyncHttpResponse[GetBrandingDefaultThemeResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve default branding theme.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.themes.get_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.themes.<a href="src/auth0/management/branding/themes/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetBrandingThemeResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve branding theme.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.themes.get(
    theme_id="themeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.themes.<a href="src/auth0/management/branding/themes/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete branding theme.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.themes.delete(
    theme_id="themeId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.themes.<a href="src/auth0/management/branding/themes/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBrandingThemeResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update branding theme.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    BrandingThemeBorders,
    BrandingThemeColors,
    BrandingThemeFontBodyText,
    BrandingThemeFontButtonsText,
    BrandingThemeFontInputLabels,
    BrandingThemeFontLinks,
    BrandingThemeFonts,
    BrandingThemeFontSubtitle,
    BrandingThemeFontTitle,
    BrandingThemePageBackground,
    BrandingThemeWidget,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.themes.update(
    theme_id="themeId",
    borders=BrandingThemeBorders(
        button_border_radius=1.1,
        button_border_weight=1.1,
        buttons_style="pill",
        input_border_radius=1.1,
        input_border_weight=1.1,
        inputs_style="pill",
        show_widget_shadow=True,
        widget_border_weight=1.1,
        widget_corner_radius=1.1,
    ),
    colors=BrandingThemeColors(
        body_text="body_text",
        error="error",
        header="header",
        icons="icons",
        input_background="input_background",
        input_border="input_border",
        input_filled_text="input_filled_text",
        input_labels_placeholders="input_labels_placeholders",
        links_focused_components="links_focused_components",
        primary_button="primary_button",
        primary_button_label="primary_button_label",
        secondary_button_border="secondary_button_border",
        secondary_button_label="secondary_button_label",
        success="success",
        widget_background="widget_background",
        widget_border="widget_border",
    ),
    fonts=BrandingThemeFonts(
        body_text=BrandingThemeFontBodyText(
            bold=True,
            size=1.1,
        ),
        buttons_text=BrandingThemeFontButtonsText(
            bold=True,
            size=1.1,
        ),
        font_url="font_url",
        input_labels=BrandingThemeFontInputLabels(
            bold=True,
            size=1.1,
        ),
        links=BrandingThemeFontLinks(
            bold=True,
            size=1.1,
        ),
        links_style="normal",
        reference_text_size=1.1,
        subtitle=BrandingThemeFontSubtitle(
            bold=True,
            size=1.1,
        ),
        title=BrandingThemeFontTitle(
            bold=True,
            size=1.1,
        ),
    ),
    page_background=BrandingThemePageBackground(
        background_color="background_color",
        background_image_url="background_image_url",
        page_layout="center",
    ),
    widget=BrandingThemeWidget(
        header_text_alignment="center",
        logo_height=1.1,
        logo_position="center",
        logo_url="logo_url",
        social_buttons_layout="bottom",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**theme_id:** `str` — The ID of the theme
    
</dd>
</dl>

<dl>
<dd>

**borders:** `BrandingThemeBorders` 
    
</dd>
</dl>

<dl>
<dd>

**colors:** `BrandingThemeColors` 
    
</dd>
</dl>

<dl>
<dd>

**fonts:** `BrandingThemeFonts` 
    
</dd>
</dl>

<dl>
<dd>

**page_background:** `BrandingThemePageBackground` 
    
</dd>
</dl>

<dl>
<dd>

**widget:** `BrandingThemeWidget` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Branding Phone Providers
<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListBrandingPhoneProvidersResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of <a href="https://auth0.com/docs/customize/phone-messages/configure-phone-messaging-providers">phone providers</a> details set for a Tenant. A list of fields to include or exclude may also be specified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.list(
    disabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the provider is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateBrandingPhoneProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a <a href="https://auth0.com/docs/customize/phone-messages/configure-phone-messaging-providers">phone provider</a>.
The <code>credentials</code> object requires different properties depending on the phone provider (which is specified using the <code>name</code> property).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, TwilioProviderCredentials

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.create(
    name="twilio",
    credentials=TwilioProviderCredentials(
        auth_token="auth_token",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `PhoneProviderNameEnum` 
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `PhoneProviderCredentials` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the provider is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[PhoneProviderConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetBrandingPhoneProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve <a href="https://auth0.com/docs/customize/phone-messages/configure-phone-messaging-providers">phone provider</a> details. A list of fields to include or exclude may also be specified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the configured phone provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateBrandingPhoneProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a <a href="https://auth0.com/docs/customize/phone-messages/configure-phone-messaging-providers">phone provider</a>.
The <code>credentials</code> object requires different properties depending on the phone provider (which is specified using the <code>name</code> property).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[PhoneProviderNameEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the provider is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[PhoneProviderCredentials]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[PhoneProviderConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.providers.<a href="src/auth0/management/branding/phone/providers/client.py">test</a>(...) -&gt; AsyncHttpResponse[CreatePhoneProviderSendTestResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.providers.test(
    id="id",
    to="to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — The recipient phone number to receive a given notification.
    
</dd>
</dl>

<dl>
<dd>

**delivery_method:** `typing.Optional[PhoneProviderDeliveryMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Branding Phone Templates
<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListPhoneTemplatesResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.list(
    disabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the template is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreatePhoneTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[PhoneTemplateNotificationTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the template is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[PhoneTemplateContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetPhoneTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdatePhoneTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[PartialPhoneTemplateContent]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Whether the template is enabled (false) or disabled (true).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">reset</a>(...) -&gt; AsyncHttpResponse[ResetPhoneTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.reset(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ResetPhoneTemplateRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.branding.phone.templates.<a href="src/auth0/management/branding/phone/templates/client.py">test</a>(...) -&gt; AsyncHttpResponse[CreatePhoneTemplateTestNotificationResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.branding.phone.templates.test(
    id="id",
    to="to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Destination of the testing phone notification
    
</dd>
</dl>

<dl>
<dd>

**delivery_method:** `typing.Optional[PhoneProviderDeliveryMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ClientGrants Organizations
<details><summary><code>client.client_grants.organizations.<a href="src/auth0/management/client_grants/organizations/client.py">list</a>(...) -&gt; AsyncPager[Organization, ListClientGrantOrganizationsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.client_grants.organizations.list(
    id="id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client grant
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clients Credentials
<details><summary><code>client.clients.credentials.<a href="src/auth0/management/clients/credentials/client.py">list</a>(...) -&gt; AsyncHttpResponse[typing.List[ClientCredential]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a client credential.

<b>Important</b>: To enable credentials to be used for a client authentication method, set the <code>client_authentication_methods</code> property on the client. To enable credentials to be used for JWT-Secured Authorization requests set the <code>signed_request_object</code> property on the client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.credentials.list(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.credentials.<a href="src/auth0/management/clients/credentials/client.py">create</a>(...) -&gt; AsyncHttpResponse[PostClientCredentialResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a client credential associated to your application. Credentials can be used to configure Private Key JWT and mTLS authentication methods, as well as for JWT-secured Authorization requests.

<h5>Public Key</h5>Public Key credentials can be used to set up Private Key JWT client authentication and JWT-secured Authorization requests.

Sample: <pre><code>{
  "credential_type": "public_key",
  "name": "string",
  "pem": "string",
  "alg": "RS256",
  "parse_expiry_from_cert": false,
  "expires_at": "2022-12-31T23:59:59Z"
}</code></pre>
<h5>Certificate (CA-signed & self-signed)</h5>Certificate credentials can be used to set up mTLS client authentication. CA-signed certificates can be configured either with a signed certificate or with just the certificate Subject DN.

CA-signed Certificate Sample (pem): <pre><code>{
  "credential_type": "x509_cert",
  "name": "string",
  "pem": "string"
}</code></pre>CA-signed Certificate Sample (subject_dn): <pre><code>{
  "credential_type": "cert_subject_dn",
  "name": "string",
  "subject_dn": "string"
}</code></pre>Self-signed Certificate Sample: <pre><code>{
  "credential_type": "cert_subject_dn",
  "name": "string",
  "pem": "string"
}</code></pre>

The credential will be created but not yet enabled for use until you set the corresponding properties in the client:
<ul>
  <li>To enable the credential for Private Key JWT or mTLS authentication methods, set the <code>client_authentication_methods</code> property on the client. For more information, read <a href="https://auth0.com/docs/get-started/applications/configure-private-key-jwt">Configure Private Key JWT Authentication</a> and <a href="https://auth0.com/docs/get-started/applications/configure-mtls">Configure mTLS Authentication</a></li>
  <li>To enable the credential for JWT-secured Authorization requests, set the <code>signed_request_object</code>property on the client. For more information, read <a href="https://auth0.com/docs/get-started/applications/configure-jar">Configure JWT-secured Authorization Requests (JAR)</a></li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.credentials.create(
    client_id="client_id",
    credential_type="public_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**credential_type:** `ClientCredentialTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Friendly name for a credential.
    
</dd>
</dl>

<dl>
<dd>

**subject_dn:** `typing.Optional[str]` — Subject Distinguished Name. Mutually exclusive with `pem` property. Applies to `cert_subject_dn` credential type.
    
</dd>
</dl>

<dl>
<dd>

**pem:** `typing.Optional[str]` — PEM-formatted public key (SPKI and PKCS1) or X509 certificate. Must be JSON escaped.
    
</dd>
</dl>

<dl>
<dd>

**alg:** `typing.Optional[PublicKeyCredentialAlgorithmEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**parse_expiry_from_cert:** `typing.Optional[bool]` — Parse expiry from x509 certificate. If true, attempts to parse the expiry date from the provided PEM. Applies to `public_key` credential type.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` — The ISO 8601 formatted date representing the expiration of the credential. If not specified (not recommended), the credential never expires. Applies to `public_key` credential type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.credentials.<a href="src/auth0/management/clients/credentials/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetClientCredentialResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a client credential.

<b>Important</b>: To enable credentials to be used for a client authentication method, set the <code>client_authentication_methods</code> property on the client. To enable credentials to be used for JWT-Secured Authorization requests set the <code>signed_request_object</code> property on the client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.credentials.get(
    client_id="client_id",
    credential_id="credential_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `str` — ID of the credential.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.credentials.<a href="src/auth0/management/clients/credentials/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a client credential you previously created. May be enabled or disabled. For more information, read <a href="https://www.auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow">Client Credential Flow</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.credentials.delete(
    client_id="client_id",
    credential_id="credential_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `str` — ID of the credential to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.credentials.<a href="src/auth0/management/clients/credentials/client.py">update</a>(...) -&gt; AsyncHttpResponse[PatchClientCredentialResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change a client credential you previously created. May be enabled or disabled. For more information, read <a href="https://www.auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow">Client Credential Flow</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.clients.credentials.update(
    client_id="client_id",
    credential_id="credential_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — ID of the client.
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `str` — ID of the credential.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` — The ISO 8601 formatted date representing the expiration of the credential.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clients Connections
<details><summary><code>client.clients.connections.<a href="src/auth0/management/clients/connections/client.py">get</a>(...) -&gt; AsyncPager[ConnectionForList, ListClientConnectionsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all connections that are enabled for the specified <a href="https://www.auth0.com/docs/get-started/applications"> Application</a>, using checkpoint pagination. A list of fields to include or exclude for each connection may also be specified.
<ul>
  <li>
    This endpoint requires the <code>read:connections</code> scope and any one of <code>read:clients</code> or <code>read:client_summary</code>.
  </li>
  <li>
    <b>Note</b>: The first time you call this endpoint, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no further results are remaining.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.clients.connections.get(
    id="id",
    from_="from",
    take=1,
    fields="fields",
    include_fields=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the client for which to retrieve enabled connections.
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `typing.Optional[
    typing.Union[
        ConnectionStrategyEnum, typing.Sequence[ConnectionStrategyEnum]
    ]
]` — Provide strategies to only retrieve connections with such strategies
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — <code>true</code> if the fields specified are to be included in the result, <code>false</code> otherwise (defaults to <code>true</code>)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections DirectoryProvisioning
<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">list</a>(...) -&gt; AsyncPager[DirectoryProvisioning, ListDirectoryProvisioningsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of directory provisioning configurations of a tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.connections.directory_provisioning.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetDirectoryProvisioningResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the directory provisioning configuration of a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve its directory provisioning configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateDirectoryProvisioningResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a directory provisioning configuration for a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, CreateDirectoryProvisioningRequestContent

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.create(
    id="id",
    request=CreateDirectoryProvisioningRequestContent(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to create its directory provisioning configuration
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CreateDirectoryProvisioningRequestContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the directory provisioning configuration of a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to delete its directory provisioning configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateDirectoryProvisioningResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the directory provisioning configuration of a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, UpdateDirectoryProvisioningRequestContent

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.update(
    id="id",
    request=UpdateDirectoryProvisioningRequestContent(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to create its directory provisioning configuration
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[UpdateDirectoryProvisioningRequestContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.directory_provisioning.<a href="src/auth0/management/connections/directory_provisioning/client.py">get_default_mapping</a>(...) -&gt; AsyncHttpResponse[GetDirectoryProvisioningDefaultMappingResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the directory provisioning default attribute mapping of a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.get_default_mapping(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve its directory provisioning configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections Clients
<details><summary><code>client.connections.clients.<a href="src/auth0/management/connections/clients/client.py">get</a>(...) -&gt; AsyncPager[ConnectionEnabledClient, GetConnectionEnabledClientsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all clients that have the specified <a href="https://auth0.com/docs/authenticate/identity-providers">connection</a> enabled.

<b>Note</b>: The first time you call this endpoint, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no further results are remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.connections.clients.get(
    id="id",
    take=1,
    from_="from",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection for which enabled clients are to be retrieved
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.clients.<a href="src/auth0/management/connections/clients/client.py">update</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, UpdateEnabledClientConnectionsRequestContentItem

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.clients.update(
    id="id",
    request=[
        UpdateEnabledClientConnectionsRequestContentItem(
            client_id="client_id",
            status=True,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to modify
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateEnabledClientConnectionsRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections Keys
<details><summary><code>client.connections.keys.<a href="src/auth0/management/connections/keys/client.py">get</a>(...) -&gt; AsyncHttpResponse[typing.List[ConnectionKey]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the connection keys for the Okta or OIDC connection strategy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.keys.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.keys.<a href="src/auth0/management/connections/keys/client.py">rotate</a>(...) -&gt; AsyncHttpResponse[RotateConnectionsKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotates the connection keys for the Okta or OIDC connection strategies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, RotateConnectionKeysRequestContent

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.keys.rotate(
    id="id",
    request=RotateConnectionKeysRequestContent(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the connection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[RotateConnectionKeysRequestContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections ScimConfiguration
<details><summary><code>client.connections.scim_configuration.<a href="src/auth0/management/connections/scim_configuration/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetScimConfigurationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a scim configuration by its <code>connectionId</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve its SCIM configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.<a href="src/auth0/management/connections/scim_configuration/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateScimConfigurationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a scim configuration for a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, CreateScimConfigurationRequestContent

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.create(
    id="id",
    request=CreateScimConfigurationRequestContent(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to create its SCIM configuration
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CreateScimConfigurationRequestContent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.<a href="src/auth0/management/connections/scim_configuration/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a scim configuration by its <code>connectionId</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to delete its SCIM configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.<a href="src/auth0/management/connections/scim_configuration/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateScimConfigurationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a scim configuration by its <code>connectionId</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, ScimMappingItem

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.update(
    id="id",
    user_id_attribute="user_id_attribute",
    mapping=[ScimMappingItem()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to update its SCIM configuration
    
</dd>
</dl>

<dl>
<dd>

**user_id_attribute:** `str` — User ID attribute for generating unique user ids
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Sequence[ScimMappingItem]` — The mapping between auth0 and SCIM
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.<a href="src/auth0/management/connections/scim_configuration/client.py">get_default_mapping</a>(...) -&gt; AsyncHttpResponse[GetScimConfigurationDefaultMappingResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a scim configuration's default mapping by its <code>connectionId</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.get_default_mapping(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve its default SCIM mapping
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections Users
<details><summary><code>client.connections.users.<a href="src/auth0/management/connections/users/client.py">delete_by_email</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specified connection user by its email (you cannot delete all users from specific connection). Currently, only Database Connections are supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.users.delete_by_email(
    id="id",
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection (currently only database connections are supported)
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email of the user to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections DirectoryProvisioning Synchronizations
<details><summary><code>client.connections.directory_provisioning.synchronizations.<a href="src/auth0/management/connections/directory_provisioning/synchronizations/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateDirectorySynchronizationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request an on-demand synchronization of the directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.directory_provisioning.synchronizations.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to trigger synchronization for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections ScimConfiguration Tokens
<details><summary><code>client.connections.scim_configuration.tokens.<a href="src/auth0/management/connections/scim_configuration/tokens/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetScimTokensResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all scim tokens by its connection <code>id</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.tokens.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to retrieve its SCIM configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.tokens.<a href="src/auth0/management/connections/scim_configuration/tokens/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateScimTokenResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a scim token for a scim client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.tokens.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the connection to create its SCIM token
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Sequence[str]]` — The scopes of the scim token
    
</dd>
</dl>

<dl>
<dd>

**token_lifetime:** `typing.Optional[int]` — Lifetime of the token in seconds. Must be greater than 900
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.scim_configuration.tokens.<a href="src/auth0/management/connections/scim_configuration/tokens/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a scim token by its connection <code>id</code> and <code>tokenId</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.connections.scim_configuration.tokens.delete(
    id="id",
    token_id="tokenId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The connection id that owns the SCIM token to delete
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `str` — The id of the scim token to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Emails Provider
<details><summary><code>client.emails.provider.<a href="src/auth0/management/emails/provider/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetEmailProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the <a href="https://auth0.com/docs/customize/email/smtp-email-providers">email provider configuration</a> in your tenant. A list of fields to include or exclude may also be specified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.emails.provider.get(
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (dependent upon include_fields) from the result. Leave empty to retrieve `name` and `enabled`. Additional fields available include `credentials`, `default_from_address`, and `settings`.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.emails.provider.<a href="src/auth0/management/emails/provider/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateEmailProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an <a href="https://auth0.com/docs/email/providers">email provider</a>. The <code>credentials</code> object
requires different properties depending on the email provider (which is specified using the <code>name</code> property):
<ul>
  <li><code>mandrill</code> requires <code>api_key</code></li>
  <li><code>sendgrid</code> requires <code>api_key</code></li>
  <li>
    <code>sparkpost</code> requires <code>api_key</code>. Optionally, set <code>region</code> to <code>eu</code> to use
    the SparkPost service hosted in Western Europe; set to <code>null</code> to use the SparkPost service hosted in
    North America. <code>eu</code> or <code>null</code> are the only valid values for <code>region</code>.
  </li>
  <li>
    <code>mailgun</code> requires <code>api_key</code> and <code>domain</code>. Optionally, set <code>region</code> to
    <code>eu</code> to use the Mailgun service hosted in Europe; set to <code>null</code> otherwise. <code>eu</code> or
    <code>null</code> are the only valid values for <code>region</code>.
  </li>
  <li><code>ses</code> requires <code>accessKeyId</code>, <code>secretAccessKey</code>, and <code>region</code></li>
  <li>
    <code>smtp</code> requires <code>smtp_host</code>, <code>smtp_port</code>, <code>smtp_user</code>, and
    <code>smtp_pass</code>
  </li>
</ul>
Depending on the type of provider it is possible to specify <code>settings</code> object with different configuration
options, which will be used when sending an email:
<ul>
  <li>
    <code>smtp</code> provider, <code>settings</code> may contain <code>headers</code> object.
    <ul>
      <li>
        When using AWS SES SMTP host, you may provide a name of configuration set in
        <code>X-SES-Configuration-Set</code> header. Value must be a string.
      </li>
      <li>
        When using Sparkpost host, you may provide value for
        <code>X-MSYS_API</code> header. Value must be an object.
      </li>
    </ul>
  </li>
  <li>
    for <code>ses</code> provider, <code>settings</code> may contain <code>message</code> object, where you can provide
    a name of configuration set in <code>configuration_set_name</code> property. Value must be a string.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, EmailProviderCredentialsSchemaZero

client = Auth0(
    token="YOUR_TOKEN",
)
client.emails.provider.create(
    name="mailgun",
    credentials=EmailProviderCredentialsSchemaZero(
        api_key="api_key",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `EmailProviderNameEnum` 
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `EmailProviderCredentialsSchema` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the provider is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**default_from_address:** `typing.Optional[str]` — Email address to use as "from" when no other address specified.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[EmailSpecificProviderSettingsWithAdditionalProperties]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.emails.provider.<a href="src/auth0/management/emails/provider/client.py">delete</a>() -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the email provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.emails.provider.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.emails.provider.<a href="src/auth0/management/emails/provider/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateEmailProviderResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an <a href="https://auth0.com/docs/email/providers">email provider</a>. The <code>credentials</code> object
requires different properties depending on the email provider (which is specified using the <code>name</code> property):
<ul>
  <li><code>mandrill</code> requires <code>api_key</code></li>
  <li><code>sendgrid</code> requires <code>api_key</code></li>
  <li>
    <code>sparkpost</code> requires <code>api_key</code>. Optionally, set <code>region</code> to <code>eu</code> to use
    the SparkPost service hosted in Western Europe; set to <code>null</code> to use the SparkPost service hosted in
    North America. <code>eu</code> or <code>null</code> are the only valid values for <code>region</code>.
  </li>
  <li>
    <code>mailgun</code> requires <code>api_key</code> and <code>domain</code>. Optionally, set <code>region</code> to
    <code>eu</code> to use the Mailgun service hosted in Europe; set to <code>null</code> otherwise. <code>eu</code> or
    <code>null</code> are the only valid values for <code>region</code>.
  </li>
  <li><code>ses</code> requires <code>accessKeyId</code>, <code>secretAccessKey</code>, and <code>region</code></li>
  <li>
    <code>smtp</code> requires <code>smtp_host</code>, <code>smtp_port</code>, <code>smtp_user</code>, and
    <code>smtp_pass</code>
  </li>
</ul>
Depending on the type of provider it is possible to specify <code>settings</code> object with different configuration
options, which will be used when sending an email:
<ul>
  <li>
    <code>smtp</code> provider, <code>settings</code> may contain <code>headers</code> object.
    <ul>
      <li>
        When using AWS SES SMTP host, you may provide a name of configuration set in
        <code>X-SES-Configuration-Set</code> header. Value must be a string.
      </li>
      <li>
        When using Sparkpost host, you may provide value for
        <code>X-MSYS_API</code> header. Value must be an object.
      </li>
    </ul>
    for <code>ses</code> provider, <code>settings</code> may contain <code>message</code> object, where you can provide
    a name of configuration set in <code>configuration_set_name</code> property. Value must be a string.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.emails.provider.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[EmailProviderNameEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the provider is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**default_from_address:** `typing.Optional[str]` — Email address to use as "from" when no other address specified.
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[EmailProviderCredentialsSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[EmailSpecificProviderSettingsWithAdditionalProperties]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EventStreams Deliveries
<details><summary><code>client.event_streams.deliveries.<a href="src/auth0/management/event_streams/deliveries/client.py">list</a>(...) -&gt; AsyncHttpResponse[typing.List[EventStreamDelivery]]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.deliveries.list(
    id="id",
    statuses="statuses",
    event_types="event_types",
    date_from="date_from",
    date_to="date_to",
    from_="from",
    take=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[str]` — Comma-separated list of statuses by which to filter
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[str]` — Comma-separated list of event types by which to filter
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[str]` — An RFC-3339 date-time for redelivery start, inclusive. Does not allow sub-second precision.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[str]` — An RFC-3339 date-time for redelivery end, exclusive. Does not allow sub-second precision.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.deliveries.<a href="src/auth0/management/event_streams/deliveries/client.py">get_history</a>(...) -&gt; AsyncHttpResponse[GetEventStreamDeliveryHistoryResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.deliveries.get_history(
    id="id",
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EventStreams Redeliveries
<details><summary><code>client.event_streams.redeliveries.<a href="src/auth0/management/event_streams/redeliveries/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateEventStreamRedeliveryResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.redeliveries.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[dt.datetime]` — An RFC-3339 date-time for redelivery start, inclusive. Does not allow sub-second precision.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[dt.datetime]` — An RFC-3339 date-time for redelivery end, exclusive. Does not allow sub-second precision.
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[typing.Sequence[EventStreamDeliveryStatusEnum]]` — Filter by status
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[EventStreamEventTypeEnum]]` — Filter by event type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_streams.redeliveries.<a href="src/auth0/management/event_streams/redeliveries/client.py">create_by_id</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.event_streams.redeliveries.create_by_id(
    id="id",
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the event stream.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flows Executions
<details><summary><code>client.flows.executions.<a href="src/auth0/management/flows/executions/client.py">list</a>(...) -&gt; AsyncPager[FlowExecutionSummary, ListFlowExecutionsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.flows.executions.list(
    flow_id="flow_id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flow_id:** `str` — Flow id
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.executions.<a href="src/auth0/management/flows/executions/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetFlowExecutionResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.executions.get(
    flow_id="flow_id",
    execution_id="execution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flow_id:** `str` — Flow id
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` — Flow execution id
    
</dd>
</dl>

<dl>
<dd>

**hydrate:** `typing.Optional[
    typing.Union[
        GetFlowExecutionRequestParametersHydrateEnum,
        typing.Sequence[GetFlowExecutionRequestParametersHydrateEnum],
    ]
]` — Hydration param
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.executions.<a href="src/auth0/management/flows/executions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.executions.delete(
    flow_id="flow_id",
    execution_id="execution_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flow_id:** `str` — Flows id
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` — Flow execution identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Flows Vault Connections
<details><summary><code>client.flows.vault.connections.<a href="src/auth0/management/flows/vault/connections/client.py">list</a>(...) -&gt; AsyncPager[
    FlowsVaultConnectionSummary,
    ListFlowsVaultConnectionsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.flows.vault.connections.list(
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.vault.connections.<a href="src/auth0/management/flows/vault/connections/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateFlowsVaultConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    CreateFlowsVaultConnectionActivecampaignApiKey,
    FlowsVaultConnectioSetupApiKeyWithBaseUrl,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.vault.connections.create(
    request=CreateFlowsVaultConnectionActivecampaignApiKey(
        name="name",
        app_id="ACTIVECAMPAIGN",
        setup=FlowsVaultConnectioSetupApiKeyWithBaseUrl(
            type="API_KEY",
            api_key="api_key",
            base_url="base_url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateFlowsVaultConnectionRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.vault.connections.<a href="src/auth0/management/flows/vault/connections/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetFlowsVaultConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.vault.connections.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flows Vault connection ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.vault.connections.<a href="src/auth0/management/flows/vault/connections/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.vault.connections.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Vault connection id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.flows.vault.connections.<a href="src/auth0/management/flows/vault/connections/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateFlowsVaultConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.flows.vault.connections.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flows Vault connection ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Flows Vault Connection name.
    
</dd>
</dl>

<dl>
<dd>

**setup:** `typing.Optional[UpdateFlowsVaultConnectionSetup]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups Members
<details><summary><code>client.groups.members.<a href="src/auth0/management/groups/members/client.py">get</a>(...) -&gt; AsyncPager[GroupMember, GetGroupMembersResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all users that are a member of this group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.groups.members.get(
    id="id",
    fields="fields",
    include_fields=True,
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the group (service-generated).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Enrollments
<details><summary><code>client.guardian.enrollments.<a href="src/auth0/management/guardian/enrollments/client.py">create_ticket</a>(...) -&gt; AsyncHttpResponse[CreateGuardianEnrollmentTicketResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a <a href="https://auth0.com/docs/secure/multi-factor-authentication/auth0-guardian/create-custom-enrollment-tickets">multi-factor authentication (MFA) enrollment ticket</a>, and optionally send an email with the created ticket, to a given user.
Create a <a href="https://auth0.com/docs/secure/multi-factor-authentication/auth0-guardian/create-custom-enrollment-tickets">multi-factor authentication (MFA) enrollment ticket</a>, and optionally send an email with the created ticket to a given user. Enrollment tickets can specify which factor users must enroll with or allow existing MFA users to enroll in additional factors.<br/> 

Note: Users cannot enroll in Email as a factor through custom enrollment tickets. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.enrollments.create_ticket(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — user_id for the enrollment ticket
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — alternate email to which the enrollment email will be sent. Optional - by default, the email will be sent to the user's default address
    
</dd>
</dl>

<dl>
<dd>

**send_mail:** `typing.Optional[bool]` — Send an email to the user to start the enrollment
    
</dd>
</dl>

<dl>
<dd>

**email_locale:** `typing.Optional[str]` — Optional. Specify the locale of the enrollment email. Used with send_email.
    
</dd>
</dl>

<dl>
<dd>

**factor:** `typing.Optional[GuardianEnrollmentFactorEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_multiple_enrollments:** `typing.Optional[bool]` — Optional. Allows a user who has previously enrolled in MFA to enroll with additional factors.<br />Note: Parameter can only be used with Universal Login; it cannot be used with Classic Login or custom MFA pages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.enrollments.<a href="src/auth0/management/guardian/enrollments/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetGuardianEnrollmentResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details, such as status and type, for a specific multi-factor authentication enrollment registered to a user account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.enrollments.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the enrollment to be retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.enrollments.<a href="src/auth0/management/guardian/enrollments/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a specific multi-factor authentication (MFA) enrollment from a user's account. This allows the user to re-enroll with MFA. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/reset-user-mfa">Reset User Multi-Factor Authentication and Recovery Codes</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.enrollments.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the enrollment to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Factors
<details><summary><code>client.guardian.factors.<a href="src/auth0/management/guardian/factors/client.py">list</a>() -&gt; AsyncHttpResponse[typing.List[GuardianFactor]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors">multi-factor authentication factors</a> associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.<a href="src/auth0/management/guardian/factors/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status (i.e., enabled or disabled) of a specific multi-factor authentication factor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.set(
    name="push-notification",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `GuardianFactorNameEnum` — Factor name. Can be `sms`, `push-notification`, `email`, `duo` `otp` `webauthn-roaming`, `webauthn-platform`, or `recovery-code`.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Whether this factor is enabled (true) or disabled (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Policies
<details><summary><code>client.guardian.policies.<a href="src/auth0/management/guardian/policies/client.py">list</a>() -&gt; AsyncHttpResponse[ListGuardianPoliciesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the <a href="https://auth0.com/docs/secure/multi-factor-authentication/enable-mfa">multi-factor authentication (MFA) policies</a> configured for your tenant.

The following policies are supported:
<ul>
<li><code>all-applications</code> policy prompts with MFA for all logins.</li>
<li><code>confidence-score</code> policy prompts with MFA only for low confidence logins.</li>
</ul>

<b>Note</b>: The <code>confidence-score</code> policy is part of the <a href="https://auth0.com/docs/secure/multi-factor-authentication/adaptive-mfa">Adaptive MFA feature</a>. Adaptive MFA requires an add-on for the Enterprise plan; review <a href="https://auth0.com/pricing">Auth0 Pricing</a> for more details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.policies.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.policies.<a href="src/auth0/management/guardian/policies/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetGuardianPoliciesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set <a href="https://auth0.com/docs/secure/multi-factor-authentication/enable-mfa">multi-factor authentication (MFA) policies</a> for your tenant.

The following policies are supported:
<ul>
<li><code>all-applications</code> policy prompts with MFA for all logins.</li>
<li><code>confidence-score</code> policy prompts with MFA only for low confidence logins.</li>
</ul>

<b>Note</b>: The <code>confidence-score</code> policy is part of the <a href="https://auth0.com/docs/secure/multi-factor-authentication/adaptive-mfa">Adaptive MFA feature</a>. Adaptive MFA requires an add-on for the Enterprise plan; review <a href="https://auth0.com/pricing">Auth0 Pricing</a> for more details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.policies.set(
    request=["all-applications"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SetGuardianPoliciesRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Factors Phone
<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">get_message_types</a>() -&gt; AsyncHttpResponse[GetGuardianFactorPhoneMessageTypesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve list of <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-sms-voice-notifications-mfa">phone-type MFA factors</a> (i.e., sms and voice) that are enabled for your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.get_message_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">set_message_types</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorPhoneMessageTypesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the list of <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-sms-voice-notifications-mfa">phone-type MFA factors</a> (i.e., sms and voice) that are enabled for your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.set_message_types(
    message_types=["sms"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_types:** `typing.Sequence[GuardianFactorPhoneFactorMessageTypeEnum]` — The list of phone factors to enable on the tenant. Can include `sms` and `voice`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">get_twilio_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderPhoneTwilioResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve configuration details for a Twilio phone provider that has been set up in your tenant. To learn more, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-sms-voice-notifications-mfa">Configure SMS and Voice Notifications for MFA</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.get_twilio_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">set_twilio_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPhoneTwilioResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration of a Twilio phone provider that has been set up in your tenant. To learn more, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-sms-voice-notifications-mfa">Configure SMS and Voice Notifications for MFA</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.set_twilio_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — From number
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_sid:** `typing.Optional[str]` — Copilot SID
    
</dd>
</dl>

<dl>
<dd>

**auth_token:** `typing.Optional[str]` — Twilio Authentication token
    
</dd>
</dl>

<dl>
<dd>

**sid:** `typing.Optional[str]` — Twilio SID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">get_selected_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderPhoneResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the multi-factor authentication phone provider configured for your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.get_selected_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">set_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPhoneResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.set_provider(
    provider="auth0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `GuardianFactorsProviderSmsProviderEnum` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">get_templates</a>() -&gt; AsyncHttpResponse[GetGuardianFactorPhoneTemplatesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the multi-factor authentication enrollment and verification templates for phone-type factors available in your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.get_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.phone.<a href="src/auth0/management/guardian/factors/phone/client.py">set_templates</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorPhoneTemplatesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Customize the messages sent to complete phone enrollment and verification (subscription required).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.phone.set_templates(
    enrollment_message="enrollment_message",
    verification_message="verification_message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_message:** `str` — Message sent to the user when they are invited to enroll with a phone number.
    
</dd>
</dl>

<dl>
<dd>

**verification_message:** `str` — Message sent to the user when they are prompted to verify their account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Factors PushNotification
<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">get_apns_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderApnsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve configuration details for the multi-factor authentication APNS provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.get_apns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">set_apns_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPushNotificationApnsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overwrite all configuration details of the multi-factor authentication APNS provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.set_apns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**p_12:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">update_apns_provider</a>(...) -&gt; AsyncHttpResponse[
    UpdateGuardianFactorsProviderPushNotificationApnsResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify configuration details of the multi-factor authentication APNS provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.update_apns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**p_12:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">set_fcm_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPushNotificationFcmResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overwrite all configuration details of the multi-factor authentication FCM provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.set_fcm_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**server_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">update_fcm_provider</a>(...) -&gt; AsyncHttpResponse[
    UpdateGuardianFactorsProviderPushNotificationFcmResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify configuration details of the multi-factor authentication FCM provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.update_fcm_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**server_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">set_fcmv_1_provider</a>(...) -&gt; AsyncHttpResponse[
    SetGuardianFactorsProviderPushNotificationFcmv1ResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overwrite all configuration details of the multi-factor authentication FCMV1 provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.set_fcmv_1_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**server_credentials:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">update_fcmv_1_provider</a>(...) -&gt; AsyncHttpResponse[
    UpdateGuardianFactorsProviderPushNotificationFcmv1ResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify configuration details of the multi-factor authentication FCMV1 provider associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.update_fcmv_1_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**server_credentials:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">get_sns_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderSnsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve configuration details for an AWS SNS push notification provider that has been enabled for MFA. To learn more, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-push-notifications-for-mfa">Configure Push Notifications for MFA</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.get_sns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">set_sns_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPushNotificationSnsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure the <a href="https://auth0.com/docs/multifactor-authentication/developer/sns-configuration">AWS SNS push notification provider configuration</a> (subscription required).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.set_sns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**aws_secret_access_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**aws_region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sns_apns_platform_application_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sns_gcm_platform_application_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">update_sns_provider</a>(...) -&gt; AsyncHttpResponse[
    UpdateGuardianFactorsProviderPushNotificationSnsResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure the <a href="https://auth0.com/docs/multifactor-authentication/developer/sns-configuration">AWS SNS push notification provider configuration</a> (subscription required).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.update_sns_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aws_access_key_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**aws_secret_access_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**aws_region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sns_apns_platform_application_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sns_gcm_platform_application_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">get_selected_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderPushNotificationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the push notification provider configured for your tenant. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-push-notifications-for-mfa">Configure Push Notifications for MFA</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.get_selected_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.push_notification.<a href="src/auth0/management/guardian/factors/push_notification/client.py">set_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderPushNotificationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the push notification provider configured for your tenant. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors/configure-push-notifications-for-mfa">Configure Push Notifications for MFA</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.push_notification.set_provider(
    provider="guardian",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `GuardianFactorsProviderPushNotificationProviderDataEnum` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Factors Sms
<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">get_twilio_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderSmsTwilioResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the <a href="https://auth0.com/docs/multifactor-authentication/twilio-configuration">Twilio SMS provider configuration</a> (subscription required).

    A new endpoint is available to retrieve the Twilio configuration related to phone factors (<a href='https://auth0.com/docs/api/management/v2/#!/Guardian/get_twilio'>phone Twilio configuration</a>). It has the same payload as this one. Please use it instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.get_twilio_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">set_twilio_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderSmsTwilioResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated. To complete this action, use the <a href="https://auth0.com/docs/api/management/v2/guardian/put-twilio">Update Twilio phone configuration</a> endpoint.

    <b>Previous functionality</b>: Update the Twilio SMS provider configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.set_twilio_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — From number
    
</dd>
</dl>

<dl>
<dd>

**messaging_service_sid:** `typing.Optional[str]` — Copilot SID
    
</dd>
</dl>

<dl>
<dd>

**auth_token:** `typing.Optional[str]` — Twilio Authentication token
    
</dd>
</dl>

<dl>
<dd>

**sid:** `typing.Optional[str]` — Twilio SID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">get_selected_provider</a>() -&gt; AsyncHttpResponse[GetGuardianFactorsProviderSmsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated. To complete this action, use the <a href="https://auth0.com/docs/api/management/v2/guardian/get-phone-providers">Retrieve phone configuration</a> endpoint instead.

    <b>Previous functionality</b>: Retrieve details for the multi-factor authentication SMS provider configured for your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.get_selected_provider()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">set_provider</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorsProviderSmsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated. To complete this action, use the <a href="https://auth0.com/docs/api/management/v2/guardian/put-phone-providers">Update phone configuration</a> endpoint instead.

    <b>Previous functionality</b>: Update the multi-factor authentication SMS provider configuration in your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.set_provider(
    provider="auth0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `GuardianFactorsProviderSmsProviderEnum` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">get_templates</a>() -&gt; AsyncHttpResponse[GetGuardianFactorSmsTemplatesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated. To complete this action, use the <a href="https://auth0.com/docs/api/management/v2/guardian/get-factor-phone-templates">Retrieve enrollment and verification phone templates</a> endpoint instead.

    <b>Previous function</b>: Retrieve details of SMS enrollment and verification templates configured for your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.get_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.sms.<a href="src/auth0/management/guardian/factors/sms/client.py">set_templates</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorSmsTemplatesResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint has been deprecated. To complete this action, use the <a href="https://auth0.com/docs/api/management/v2/guardian/put-factor-phone-templates">Update enrollment and verification phone templates</a> endpoint instead.

    <b>Previous functionality</b>: Customize the messages sent to complete SMS enrollment and verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.sms.set_templates(
    enrollment_message="enrollment_message",
    verification_message="verification_message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enrollment_message:** `str` — Message sent to the user when they are invited to enroll with a phone number.
    
</dd>
</dl>

<dl>
<dd>

**verification_message:** `str` — Message sent to the user when they are prompted to verify their account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guardian Factors Duo Settings
<details><summary><code>client.guardian.factors.duo.settings.<a href="src/auth0/management/guardian/factors/duo/settings/client.py">get</a>() -&gt; AsyncHttpResponse[GetGuardianFactorDuoSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the DUO account and factor configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.duo.settings.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.duo.settings.<a href="src/auth0/management/guardian/factors/duo/settings/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetGuardianFactorDuoSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the DUO account configuration and other properties specific to this factor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.duo.settings.set()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ikey:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**skey:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guardian.factors.duo.settings.<a href="src/auth0/management/guardian/factors/duo/settings/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateGuardianFactorDuoSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.guardian.factors.duo.settings.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ikey:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**skey:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Hooks Secrets
<details><summary><code>client.hooks.secrets.<a href="src/auth0/management/hooks/secrets/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetHookSecretResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a hook's secrets by the ID of the hook. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.secrets.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook to retrieve secrets from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.secrets.<a href="src/auth0/management/hooks/secrets/client.py">create</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add one or more secrets to an existing hook. Accepts an object of key-value pairs, where the key is the name of the secret. A hook can have a maximum of 20 secrets. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.secrets.create(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the hook to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateHookSecretRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.secrets.<a href="src/auth0/management/hooks/secrets/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one or more existing secrets for a given hook. Accepts an array of secret names to delete. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.secrets.delete(
    id="id",
    request=["string"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook whose secrets to delete.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteHookSecretRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hooks.secrets.<a href="src/auth0/management/hooks/secrets/client.py">update</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one or more existing secrets for an existing hook. Accepts an object of key-value pairs, where the key is the name of the existing secret. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.hooks.secrets.update(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the hook whose secrets to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateHookSecretRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs UsersExports
<details><summary><code>client.jobs.users_exports.<a href="src/auth0/management/jobs/users_exports/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateExportUsersResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export all users to a file via a long-running job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.jobs.users_exports.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — connection_id of the connection from which users will be exported.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[JobFileFormatEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[CreateExportUsersFields]]` — List of fields to be included in the CSV. Defaults to a predefined set of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs UsersImports
<details><summary><code>client.jobs.users_imports.<a href="src/auth0/management/jobs/users_imports/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateImportUsersResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import users from a <a href="https://auth0.com/docs/users/references/bulk-import-database-schema-examples">formatted file</a> into a connection via a long-running job. When importing users, with or without upsert, the `email_verified` is set to `false` when the email address is added or updated. Users must verify their email address. To avoid this behavior, set `email_verified` to `true` in the imported data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.jobs.users_imports.create(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**users:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — connection_id of the connection to which users will be imported.
    
</dd>
</dl>

<dl>
<dd>

**upsert:** `typing.Optional[bool]` — Whether to update users if they already exist (true) or to ignore them (false).
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — Customer-defined ID.
    
</dd>
</dl>

<dl>
<dd>

**send_completion_email:** `typing.Optional[bool]` — Whether to send a completion email to all tenant owners when the job is finished (true) or not (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs VerificationEmail
<details><summary><code>client.jobs.verification_email.<a href="src/auth0/management/jobs/verification_email/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateVerificationEmailResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an email to the specified user that asks them to click a link to <a href="https://auth0.com/docs/email/custom#verification-email">verify their email address</a>.

Note: You must have the `Status` toggle enabled for the verification email template for the email to be sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.jobs.verification_email.create(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — user_id of the user to send the verification email to.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — client_id of the client (application). If no value provided, the global Client ID will be used.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — (Optional) Organization ID – the ID of the Organization. If provided, organization parameters will be made available to the email template and organization branding will be applied to the prompt. In addition, the redirect link in the prompt will include organization_id and organization_name query string parameters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs Errors
<details><summary><code>client.jobs.errors.<a href="src/auth0/management/jobs/errors/client.py">get</a>(...) -&gt; AsyncHttpResponse[ErrorsGetResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve error details of a failed job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.jobs.errors.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys CustomSigning
<details><summary><code>client.keys.custom_signing.<a href="src/auth0/management/keys/custom_signing/client.py">get</a>() -&gt; AsyncHttpResponse[GetCustomSigningKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entire jwks representation of custom signing keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.custom_signing.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.custom_signing.<a href="src/auth0/management/keys/custom_signing/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetCustomSigningKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace entire jwks representation of custom signing keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, CustomSigningKeyJwk

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.custom_signing.set(
    keys=[
        CustomSigningKeyJwk(
            kty="EC",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**keys:** `typing.Sequence[CustomSigningKeyJwk]` — An array of custom public signing keys.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.custom_signing.<a href="src/auth0/management/keys/custom_signing/client.py">delete</a>() -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entire jwks representation of custom signing keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.custom_signing.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys Encryption
<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">list</a>(...) -&gt; AsyncPager[EncryptionKey, ListEncryptionKeyOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all the encryption keys associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.keys.encryption.list(
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Default value is 50, maximum value is 100.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateEncryptionKeyResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create the new, pre-activated encryption key, without the key material.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.create(
    type="customer-provided-root-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `CreateEncryptionKeyType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">rekey</a>() -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform rekeying operation on the key hierarchy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.rekey()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetEncryptionKeyResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the encryption key with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.get(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Encryption key ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">import_</a>(...) -&gt; AsyncHttpResponse[ImportEncryptionKeyResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import wrapped key material and activate encryption key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.import_(
    kid="kid",
    wrapped_key="wrapped_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Encryption key ID
    
</dd>
</dl>

<dl>
<dd>

**wrapped_key:** `str` — Base64 encoded ciphertext of key material wrapped by public wrapping key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the custom provided encryption key with the given ID and move back to using native encryption key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.delete(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Encryption key ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.encryption.<a href="src/auth0/management/keys/encryption/client.py">create_public_wrapping_key</a>(...) -&gt; AsyncHttpResponse[CreateEncryptionKeyPublicWrappingResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create the public wrapping key to wrap your own encryption key material.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.encryption.create_public_wrapping_key(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Encryption key ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys Signing
<details><summary><code>client.keys.signing.<a href="src/auth0/management/keys/signing/client.py">list</a>() -&gt; AsyncHttpResponse[typing.List[SigningKeys]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of all the application signing keys associated with your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.signing.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.signing.<a href="src/auth0/management/keys/signing/client.py">rotate</a>() -&gt; AsyncHttpResponse[RotateSigningKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate the application signing key of your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.signing.rotate()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.signing.<a href="src/auth0/management/keys/signing/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetSigningKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of the application signing key with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.signing.get(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Key id of the key to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.signing.<a href="src/auth0/management/keys/signing/client.py">revoke</a>(...) -&gt; AsyncHttpResponse[RevokedSigningKeysResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke the application signing key with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.keys.signing.revoke(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` — Key id of the key to revoke
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations ClientGrants
<details><summary><code>client.organizations.client_grants.<a href="src/auth0/management/organizations/client_grants/client.py">list</a>(...) -&gt; AsyncPager[
    OrganizationClientGrant,
    ListOrganizationClientGrantsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.client_grants.list(
    id="id",
    audience="audience",
    client_id="client_id",
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**audience:** `typing.Optional[str]` — Optional filter on audience of the client grant.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Optional filter on client_id of the client grant.
    
</dd>
</dl>

<dl>
<dd>

**grant_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional filter on the ID of the client grant. Must be URL encoded and may be specified multiple times (max 10).<br /><b>e.g.</b> <i>../client-grants?grant_ids=id1&grant_ids=id2</i>
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.client_grants.<a href="src/auth0/management/organizations/client_grants/client.py">create</a>(...) -&gt; AsyncHttpResponse[AssociateOrganizationClientGrantResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.client_grants.create(
    id="id",
    grant_id="grant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**grant_id:** `str` — A Client Grant ID to add to the organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.client_grants.<a href="src/auth0/management/organizations/client_grants/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.client_grants.delete(
    id="id",
    grant_id="grant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**grant_id:** `str` — The Client Grant ID to remove from the organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations DiscoveryDomains
<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">list</a>(...) -&gt; AsyncPager[
    OrganizationDiscoveryDomain, ListOrganizationDiscoveryDomainsResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve list of all organization discovery domains associated with the specified organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.discovery_domains.list(
    id="id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateOrganizationDiscoveryDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new discovery domain for an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.discovery_domains.create(
    id="id",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — The domain name to associate with the organization e.g. acme.com.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[OrganizationDiscoveryDomainStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**use_for_organization_discovery:** `typing.Optional[bool]` — Indicates whether this domain should be used for organization discovery.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">get_by_name</a>(...) -&gt; AsyncHttpResponse[GetOrganizationDiscoveryDomainByNameResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single organization discovery domain specified by domain name.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.discovery_domains.get_by_name(
    id="id",
    discovery_domain="discovery_domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**discovery_domain:** `str` — Domain name of the discovery domain.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetOrganizationDiscoveryDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a single organization discovery domain specified by ID. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.discovery_domains.get(
    id="id",
    discovery_domain_id="discovery_domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**discovery_domain_id:** `str` — ID of the discovery domain.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a discovery domain from an organization. This action cannot be undone. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.discovery_domains.delete(
    id="id",
    discovery_domain_id="discovery_domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**discovery_domain_id:** `str` — ID of the discovery domain.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.discovery_domains.<a href="src/auth0/management/organizations/discovery_domains/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateOrganizationDiscoveryDomainResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the verification status and/or use_for_organization_discovery for an organization discovery domain. The <code>status</code> field must be either <code>pending</code> or <code>verified</code>. The <code>use_for_organization_discovery</code> field can be <code>true</code> or <code>false</code> (default: <code>true</code>).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.discovery_domains.update(
    id="id",
    discovery_domain_id="discovery_domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**discovery_domain_id:** `str` — ID of the discovery domain to update.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[OrganizationDiscoveryDomainStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**use_for_organization_discovery:** `typing.Optional[bool]` — Indicates whether this domain should be used for organization discovery.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations EnabledConnections
<details><summary><code>client.organizations.enabled_connections.<a href="src/auth0/management/organizations/enabled_connections/client.py">list</a>(...) -&gt; AsyncPager[
    OrganizationConnection,
    ListOrganizationConnectionsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a specific connection currently enabled for an Organization. Information returned includes details such as connection ID, name, strategy, and whether the connection automatically grants membership upon login.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.enabled_connections.list(
    id="id",
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.enabled_connections.<a href="src/auth0/management/organizations/enabled_connections/client.py">add</a>(...) -&gt; AsyncHttpResponse[AddOrganizationConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable a specific connection for a given Organization. To enable a connection, it must already exist within your tenant; connections cannot be created through this action.

<a href="https://auth0.com/docs/authenticate/identity-providers">Connections</a> represent the relationship between Auth0 and a source of users. Available types of connections include database, enterprise, and social.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.enabled_connections.add(
    id="id",
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Single connection ID to add to the organization.
    
</dd>
</dl>

<dl>
<dd>

**assign_membership_on_login:** `typing.Optional[bool]` — When true, all users that log in with this connection will be automatically granted membership in the organization. When false, users must be granted membership in the organization before logging in with this connection.
    
</dd>
</dl>

<dl>
<dd>

**is_signup_enabled:** `typing.Optional[bool]` — Determines whether organization signup should be enabled for this organization connection. Only applicable for database connections. Default: false.
    
</dd>
</dl>

<dl>
<dd>

**show_as_button:** `typing.Optional[bool]` — Determines whether a connection should be displayed on this organization’s login prompt. Only applicable for enterprise connections. Default: true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.enabled_connections.<a href="src/auth0/management/organizations/enabled_connections/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetOrganizationConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details about a specific connection currently enabled for an Organization. Information returned includes details such as connection ID, name, strategy, and whether the connection automatically grants membership upon login.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.enabled_connections.get(
    id="id",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Connection identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.enabled_connections.<a href="src/auth0/management/organizations/enabled_connections/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable a specific connection for an Organization. Once disabled, Organization members can no longer use that connection to authenticate. 

<b>Note</b>: This action does not remove the connection from your tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.enabled_connections.delete(
    id="id",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Connection identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.enabled_connections.<a href="src/auth0/management/organizations/enabled_connections/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateOrganizationConnectionResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the details of a specific connection currently enabled for an Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.enabled_connections.update(
    id="id",
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` — Connection identifier.
    
</dd>
</dl>

<dl>
<dd>

**assign_membership_on_login:** `typing.Optional[bool]` — When true, all users that log in with this connection will be automatically granted membership in the organization. When false, users must be granted membership in the organization before logging in with this connection.
    
</dd>
</dl>

<dl>
<dd>

**is_signup_enabled:** `typing.Optional[bool]` — Determines whether organization signup should be enabled for this organization connection. Only applicable for database connections. Default: false.
    
</dd>
</dl>

<dl>
<dd>

**show_as_button:** `typing.Optional[bool]` — Determines whether a connection should be displayed on this organization’s login prompt. Only applicable for enterprise connections. Default: true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations Invitations
<details><summary><code>client.organizations.invitations.<a href="src/auth0/management/organizations/invitations/client.py">list</a>(...) -&gt; AsyncPager[
    OrganizationInvitation,
    ListOrganizationInvitationsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a detailed list of invitations sent to users for a specific Organization. The list includes details such as inviter and invitee information, invitation URLs, and dates of creation and expiration. To learn more about Organization invitations, review <a href="https://auth0.com/docs/manage-users/organizations/configure-organizations/invite-members">Invite Organization Members</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.invitations.list(
    id="id",
    page=1,
    per_page=1,
    include_totals=True,
    fields="fields",
    include_fields=True,
    sort="sort",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — When true, return results inside an object that also contains the start and limit.  When false (default), a direct array of results is returned.  We do not yet support returning the total invitations count.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Use field:order where order is 1 for ascending and -1 for descending Defaults to created_at:-1.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.invitations.<a href="src/auth0/management/organizations/invitations/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateOrganizationInvitationResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a user invitation for a specific Organization. Upon creation, the listed user receives an email inviting them to join the Organization. To learn more about Organization invitations, review <a href="https://auth0.com/docs/manage-users/organizations/configure-organizations/invite-members">Invite Organization Members</a>. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    OrganizationInvitationInvitee,
    OrganizationInvitationInviter,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.invitations.create(
    id="id",
    inviter=OrganizationInvitationInviter(
        name="name",
    ),
    invitee=OrganizationInvitationInvitee(
        email="email",
    ),
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**inviter:** `OrganizationInvitationInviter` 
    
</dd>
</dl>

<dl>
<dd>

**invitee:** `OrganizationInvitationInvitee` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — Auth0 client ID. Used to resolve the application's login initiation endpoint.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — The id of the connection to force invitee to authenticate with.
    
</dd>
</dl>

<dl>
<dd>

**app_metadata:** `typing.Optional[AppMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**user_metadata:** `typing.Optional[UserMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**ttl_sec:** `typing.Optional[int]` — Number of seconds for which the invitation is valid before expiration. If unspecified or set to 0, this value defaults to 604800 seconds (7 days). Max value: 2592000 seconds (30 days).
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[str]]` — List of roles IDs to associated with the user.
    
</dd>
</dl>

<dl>
<dd>

**send_invitation_email:** `typing.Optional[bool]` — Whether the user will receive an invitation email (true) or no email (false), true by default
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.invitations.<a href="src/auth0/management/organizations/invitations/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetOrganizationInvitationResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.invitations.get(
    id="id",
    invitation_id="invitation_id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — The id of the user invitation.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.invitations.<a href="src/auth0/management/organizations/invitations/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.invitations.delete(
    id="id",
    invitation_id="invitation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**invitation_id:** `str` — The id of the user invitation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations Members
<details><summary><code>client.organizations.members.<a href="src/auth0/management/organizations/members/client.py">list</a>(...) -&gt; AsyncPager[OrganizationMember, ListOrganizationMembersPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List organization members.
This endpoint is subject to eventual consistency. New users may not be immediately included in the response and deleted users may not be immediately removed from it.

<ul>
  <li>
    Use the <code>fields</code> parameter to optionally define the specific member details retrieved. If <code>fields</code> is left blank, all fields (except roles) are returned.
  </li>
  <li>
    Member roles are not sent by default. Use <code>fields=roles</code> to retrieve the roles assigned to each listed member. To use this parameter, you must include the <code>read:organization_member_roles</code> scope in the token.
  </li>
</ul>

This endpoint supports two types of pagination:

- Offset pagination
- Checkpoint pagination

Checkpoint pagination must be used if you need to retrieve more than 1000 organization members.

<h2>Checkpoint Pagination</h2>

To search by checkpoint, use the following parameters: - from: Optional id from which to start selection. - take: The total amount of entries to retrieve when using the from parameter. Defaults to 50. Note: The first time you call this endpoint using Checkpoint Pagination, you should omit the <code>from</code> parameter. If there are more results, a <code>next</code> value will be included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, this indicates there are no more pages remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.members.list(
    id="id",
    from_="from",
    take=1,
    fields="fields",
    include_fields=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.members.<a href="src/auth0/management/organizations/members/client.py">create</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set one or more existing users as members of a specific <a href="https://auth0.com/docs/manage-users/organizations">Organization</a>.

To add a user to an Organization through this action, the user must already exist in your tenant. If a user does not yet exist, you can <a href="https://auth0.com/docs/manage-users/organizations/configure-organizations/invite-members">invite them to create an account</a>, manually create them through the Auth0 Dashboard, or use the Management API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.members.create(
    id="id",
    members=["members"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Sequence[str]` — List of user IDs to add to the organization as members.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.members.<a href="src/auth0/management/organizations/members/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.members.delete(
    id="id",
    members=["members"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Sequence[str]` — List of user IDs to remove from the organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations Members Roles
<details><summary><code>client.organizations.members.roles.<a href="src/auth0/management/organizations/members/roles/client.py">list</a>(...) -&gt; AsyncPager[Role, ListOrganizationMemberRolesOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list of roles assigned to a given user within the context of a specific Organization. 

Users can be members of multiple Organizations with unique roles assigned for each membership. This action only returns the roles associated with the specified Organization; any roles assigned to the user within other Organizations are not included.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.organizations.members.roles.list(
    id="id",
    user_id="user_id",
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — ID of the user to associate roles with.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.members.roles.<a href="src/auth0/management/organizations/members/roles/client.py">assign</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign one or more <a href="https://auth0.com/docs/manage-users/access-control/rbac">roles</a> to a user to determine their access for a specific Organization.

Users can be members of multiple Organizations with unique roles assigned for each membership. This action assigns roles to a user only for the specified Organization. Roles cannot be assigned to a user across multiple Organizations in the same call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.members.roles.assign(
    id="id",
    user_id="user_id",
    roles=["roles"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — ID of the user to associate roles with.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — List of roles IDs to associated with the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.members.roles.<a href="src/auth0/management/organizations/members/roles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one or more Organization-specific <a href="https://auth0.com/docs/manage-users/access-control/rbac">roles</a> from a given user.

Users can be members of multiple Organizations with unique roles assigned for each membership. This action removes roles from a user in relation to the specified Organization. Roles assigned to the user within a different Organization cannot be managed in the same call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.organizations.members.roles.delete(
    id="id",
    user_id="user_id",
    roles=["roles"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Organization identifier.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — User ID of the organization member to remove roles from.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — List of roles IDs associated with the organization member to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts Rendering
<details><summary><code>client.prompts.rendering.<a href="src/auth0/management/prompts/rendering/client.py">list</a>(...) -&gt; AsyncPager[
    ListAculsResponseContentItem, ListAculsOffsetPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get render setting configurations for all screens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.prompts.rendering.list(
    fields="fields",
    include_fields=True,
    page=1,
    per_page=1,
    include_totals=True,
    prompt="prompt",
    screen="screen",
    rendering_mode="advanced",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (default: true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Maximum value is 100, default value is 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total configuration count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Name of the prompt to filter by
    
</dd>
</dl>

<dl>
<dd>

**screen:** `typing.Optional[str]` — Name of the screen to filter by
    
</dd>
</dl>

<dl>
<dd>

**rendering_mode:** `typing.Optional[AculRenderingModeEnum]` — Rendering mode to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.rendering.<a href="src/auth0/management/prompts/rendering/client.py">bulk_update</a>(...) -&gt; AsyncHttpResponse[BulkUpdateAculResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Learn more about <a href='https://auth0.com/docs/customize/login-pages/advanced-customizations/getting-started/configure-acul-screens'>configuring render settings</a> for advanced customization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import AculConfigsItem, Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.rendering.bulk_update(
    configs=[
        AculConfigsItem(
            prompt="login",
            screen="login",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configs:** `AculConfigs` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.rendering.<a href="src/auth0/management/prompts/rendering/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetAculResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get render settings for a screen.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.rendering.get(
    prompt="login",
    screen="login",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PromptGroupNameEnum` — Name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**screen:** `ScreenGroupNameEnum` — Name of the screen
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.rendering.<a href="src/auth0/management/prompts/rendering/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateAculResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Learn more about <a href='https://auth0.com/docs/customize/login-pages/advanced-customizations/getting-started/configure-acul-screens'>configuring render settings</a> for advanced customization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.rendering.update(
    prompt="login",
    screen="login",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PromptGroupNameEnum` — Name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**screen:** `ScreenGroupNameEnum` — Name of the screen
    
</dd>
</dl>

<dl>
<dd>

**rendering_mode:** `typing.Optional[AculRenderingModeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**context_configuration:** `typing.Optional[AculContextConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**default_head_tags_disabled:** `typing.Optional[bool]` — Override Universal Login default head tags
    
</dd>
</dl>

<dl>
<dd>

**use_page_template:** `typing.Optional[bool]` — Use page template with ACUL
    
</dd>
</dl>

<dl>
<dd>

**head_tags:** `typing.Optional[typing.Sequence[AculHeadTag]]` — An array of head tags
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[AculFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts CustomText
<details><summary><code>client.prompts.custom_text.<a href="src/auth0/management/prompts/custom_text/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetCustomTextsByLanguageResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve custom text for a specific prompt and language.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.custom_text.get(
    prompt="login",
    language="am",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PromptGroupNameEnum` — Name of the prompt.
    
</dd>
</dl>

<dl>
<dd>

**language:** `PromptLanguageEnum` — Language to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.custom_text.<a href="src/auth0/management/prompts/custom_text/client.py">set</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set custom text for a specific prompt. Existing texts will be overwritten.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.custom_text.set(
    prompt="login",
    language="am",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PromptGroupNameEnum` — Name of the prompt.
    
</dd>
</dl>

<dl>
<dd>

**language:** `PromptLanguageEnum` — Language to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetsCustomTextsByLanguageRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts Partials
<details><summary><code>client.prompts.partials.<a href="src/auth0/management/prompts/partials/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetPartialsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get template partials for a prompt
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.partials.get(
    prompt="login",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PartialGroupsEnum` — Name of the prompt.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.partials.<a href="src/auth0/management/prompts/partials/client.py">set</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set template partials for a prompt
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.prompts.partials.set(
    prompt="login",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `PartialGroupsEnum` — Name of the prompt.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetPartialsRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RiskAssessments Settings
<details><summary><code>client.risk_assessments.settings.<a href="src/auth0/management/risk_assessments/settings/client.py">get</a>() -&gt; AsyncHttpResponse[GetRiskAssessmentsSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the tenant settings for risk assessments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.risk_assessments.settings.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.risk_assessments.settings.<a href="src/auth0/management/risk_assessments/settings/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateRiskAssessmentsSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the tenant settings for risk assessments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.risk_assessments.settings.update(
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enabled:** `bool` — Whether or not risk assessment is enabled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RiskAssessments Settings NewDevice
<details><summary><code>client.risk_assessments.settings.new_device.<a href="src/auth0/management/risk_assessments/settings/new_device/client.py">get</a>() -&gt; AsyncHttpResponse[GetRiskAssessmentsSettingsNewDeviceResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the risk assessment settings for the new device assessor
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.risk_assessments.settings.new_device.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.risk_assessments.settings.new_device.<a href="src/auth0/management/risk_assessments/settings/new_device/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateRiskAssessmentsSettingsNewDeviceResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the risk assessment settings for the new device assessor
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.risk_assessments.settings.new_device.update(
    remember_for=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**remember_for:** `int` — Length of time to remember devices for, in days.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles Permissions
<details><summary><code>client.roles.permissions.<a href="src/auth0/management/roles/permissions/client.py">list</a>(...) -&gt; AsyncPager[
    PermissionsResponsePayload,
    ListRolePermissionsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list (name, description, resource server) of permissions granted by a specified user role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.roles.permissions.list(
    id="id",
    per_page=1,
    page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to list granted permissions.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.permissions.<a href="src/auth0/management/roles/permissions/client.py">add</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add one or more <a href="https://auth0.com/docs/manage-users/access-control/configure-core-rbac/manage-permissions">permissions</a> to a specified user role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, PermissionRequestPayload

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.permissions.add(
    id="id",
    permissions=[
        PermissionRequestPayload(
            resource_server_identifier="resource_server_identifier",
            permission_name="permission_name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to add permissions to.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[PermissionRequestPayload]` — array of resource_server_identifier, permission_name pairs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.permissions.<a href="src/auth0/management/roles/permissions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one or more <a href="https://auth0.com/docs/manage-users/access-control/configure-core-rbac/manage-permissions">permissions</a> from a specified user role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, PermissionRequestPayload

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.permissions.delete(
    id="id",
    permissions=[
        PermissionRequestPayload(
            resource_server_identifier="resource_server_identifier",
            permission_name="permission_name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to remove permissions from.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[PermissionRequestPayload]` — array of resource_server_identifier, permission_name pairs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles Users
<details><summary><code>client.roles.users.<a href="src/auth0/management/roles/users/client.py">list</a>(...) -&gt; AsyncPager[RoleUser, ListRoleUsersPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve list of users associated with a specific role. For Dashboard instructions, review <a href="https://auth0.com/docs/manage-users/access-control/configure-core-rbac/roles/view-users-assigned-to-roles">View Users Assigned to Roles</a>.

This endpoint supports two types of pagination:
<ul>
<li>Offset pagination</li>
<li>Checkpoint pagination</li>
</ul>

Checkpoint pagination must be used if you need to retrieve more than 1000 organization members.

<h2>Checkpoint Pagination</h2>

To search by checkpoint, use the following parameters:
<ul>
<li><code>from</code>: Optional id from which to start selection.</li>
<li><code>take</code>: The total amount of entries to retrieve when using the from parameter. Defaults to 50.</li>
</ul>

<b>Note</b>: The first time you call this endpoint using checkpoint pagination, omit the <code>from</code> parameter. If there are more results, a <code>next</code> value is included in the response. You can use this for subsequent API calls. When <code>next</code> is no longer included in the response, no pages are remaining.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.roles.users.list(
    id="id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to retrieve a list of users associated with.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.users.<a href="src/auth0/management/roles/users/client.py">assign</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign one or more users to an existing user role. To learn more, review <a href="https://auth0.com/docs/manage-users/access-control/rbac">Role-Based Access Control</a>.

<b>Note</b>: New roles cannot be created through this action.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.roles.users.assign(
    id="id",
    users=["users"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the role to assign users to.
    
</dd>
</dl>

<dl>
<dd>

**users:** `typing.Sequence[str]` — user_id's of the users to assign the role to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SelfServiceProfiles CustomText
<details><summary><code>client.self_service_profiles.custom_text.<a href="src/auth0/management/self_service_profiles/custom_text/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListSelfServiceProfileCustomTextResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves text customizations for a given self-service profile, language and Self Service SSO Flow page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.custom_text.list(
    id="id",
    language="en",
    page="get-started",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile.
    
</dd>
</dl>

<dl>
<dd>

**language:** `SelfServiceProfileCustomTextLanguageEnum` — The language of the custom text.
    
</dd>
</dl>

<dl>
<dd>

**page:** `SelfServiceProfileCustomTextPageEnum` — The page where the custom text is shown.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.custom_text.<a href="src/auth0/management/self_service_profiles/custom_text/client.py">set</a>(...) -&gt; AsyncHttpResponse[SetSelfServiceProfileCustomTextResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates text customizations for a given self-service profile, language and Self Service SSO Flow page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.custom_text.set(
    id="id",
    language="en",
    page="get-started",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile.
    
</dd>
</dl>

<dl>
<dd>

**language:** `SelfServiceProfileCustomTextLanguageEnum` — The language of the custom text.
    
</dd>
</dl>

<dl>
<dd>

**page:** `SelfServiceProfileCustomTextPageEnum` — The page where the custom text is shown.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetSelfServiceProfileCustomTextRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SelfServiceProfiles SsoTicket
<details><summary><code>client.self_service_profiles.sso_ticket.<a href="src/auth0/management/self_service_profiles/sso_ticket/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateSelfServiceProfileSsoTicketResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an SSO access ticket to initiate the Self Service SSO Flow using a self-service profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.sso_ticket.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The id of the self-service profile to retrieve
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — If provided, this will allow editing of the provided connection during the SSO Flow
    
</dd>
</dl>

<dl>
<dd>

**connection_config:** `typing.Optional[SelfServiceProfileSsoTicketConnectionConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled_clients:** `typing.Optional[typing.Sequence[str]]` — List of client_ids that the connection will be enabled for.
    
</dd>
</dl>

<dl>
<dd>

**enabled_organizations:** `typing.Optional[typing.Sequence[SelfServiceProfileSsoTicketEnabledOrganization]]` — List of organizations that the connection will be enabled for.
    
</dd>
</dl>

<dl>
<dd>

**ttl_sec:** `typing.Optional[int]` — Number of seconds for which the ticket is valid before expiration. If unspecified or set to 0, this value defaults to 432000 seconds (5 days).
    
</dd>
</dl>

<dl>
<dd>

**domain_aliases_config:** `typing.Optional[SelfServiceProfileSsoTicketDomainAliasesConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**provisioning_config:** `typing.Optional[SelfServiceProfileSsoTicketProvisioningConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**use_for_organization_discovery:** `typing.Optional[bool]` — Indicates whether a verified domain should be used for organization discovery during authentication.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.self_service_profiles.sso_ticket.<a href="src/auth0/management/self_service_profiles/sso_ticket/client.py">revoke</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes an SSO access ticket and invalidates associated sessions. The ticket will no longer be accepted to initiate a Self-Service SSO session. If any users have already started a session through this ticket, their session will be terminated. Clients should expect a `202 Accepted` response upon successful processing, indicating that the request has been acknowledged and that the revocation is underway but may not be fully completed at the time of response. If the specified ticket does not exist, a `202 Accepted` response is also returned, signaling that no further action is required.
Clients should treat these `202` responses as an acknowledgment that the request has been accepted and is in progress, even if the ticket was not found.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.self_service_profiles.sso_ticket.revoke(
    profile_id="profileId",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` — The id of the self-service profile
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the ticket to revoke
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants Settings
<details><summary><code>client.tenants.settings.<a href="src/auth0/management/tenants/settings/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetTenantSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve tenant settings. A list of fields to include or exclude may also be specified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.tenants.settings.get(
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.settings.<a href="src/auth0/management/tenants/settings/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateTenantSettingsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update settings for a tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.tenants.settings.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**change_password:** `typing.Optional[TenantSettingsPasswordPage]` 
    
</dd>
</dl>

<dl>
<dd>

**device_flow:** `typing.Optional[TenantSettingsDeviceFlow]` 
    
</dd>
</dl>

<dl>
<dd>

**guardian_mfa_page:** `typing.Optional[TenantSettingsGuardianPage]` 
    
</dd>
</dl>

<dl>
<dd>

**default_audience:** `typing.Optional[str]` — Default audience for API Authorization.
    
</dd>
</dl>

<dl>
<dd>

**default_directory:** `typing.Optional[str]` — Name of connection used for password grants at the `/token` endpoint. The following connection types are supported: LDAP, AD, Database Connections, Passwordless, Windows Azure Active Directory, ADFS.
    
</dd>
</dl>

<dl>
<dd>

**error_page:** `typing.Optional[TenantSettingsErrorPage]` 
    
</dd>
</dl>

<dl>
<dd>

**default_token_quota:** `typing.Optional[DefaultTokenQuota]` 
    
</dd>
</dl>

<dl>
<dd>

**flags:** `typing.Optional[TenantSettingsFlags]` 
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` — Friendly name for this tenant.
    
</dd>
</dl>

<dl>
<dd>

**picture_url:** `typing.Optional[str]` — URL of logo to be shown for this tenant (recommended size: 150x150)
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — End-user support email.
    
</dd>
</dl>

<dl>
<dd>

**support_url:** `typing.Optional[str]` — End-user support url.
    
</dd>
</dl>

<dl>
<dd>

**allowed_logout_urls:** `typing.Optional[typing.Sequence[str]]` — URLs that are valid to redirect to after logout from Auth0.
    
</dd>
</dl>

<dl>
<dd>

**session_lifetime:** `typing.Optional[int]` — Number of hours a session will stay valid.
    
</dd>
</dl>

<dl>
<dd>

**idle_session_lifetime:** `typing.Optional[int]` — Number of hours for which a session can be inactive before the user must log in again.
    
</dd>
</dl>

<dl>
<dd>

**ephemeral_session_lifetime:** `typing.Optional[int]` — Number of hours an ephemeral (non-persistent) session will stay valid.
    
</dd>
</dl>

<dl>
<dd>

**idle_ephemeral_session_lifetime:** `typing.Optional[int]` — Number of hours for which an ephemeral (non-persistent) session can be inactive before the user must log in again.
    
</dd>
</dl>

<dl>
<dd>

**sandbox_version:** `typing.Optional[str]` — Selected sandbox version for the extensibility environment
    
</dd>
</dl>

<dl>
<dd>

**legacy_sandbox_version:** `typing.Optional[str]` — Selected legacy sandbox version for the extensibility environment
    
</dd>
</dl>

<dl>
<dd>

**default_redirection_uri:** `typing.Optional[str]` — The default absolute redirection uri, must be https
    
</dd>
</dl>

<dl>
<dd>

**enabled_locales:** `typing.Optional[typing.Sequence[TenantSettingsSupportedLocalesEnum]]` — Supported locales for the user interface
    
</dd>
</dl>

<dl>
<dd>

**session_cookie:** `typing.Optional[SessionCookieSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**sessions:** `typing.Optional[TenantSettingsSessions]` 
    
</dd>
</dl>

<dl>
<dd>

**oidc_logout:** `typing.Optional[TenantOidcLogoutSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**customize_mfa_in_postlogin_action:** `typing.Optional[bool]` — Whether to enable flexible factors for MFA in the PostLogin action
    
</dd>
</dl>

<dl>
<dd>

**allow_organization_name_in_authentication_api:** `typing.Optional[bool]` — Whether to accept an organization name instead of an ID on auth endpoints
    
</dd>
</dl>

<dl>
<dd>

**acr_values_supported:** `typing.Optional[typing.Sequence[str]]` — Supported ACR values
    
</dd>
</dl>

<dl>
<dd>

**mtls:** `typing.Optional[TenantSettingsMtls]` 
    
</dd>
</dl>

<dl>
<dd>

**pushed_authorization_requests_supported:** `typing.Optional[bool]` — Enables the use of Pushed Authorization Requests
    
</dd>
</dl>

<dl>
<dd>

**authorization_response_iss_parameter_supported:** `typing.Optional[bool]` — Supports iss parameter in authorization responses
    
</dd>
</dl>

<dl>
<dd>

**skip_non_verifiable_callback_uri_confirmation_prompt:** `typing.Optional[bool]` 

Controls whether a confirmation prompt is shown during login flows when the redirect URI uses non-verifiable callback URIs (for example, a custom URI schema such as `myapp://`, or `localhost`).
If set to true, a confirmation prompt will not be shown. We recommend that this is set to false for improved protection from malicious apps.
See https://auth0.com/docs/secure/security-guidance/measures-against-app-impersonation for more information.
    
</dd>
</dl>

<dl>
<dd>

**resource_parameter_profile:** `typing.Optional[TenantSettingsResourceParameterProfile]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_ai_guide:** `typing.Optional[bool]` — Whether Auth0 Guide (AI-powered assistance) is enabled for this tenant.
    
</dd>
</dl>

<dl>
<dd>

**phone_consolidated_experience:** `typing.Optional[bool]` — Whether Phone Consolidated Experience is enabled for this tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users AuthenticationMethods
<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">list</a>(...) -&gt; AsyncPager[
    UserAuthenticationMethod,
    ListUserAuthenticationMethodsOffsetPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list of authentication methods associated with a specified user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.authentication_methods.list(
    id="id",
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0. Default is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Default is 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateUserAuthenticationMethodResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an authentication method. Authentication methods created via this endpoint will be auto confirmed and should already have verification completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.create(
    id="id",
    type="phone",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user to whom the new authentication method will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreatedUserAuthenticationMethodTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A human-readable label to identify the authentication method.
    
</dd>
</dl>

<dl>
<dd>

**totp_secret:** `typing.Optional[str]` — Base32 encoded secret for TOTP generation.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — Applies to phone authentication methods only. The destination phone number used to send verification codes via text and voice.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Applies to email authentication methods only. The email address used to send verification messages.
    
</dd>
</dl>

<dl>
<dd>

**preferred_authentication_method:** `typing.Optional[PreferredAuthenticationMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `typing.Optional[str]` — Applies to webauthn authentication methods only. The id of the credential.
    
</dd>
</dl>

<dl>
<dd>

**public_key:** `typing.Optional[str]` — Applies to webauthn authentication methods only. The public key, which is encoded as base64.
    
</dd>
</dl>

<dl>
<dd>

**relying_party_identifier:** `typing.Optional[str]` — Applies to webauthn authentication methods only. The relying party identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">set</a>(...) -&gt; AsyncHttpResponse[typing.List[SetUserAuthenticationMethodResponseContent]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the specified user <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors"> authentication methods</a> with supplied values.

    <b>Note</b>: Authentication methods supplied through this action do not iterate on existing methods. Instead, any methods passed will overwrite the user&#8217s existing settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, SetUserAuthenticationMethods

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.set(
    id="id",
    request=[
        SetUserAuthenticationMethods(
            type="phone",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetUserAuthenticationMethodsRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">delete_all</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove all authentication methods (i.e., enrolled MFA factors) from the specified user account. This action cannot be undone. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.delete_all(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetUserAuthenticationMethodResponseContent]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.get(
    id="id",
    authentication_method_id="authentication_method_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**authentication_method_id:** `str` — The ID of the authentication methods in question.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the authentication method with the given ID from the specified user. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/manage-mfa-auth0-apis/manage-authentication-methods-with-management-api">Manage Authentication Methods with Management API</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.delete(
    id="id",
    authentication_method_id="authentication_method_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**authentication_method_id:** `str` — The ID of the authentication method to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.authentication_methods.<a href="src/auth0/management/users/authentication_methods/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateUserAuthenticationMethodResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify the authentication method with the given ID from the specified user. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/manage-mfa-auth0-apis/manage-authentication-methods-with-management-api">Manage Authentication Methods with Management API</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authentication_methods.update(
    id="id",
    authentication_method_id="authentication_method_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the user in question.
    
</dd>
</dl>

<dl>
<dd>

**authentication_method_id:** `str` — The ID of the authentication method to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A human-readable label to identify the authentication method.
    
</dd>
</dl>

<dl>
<dd>

**preferred_authentication_method:** `typing.Optional[PreferredAuthenticationMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Authenticators
<details><summary><code>client.users.authenticators.<a href="src/auth0/management/users/authenticators/client.py">delete_all</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove all authenticators registered to a given user ID, such as OTP, email, phone, and push-notification. This action cannot be undone. For more information, review <a href="https://auth0.com/docs/secure/multi-factor-authentication/manage-mfa-auth0-apis/manage-authentication-methods-with-management-api">Manage Authentication Methods with Management API</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.authenticators.delete_all(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users ConnectedAccounts
<details><summary><code>client.users.connected_accounts.<a href="src/auth0/management/users/connected_accounts/client.py">list</a>(...) -&gt; AsyncPager[ConnectedAccount, ListUserConnectedAccountsResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all connected accounts associated with the user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.connected_accounts.list(
    id="id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to list connected accounts for.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results to return.  Defaults to 10 with a maximum of 20
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Enrollments
<details><summary><code>client.users.enrollments.<a href="src/auth0/management/users/enrollments/client.py">get</a>(...) -&gt; AsyncHttpResponse[typing.List[UsersEnrollment]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the first <a href="https://auth0.com/docs/secure/multi-factor-authentication/multi-factor-authentication-factors">multi-factor authentication</a> enrollment that a specific user has confirmed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.enrollments.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to list enrollments for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users FederatedConnectionsTokensets
<details><summary><code>client.users.federated_connections_tokensets.<a href="src/auth0/management/users/federated_connections_tokensets/client.py">list</a>(...) -&gt; AsyncHttpResponse[typing.List[FederatedConnectionTokenSet]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active federated connections tokensets for a provided user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.federated_connections_tokensets.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — User identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.federated_connections_tokensets.<a href="src/auth0/management/users/federated_connections_tokensets/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.federated_connections_tokensets.delete(
    id="id",
    tokenset_id="tokenset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the user that owns the tokenset
    
</dd>
</dl>

<dl>
<dd>

**tokenset_id:** `str` — The tokenset id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Groups
<details><summary><code>client.users.groups.<a href="src/auth0/management/users/groups/client.py">get</a>(...) -&gt; AsyncPager[UserGroupsResponseSchema, GetUserGroupsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all groups to which this user belongs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.groups.get(
    id="id",
    fields="fields",
    include_fields=True,
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to list groups for.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — A comma separated list of fields to include or exclude (depending on include_fields) from the result, empty to retrieve all fields
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false).
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Identities
<details><summary><code>client.users.identities.<a href="src/auth0/management/users/identities/client.py">link</a>(...) -&gt; AsyncHttpResponse[typing.List[UserIdentity]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link two user accounts together forming a primary and secondary relationship. On successful linking, the endpoint returns the new array of the primary account identities.

Note: There are two ways of invoking the endpoint:

<ul>
  <li>With the authenticated primary account's JWT in the Authorization header, which has the <code>update:current_user_identities</code> scope:
    <pre>
      POST /api/v2/users/PRIMARY_ACCOUNT_USER_ID/identities
      Authorization: "Bearer PRIMARY_ACCOUNT_JWT"
      {
        "link_with": "SECONDARY_ACCOUNT_JWT"
      }
    </pre>
    In this case, only the <code>link_with</code> param is required in the body, which also contains the JWT obtained upon the secondary account's authentication.
  </li>
  <li>With a token generated by the API V2 containing the <code>update:users</code> scope:
    <pre>
    POST /api/v2/users/PRIMARY_ACCOUNT_USER_ID/identities
    Authorization: "Bearer YOUR_API_V2_TOKEN"
    {
      "provider": "SECONDARY_ACCOUNT_PROVIDER",
      "connection_id": "SECONDARY_ACCOUNT_CONNECTION_ID(OPTIONAL)",
      "user_id": "SECONDARY_ACCOUNT_USER_ID"
    }
    </pre>
    In this case you need to send <code>provider</code> and <code>user_id</code> in the body. Optionally you can also send the <code>connection_id</code> param which is suitable for identifying a particular database connection for the 'auth0' provider.
  </li>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.identities.link(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the primary user account to link a second user account to.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[UserIdentityProviderEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — connection_id of the secondary user account being linked when more than one `auth0` database provider exists.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[UserId]` 
    
</dd>
</dl>

<dl>
<dd>

**link_with:** `typing.Optional[str]` — JWT for the secondary account being linked. If sending this parameter, `provider`, `user_id`, and `connection_id` must not be sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.identities.<a href="src/auth0/management/users/identities/client.py">delete</a>(...) -&gt; AsyncHttpResponse[DeleteUserIdentityResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlink a specific secondary account from a target user. This action requires the ID of both the target user and the secondary account. 

Unlinking the secondary account removes it from the identities array of the target user and creates a new standalone profile for the secondary account. To learn more, review <a href="https://auth0.com/docs/manage-users/user-accounts/user-account-linking/unlink-user-accounts">Unlink User Accounts</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.identities.delete(
    id="id",
    provider="ad",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the primary user account.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `UserIdentityProviderEnum` — Identity provider name of the secondary linked account (e.g. `google-oauth2`).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — ID of the secondary linked account (e.g. `123456789081523216417` part after the `|` in `google-oauth2|123456789081523216417`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Logs
<details><summary><code>client.users.logs.<a href="src/auth0/management/users/logs/client.py">list</a>(...) -&gt; AsyncPager[Log, UserListLogOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve log events for a specific user.

Note: For more information on all possible event types, their respective acronyms and descriptions, see <a href="https://auth0.com/docs/logs/log-event-type-codes">Log Event Type Codes</a>.

For more information on the list of fields that can be used in `sort`, see <a href="https://auth0.com/docs/logs/log-search-query-syntax#searchable-fields">Searchable Fields</a>.

Auth0 <a href="https://auth0.com/docs/logs/retrieve-log-events-using-mgmt-api#limitations">limits the number of logs</a> you can return by search criteria to 100 logs per request. Furthermore, you may only paginate through up to 1,000 search results. If you exceed this threshold, please redefine your search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.logs.list(
    id="id",
    page=1,
    per_page=1,
    sort="sort",
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user of the logs to retrieve
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Paging is disabled if parameter not sent.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Use `fieldname:1` for ascending order and `fieldname:-1` for descending.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Multifactor
<details><summary><code>client.users.multifactor.<a href="src/auth0/management/users/multifactor/client.py">invalidate_remember_browser</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate all remembered browsers across all <a href="https://auth0.com/docs/multifactor-authentication">authentication factors</a> for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.multifactor.invalidate_remember_browser(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to invalidate all remembered browsers and authentication factors for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.multifactor.<a href="src/auth0/management/users/multifactor/client.py">delete_provider</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a <a href="https://auth0.com/docs/multifactor-authentication">multifactor</a> authentication configuration from a user's account. This forces the user to manually reconfigure the multi-factor provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.multifactor.delete_provider(
    id="id",
    provider="duo",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to remove a multifactor configuration from.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `UserMultifactorProviderEnum` — The multi-factor provider. Supported values 'duo' or 'google-authenticator'
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Organizations
<details><summary><code>client.users.organizations.<a href="src/auth0/management/users/organizations/client.py">list</a>(...) -&gt; AsyncPager[Organization, ListUserOrganizationsOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve list of the specified user's current Organization memberships. User must be specified by user ID. For more information, review <a href="https://auth0.com/docs/manage-users/organizations">Auth0 Organizations</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.organizations.list(
    id="id",
    page=1,
    per_page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to retrieve the organizations for.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Permissions
<details><summary><code>client.users.permissions.<a href="src/auth0/management/users/permissions/client.py">list</a>(...) -&gt; AsyncPager[
    UserPermissionSchema, ListUserPermissionsOffsetPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all permissions associated with the user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.permissions.list(
    id="id",
    per_page=1,
    page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to retrieve the permissions for.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.permissions.<a href="src/auth0/management/users/permissions/client.py">create</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign permissions to a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, PermissionRequestPayload

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.permissions.create(
    id="id",
    permissions=[
        PermissionRequestPayload(
            resource_server_identifier="resource_server_identifier",
            permission_name="permission_name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to assign permissions to.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[PermissionRequestPayload]` — List of permissions to add to this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.permissions.<a href="src/auth0/management/users/permissions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove permissions from a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0, PermissionRequestPayload

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.permissions.delete(
    id="id",
    permissions=[
        PermissionRequestPayload(
            resource_server_identifier="resource_server_identifier",
            permission_name="permission_name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to remove permissions from.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[PermissionRequestPayload]` — List of permissions to remove from this user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users RiskAssessments
<details><summary><code>client.users.risk_assessments.<a href="src/auth0/management/users/risk_assessments/client.py">clear</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clear risk assessment assessors for a specific user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.risk_assessments.clear(
    id="id",
    connection="connection",
    assessors=["new-device"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to clear assessors for.
    
</dd>
</dl>

<dl>
<dd>

**connection:** `str` — The name of the connection containing the user whose assessors should be cleared.
    
</dd>
</dl>

<dl>
<dd>

**assessors:** `typing.Sequence[AssessorsTypeEnum]` — List of assessors to clear.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Roles
<details><summary><code>client.users.roles.<a href="src/auth0/management/users/roles/client.py">list</a>(...) -&gt; AsyncPager[Role, ListUserRolesOffsetPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed list of all user roles currently assigned to a user.

<b>Note</b>: This action retrieves all roles assigned to a user in the context of your whole tenant. To retrieve Organization-specific roles, use the following endpoint: <a href="https://auth0.com/docs/api/management/v2/organizations/get-organization-member-roles">Get user roles assigned to an Organization member</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.roles.list(
    id="id",
    per_page=1,
    page=1,
    include_totals=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to list roles for.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page index of the results to return. First page is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_totals:** `typing.Optional[bool]` — Return results inside an object that contains the total result count (true) or as a direct array of results (false, default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.roles.<a href="src/auth0/management/users/roles/client.py">assign</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign one or more existing user roles to a user. For more information, review <a href="https://auth0.com/docs/manage-users/access-control/rbac">Role-Based Access Control</a>.

<b>Note</b>: New roles cannot be created through this action. Additionally, this action is used to assign roles to a user in the context of your whole tenant. To assign roles in the context of a specific Organization, use the following endpoint: <a href="https://auth0.com/docs/api/management/v2/organizations/post-organization-member-roles">Assign user roles to an Organization member</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.roles.assign(
    id="id",
    roles=["roles"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to associate roles with.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — List of roles IDs to associated with the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.roles.<a href="src/auth0/management/users/roles/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one or more specified user roles assigned to a user.

<b>Note</b>: This action removes a role from a user in the context of your whole tenant. If you want to unassign a role from a user in the context of a specific Organization, use the following endpoint: <a href="https://auth0.com/docs/api/management/v2/organizations/delete-organization-member-roles">Delete user roles from an Organization member</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.roles.delete(
    id="id",
    roles=["roles"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to remove roles from.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — List of roles IDs to remove from the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users RefreshToken
<details><summary><code>client.users.refresh_token.<a href="src/auth0/management/users/refresh_token/client.py">list</a>(...) -&gt; AsyncPager[
    RefreshTokenResponseContent, ListRefreshTokensPaginatedResponseContent
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a user's refresh tokens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.refresh_token.list(
    user_id="user_id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user to get refresh tokens for
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.refresh_token.<a href="src/auth0/management/users/refresh_token/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all refresh tokens for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.refresh_token.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user to get remove refresh tokens for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Sessions
<details><summary><code>client.users.sessions.<a href="src/auth0/management/users/sessions/client.py">list</a>(...) -&gt; AsyncPager[SessionResponseContent, ListUserSessionsPaginatedResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a user's sessions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.users.sessions.list(
    user_id="user_id",
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user to get sessions for
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.sessions.<a href="src/auth0/management/users/sessions/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all sessions for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.users.sessions.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — ID of the user to get sessions for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## VerifiableCredentials Verification Templates
<details><summary><code>client.verifiable_credentials.verification.templates.<a href="src/auth0/management/verifiable_credentials/verification/templates/client.py">list</a>(...) -&gt; AsyncPager[
    VerifiableCredentialTemplateResponse,
    ListVerifiableCredentialTemplatesPaginatedResponseContent,
]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List a verifiable credential templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
response = client.verifiable_credentials.verification.templates.list(
    from_="from",
    take=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — Optional Id from which to start selection.
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable_credentials.verification.templates.<a href="src/auth0/management/verifiable_credentials/verification/templates/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateVerifiableCredentialTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a verifiable credential template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import (
    Auth0,
    MdlPresentationProperties,
    MdlPresentationRequest,
    MdlPresentationRequestProperties,
)

client = Auth0(
    token="YOUR_TOKEN",
)
client.verifiable_credentials.verification.templates.create(
    name="name",
    type="type",
    dialect="dialect",
    presentation=MdlPresentationRequest(
        org_iso_18013_5_1_m_dl=MdlPresentationRequestProperties(
            org_iso_18013_5_1=MdlPresentationProperties(),
        ),
    ),
    well_known_trusted_issuers="well_known_trusted_issuers",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dialect:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**presentation:** `MdlPresentationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**well_known_trusted_issuers:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**custom_certificate_authority:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable_credentials.verification.templates.<a href="src/auth0/management/verifiable_credentials/verification/templates/client.py">get</a>(...) -&gt; AsyncHttpResponse[GetVerifiableCredentialTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a verifiable credential template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.verifiable_credentials.verification.templates.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the template to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable_credentials.verification.templates.<a href="src/auth0/management/verifiable_credentials/verification/templates/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a verifiable credential template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.verifiable_credentials.verification.templates.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the template to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifiable_credentials.verification.templates.<a href="src/auth0/management/verifiable_credentials/verification/templates/client.py">update</a>(...) -&gt; AsyncHttpResponse[UpdateVerifiableCredentialTemplateResponseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a verifiable credential template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0 import Auth0

client = Auth0(
    token="YOUR_TOKEN",
)
client.verifiable_credentials.verification.templates.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the template to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dialect:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**presentation:** `typing.Optional[MdlPresentationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**well_known_trusted_issuers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

