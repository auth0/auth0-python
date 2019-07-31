Changes
=======

3.9.0
------------------

**Added**
- Add Roles and Permissions endpoints [\#202](https://github.com/auth0/auth0-python/pull/202) ([lbalmaceda](https://github.com/lbalmaceda))

3.8.1
------------------

July 18, 2019: This release included a breaking change affecting those users that were manually parsing the response from GET requests. e.g. /userinfo or /authorize. The `AuthenticationBase#get` method was incorrectly parsing the request result into a String. 

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
