# Change Log

## [4.2.0](https://github.com/auth0/auth0-python/tree/4.2.0) (2023-05-02)
[Full Changelog](https://github.com/auth0/auth0-python/compare/4.1.1...4.2.0)

**Added**
- Add cache_ttl param to AsymmetricSignatureVerifier [\#490](https://github.com/auth0/auth0-python/pull/490) ([matei-radu](https://github.com/matei-radu))

## [4.1.1](https://github.com/auth0/auth0-python/tree/4.1.1) (2023-04-13)
[Full Changelog](https://github.com/auth0/auth0-python/compare/4.1.0...4.1.1)

**Fixed**
- Make pw realm params optional [\#484](https://github.com/auth0/auth0-python/pull/484) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Fix intellisense on Auth0 class [\#486](https://github.com/auth0/auth0-python/pull/486) ([adamjmcgrath](https://github.com/adamjmcgrath))

## [4.1.0](https://github.com/auth0/auth0-python/tree/4.1.0) (2023-03-14)
[Full Changelog](https://github.com/auth0/auth0-python/compare/4.0.0...4.1.0)

**Added**
- Add branding theme endpoints [\#477](https://github.com/auth0/auth0-python/pull/477) ([adamjmcgrath](https://github.com/adamjmcgrath))
- [SDK-4011]  Add API2 Factor Management Endpoints [\#476](https://github.com/auth0/auth0-python/pull/476) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Use declarative setup with `pyproject.toml` [\#474](https://github.com/auth0/auth0-python/pull/474) ([Viicos](https://github.com/Viicos))

## [4.0.0](https://github.com/auth0/auth0-python/tree/4.0.0) (2023-01-19)
[Full Changelog](https://github.com/auth0/auth0-python/compare/3.24.1...4.0.0)

**Added**
- Add support for private_key_jwt [\#456](https://github.com/auth0/auth0-python/pull/456) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Add support for managing client credentials [\#459](https://github.com/auth0/auth0-python/pull/459) ([adamjmcgrath](https://github.com/adamjmcgrath))

**Security**
- Update pyjwt [\#460](https://github.com/auth0/auth0-python/pull/460) ([adamjmcgrath](https://github.com/adamjmcgrath))

**Changed**
- Publish Python Support Schedule [\#454](https://github.com/auth0/auth0-python/pull/454) ([evansims](https://github.com/evansims))

**⚠️ BREAKING CHANGES**
- Remove deprecated methods [\#461](https://github.com/auth0/auth0-python/pull/461) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Remove v3 folder [\#462](https://github.com/auth0/auth0-python/pull/462) ([adamjmcgrath](https://github.com/adamjmcgrath))

See the [V4_MIGRATION_GUIDE](https://github.com/auth0/auth0-python/blob/master/V4_MIGRATION_GUIDE.md) for more info.

## [3.24.1](https://github.com/auth0/auth0-python/tree/3.24.1) (2023-01-19)
[Full Changelog](https://github.com/auth0/auth0-python/compare/3.24.0...3.24.1)

**Fixed**
- Remove unnecessary type param from update_template_universal_login [\#463](https://github.com/auth0/auth0-python/pull/463) ([adamjmcgrath](https://github.com/adamjmcgrath))

## [3.24.0](https://github.com/auth0/auth0-python/tree/3.24.0) (2022-10-17)
[Full Changelog](https://github.com/auth0/auth0-python/compare/3.23.1...3.24.0)

**Added**
- [SDK-3714] Async token verifier [\#445](https://github.com/auth0/auth0-python/pull/445) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Add AsyncAuth0 to share a session among many services [\#443](https://github.com/auth0/auth0-python/pull/443) ([adamjmcgrath](https://github.com/adamjmcgrath))

**Fixed**
- Bugfix 414 missing import [\#442](https://github.com/auth0/auth0-python/pull/442) ([adamjmcgrath](https://github.com/adamjmcgrath))

## [3.23.1](https://github.com/auth0/auth0-python/tree/3.23.1) (2022-06-10)
[Full Changelog](https://github.com/auth0/auth0-python/compare/3.23.0...3.23.1)

**Fixed**
- Pass rest_options through Auth0 constructor [\#354](https://github.com/auth0/auth0-python/pull/354) ([adamjmcgrath](https://github.com/adamjmcgrath))


3.23.0
------------------

**Added**
- Asyncio Support [\#312](https://github.com/auth0/auth0-python/pull/312) ([adamjmcgrath](https://github.com/adamjmcgrath))
- Add `/api/v2/branding` endpoints support [\#313](https://github.com/auth0/auth0-python/pull/313) ([evansims](https://github.com/evansims))

3.22.0
------------------

**Added**
- [SDK-3174] Add `DELETE` method for `/api/v2/users/{id}/authenticators` endpoint [\#301](https://github.com/auth0/auth0-python/pull/301) ([akmjenkins](https://github.com/akmjenkins))
- [SDK-3175] Return token claims in TokenVerifier.verify() [\#273](https://github.com/auth0/auth0-python/pull/273) ([bisguzar](https://github.com/bisguzar))

**Fixed**
- [SDK-3173] Default to 'None' for `deployed` on GET /api/v2/actions/actions endpoint [\#309](https://github.com/auth0/auth0-python/pull/309) ([evansims](https://github.com/evansims))

3.21.0
------------------

**Added**
- Add pagination to device credentials [\#300](https://github.com/auth0/auth0-python/pull/300) ([fionnulak](https://github.com/fionnulak))

3.20.0
------------------

**Added**
- Add attack protection endpoints [\#303](https://github.com/auth0/auth0-python/pull/303) ([adamjmcgrath](https://github.com/adamjmcgrath))

3.19.0
------------------

**Added**
- Add actions to Auth0 class [\#293](https://github.com/auth0/auth0-python/pull/293) ([jrzerr](https://github.com/jrzerr))
- Added support for prompts API [\#291](https://github.com/auth0/auth0-python/pull/291) ([lorinkoz](https://github.com/lorinkoz))

**Changed**
- Remove references to ID token in generic token classes [\#295](https://github.com/auth0/auth0-python/pull/295) ([lbalmaceda](https://github.com/lbalmaceda))

**Fixed**
- Use assertNotEqual instead of assertNotEquals for Python 3.11 compatibility. [\#294](https://github.com/auth0/auth0-python/pull/294) ([tirkarthi](https://github.com/tirkarthi))

3.18.0
------------------

**Added**
- [SDK-2720] Add support for actions APIs [\#289](https://github.com/auth0/auth0-python/pull/289) ([jimmyjames](https://github.com/jimmyjames))

3.17.0
------------------

**Added**
- Make the CI fail when the docs syntax is invalid [\#287](https://github.com/auth0/auth0-python/pull/287) ([lbalmaceda](https://github.com/lbalmaceda))
- [SDK-2687] Implement automatic rate-limit handling [\#285](https://github.com/auth0/auth0-python/pull/285) ([evansims](https://github.com/evansims))
- Use Sphinx to generate API docs [\#281](https://github.com/auth0/auth0-python/pull/281) ([lbalmaceda](https://github.com/lbalmaceda))
- Add Passwordless Login function [\#279](https://github.com/auth0/auth0-python/pull/279) ([lbalmaceda](https://github.com/lbalmaceda))
- [SDK 2665] Update endpoint methods to support 'from' and 'take' checkpoint pagination parameters, where appropriate [\#278](https://github.com/auth0/auth0-python/pull/278) ([evansims](https://github.com/evansims))

**Deprecated**
- Deprecate /oauth/ro for passwordless [\#280](https://github.com/auth0/auth0-python/pull/280) ([lbalmaceda](https://github.com/lbalmaceda))

3.16.2
------------------

**Fixed**
- Re-Route Job Results endpoint [\#275](https://github.com/auth0/auth0-python/pull/275) ([lbalmaceda](https://github.com/lbalmaceda))

3.16.1
------------------

**Fixed**
- Remove requirements.txt file [\#270](https://github.com/auth0/auth0-python/pull/270) ([lbalmaceda](https://github.com/lbalmaceda))
- Repair Organisation get by name URL. [\#269](https://github.com/auth0/auth0-python/pull/269) ([queenvictoria](https://github.com/queenvictoria))

3.16.0
------------------

**Added**
- Add access token validation guidance for organizations [\#262](https://github.com/auth0/auth0-python/pull/262) ([lbalmaceda](https://github.com/lbalmaceda))
- Add support for Organization MGMT API endpoints [SDK-2439] [\#261](https://github.com/auth0/auth0-python/pull/261) ([lbalmaceda](https://github.com/lbalmaceda))
- Add scope to refresh_token [\#256](https://github.com/auth0/auth0-python/pull/256) ([criles25](https://github.com/criles25))
- Allow configuration of outgoing request protocol [\#254](https://github.com/auth0/auth0-python/pull/254) ([garry-jeromson](https://github.com/garry-jeromson))

3.15.0
------------------

**Added**
- Add support for organizations feature [\#258](https://github.com/auth0/auth0-python/pull/258) ([jimmyjames](https://github.com/jimmyjames))

3.14.0
------------------

**Added**
- Adds a new user method invalidate_remembered_browsers [\#248](https://github.com/auth0/auth0-python/pull/248) ([kpurdon](https://github.com/kpurdon))

3.13.0
------------------

**Added**
- Add support for Log Streams API [\#236](https://github.com/auth0/auth0-python/pull/236) ([lbalmaceda](https://github.com/lbalmaceda))

**Fixed**
- Fix imports on the management/__init__.py file [\#235](https://github.com/auth0/auth0-python/pull/235) ([matthewarmand](https://github.com/matthewarmand))

3.12.0
------------------

**Added**
- Add missing user profile properties to the signup endpoint [\#231](https://github.com/auth0/auth0-python/pull/231) ([lbalmaceda](https://github.com/lbalmaceda))
- Add Hooks management API [\#227](https://github.com/auth0/auth0-python/pull/227) ([guillp](https://github.com/guillp))
- Add missing external_id property to the import users job [\#222](https://github.com/auth0/auth0-python/pull/222) ([lbalmaceda](https://github.com/lbalmaceda))

**Changed**
- Remove iat claim value check [\#223](https://github.com/auth0/auth0-python/pull/223) ([lbalmaceda](https://github.com/lbalmaceda))

**Fixed**
- Skip sending optional parameters on POST request when unspecified [\#230](https://github.com/auth0/auth0-python/pull/230) ([lbalmaceda](https://github.com/lbalmaceda))

3.11.0
------------------

**Added**
- Add send_completion_email to users import job [\#220](https://github.com/auth0/auth0-python/pull/220) ([lbalmaceda](https://github.com/lbalmaceda))
- Expose the time at which the Rate Limit will reset [\#219](https://github.com/auth0/auth0-python/pull/219) ([lbalmaceda](https://github.com/lbalmaceda))

**Removed**
- Add deprecation note for DELETE /users (all users) [\#217](https://github.com/auth0/auth0-python/pull/217) ([lbalmaceda](https://github.com/lbalmaceda))

3.10.0
------------------

**Security**
- Improved OIDC compliance [\#213](https://github.com/auth0/auth0-python/pull/213) ([lbalmaceda](https://github.com/lbalmaceda))

**Added**
- Add connect/read timeout option [\#215](https://github.com/auth0/auth0-python/pull/215) ([lbalmaceda](https://github.com/lbalmaceda))

3.9.2
------------------

**Fixed**
- Accept client_secret as passwordless/start param [\#211](https://github.com/auth0/auth0-python/pull/211) ([lbalmaceda](https://github.com/lbalmaceda))

3.9.1
------------------

**Changed**
- Update minimum "requests" version to 2.14.0 [\#204](https://github.com/auth0/auth0-python/pull/204) ([lbalmaceda](https://github.com/lbalmaceda))

3.9.0
------------------

**Added**
- Add Roles and Permissions endpoints [\#202](https://github.com/auth0/auth0-python/pull/202) ([lbalmaceda](https://github.com/lbalmaceda))

3.8.1
------------------

July 18, 2019: This release included an unintentionally breaking change affecting those users that were manually parsing the response from GET requests. e.g. /userinfo or /authorize. The `AuthenticationBase#get` method was incorrectly parsing the request result into a String. 

From this release on, making a GET request returns a Dictionary instead.

**Breaking Change**
- Fix request creation when headers are the default [\#198](https://github.com/auth0/auth0-python/pull/198) ([lbalmaceda](https://github.com/lbalmaceda)).


3.8.0
------------------

**Fixed**
- rules_config.unset fix [\#195](https://github.com/auth0/auth0-python/pull/195) ([jhunken](https://github.com/jhunken))

**Security**
- Update requests dependency to latest version [\#196](https://github.com/auth0/auth0-python/pull/196) ([lbalmaceda](https://github.com/lbalmaceda))

3.7.2
------------------

**Fixed**
- Fix HTTP method used for rotating Client secret [\#191](https://github.com/auth0/auth0-python/pull/191) ([lbalmaceda](https://github.com/lbalmaceda))

3.7.1
------------------

**Fixed**
- Update telemetry format [\#187](https://github.com/auth0/auth0-python/pull/187) ([lbalmaceda](https://github.com/lbalmaceda))


3.7.0
------------------

**Changed**
- Remove default value for search_engine [\#185](https://github.com/auth0/auth0-python/pull/185) ([lbalmaceda](https://github.com/lbalmaceda))


3.6.1
------------------

**Fixed**
- Fixed Management API Grants class instantiation [\#179](https://github.com/auth0/auth0-python/pull/179) ([beck3905](https://github.com/beck3905))


3.6.0
------------------

**Added**
- Add grants, custom domains, rules_configs to API [\#177](https://github.com/auth0/auth0-python/pull/177) ([sagnew-dg](https://github.com/sagnew-dg))


3.5.0
------------------

**Added**
- Add Revoke Refresh Token endpoint [\#170](https://github.com/auth0/auth0-python/pull/170) ([lbalmaceda](https://github.com/lbalmaceda))
- Add /dbconnections/signup with username and metadata [\#169](https://github.com/auth0/auth0-python/pull/169) ([lbalmaceda](https://github.com/lbalmaceda))


3.4.0
------------------

**Added**
- Add `client_id` param to ClientGrants.all [\#159](https://github.com/auth0/auth0-python/pull/159) ([danishprakash](https://github.com/danishprakash))
- Add telemetry headers to AuthenticationBase [\#152](https://github.com/auth0/auth0-python/pull/152) ([crgk](https://github.com/crgk))
- Add pre-commit pypgrade hook and update supported versions [\#124](https://github.com/auth0/auth0-python/pull/124) ([hugovk](https://github.com/hugovk))
- Implemented delete_user_by_email and test for connections [\#122](https://github.com/auth0/auth0-python/pull/122) ([runz0rd](https://github.com/runz0rd))
- Adds user export job creation. [\#112](https://github.com/auth0/auth0-python/pull/112) ([dmark](https://github.com/dmark))

**Changed**
- String Formatting Updated [\#141](https://github.com/auth0/auth0-python/pull/141) ([vkmrishad](https://github.com/vkmrishad))
- Uses Python built-in modules to retrieve Python and auth0-python version number [\#125](https://github.com/auth0/auth0-python/pull/125) ([edawine](https://github.com/edawine))

**Fixed**
- Stop lower-casing email on user search [\#167](https://github.com/auth0/auth0-python/pull/167) ([helmus](https://github.com/helmus))
- Always include Content-Type header in management requests [\#158](https://github.com/auth0/auth0-python/pull/158) ([crgk](https://github.com/crgk))


3.3.0
------------------

**Added**
- Add pagination to Clients and Connections
- Add pagination to Client Grants, Resource Servers and Rules
- Add Email-Templates Management API endpoints

**Fixed**
- Replace default mutable arguments with None
- Fix JSON error message handling for Management API


3.2.2
------------------

**Fixed**
- Upload the correct package contents to Pypi.


3.2.0
------------------

**Added**
- Raise Auth0Error for bad status code [\#98](https://github.com/auth0/auth0-python/pull/98) ([beck3905](https://github.com/beck3905))

**Fixed**
- Correctly throw an exception when handing a text response [\#92](https://github.com/auth0/auth0-python/pull/92) ([benbc](https://github.com/benbc))
- Instantiate UserBlocks for consistency [\#90](https://github.com/auth0/auth0-python/pull/90) ([mattdodge](https://github.com/mattdodge))

3.1.4
------------------

Authentication API
- Improve handling of inconsistent API error responses.

3.1.3
------------------

Management API
- Added `upsert` parameter to `import_users` job.

3.1.2
------------------

Authentication API
- Added `refresh_token` method to get_token

3.1.0
------------------

Authentication API
- Added Logout Functionality

3.0.0 
------------------

Authentication API
- Added Support for API Authorization. `oauth/token` endpoint
  - Client Credentials Grant
  - Authorization Code Grant
  - Authorization Code PKCE Grant
  - Resource Owner Password Realm Grant
- Added Support for API Authorization. `authorize` endpoint
  - Authorization Code Grant

Management API v2
- Added Support for Guardian   
- Added Support to retrieve Logs
- Added Support to manage Resource Servers
- Added Support to manage Client Grants
- Added Support to manage User blocks 
