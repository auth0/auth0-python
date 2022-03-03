from .base import AuthenticationBase


class GetToken(AuthenticationBase):

    """/oauth/token related endpoints

    Args:
        domain (str): Your auth0 domain (e.g: username.auth0.com)
    """

    def authorization_code(self, client_id, client_secret, code,
                           redirect_uri, grant_type='authorization_code',
                           timeout=5.0):
        """Authorization code grant

        This is the OAuth 2.0 grant that regular web apps utilize in order
        to access an API. Use this endpoint to exchange an Authorization Code
        for a Token.

        Args:
            grant_type (str): Denotes the flow you're using. For authorization code
            use authorization_code

            client_id (str): your application's client Id

            client_secret (str): your application's client Secret

            code (str): The Authorization Code received from the /authorize Calls

            redirect_uri (str, optional): This is required only if it was set at
            the GET /authorize endpoint. The values must match

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token, id_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'code': code,
                'grant_type': grant_type,
                'redirect_uri': redirect_uri,
            },
            timeout=timeout
        )

    def authorization_code_pkce(self, client_id, code_verifier, code,
                                redirect_uri, grant_type='authorization_code',
                                timeout=5.0):
        """Authorization code pkce grant

        This is the OAuth 2.0 grant that mobile apps utilize in order to access an API.
        Use this endpoint to exchange an Authorization Code for a Token.

        Args:
            grant_type (str): Denotes the flow you're using. For authorization code pkce
            use authorization_code

            client_id (str): your application's client Id

            code_verifier (str): Cryptographically random key that was used to generate
            the code_challenge passed to /authorize.

            code (str): The Authorization Code received from the /authorize Calls

            redirect_uri (str, optional): This is required only if it was set at
            the GET /authorize endpoint. The values must match

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token, id_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'code_verifier': code_verifier,
                'code': code,
                'grant_type': grant_type,
                'redirect_uri': redirect_uri,
            },
            timeout=timeout
        )

    def client_credentials(self, client_id, client_secret, audience,
                           grant_type='client_credentials',
                           timeout=5.0):
        """Client credentials grant

        This is the OAuth 2.0 grant that server processes utilize in
        order to access an API. Use this endpoint to directly request
        an access_token by using the Application Credentials (a Client Id and
        a Client Secret).

        Args:
            grant_type (str): Denotes the flow you're using. For client credentials
            use client_credentials

            client_id (str): your application's client Id

            client_secret (str): your application's client Secret

            audience (str): The unique identifier of the target API you want to access.

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'audience': audience,
                'grant_type': grant_type,
            },
            timeout=timeout
        )

    def login(self, client_id, client_secret, username, password, scope, realm,
              audience, grant_type='http://auth0.com/oauth/grant-type/password-realm',
              timeout=5.0):
        """Calls /oauth/token endpoint with password-realm grant type


        This is the OAuth 2.0 grant that highly trusted apps utilize in order
        to access an API. In this flow the end-user is asked to fill in credentials
        (username/password) typically using an interactive form in the user-agent
        (browser). This information is later on sent to the client and Auth0.
        It is therefore imperative that the client is absolutely trusted with
        this information.

        Args:
            grant_type (str): Denotes the flow you're using. For password realm
            use http://auth0.com/oauth/grant-type/password-realm

            client_id (str): your application's client Id

            client_secret (str): your application's client Secret

            audience (str): The unique identifier of the target API you want to access.

            username (str): Resource owner's identifier

            password (str): resource owner's Secret

            scope(str): String value of the different scopes the client is asking for.
            Multiple scopes are separated with whitespace.

            realm (str): String value of the realm the user belongs.
            Set this if you want to add realm support at this grant.

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token, id_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'username': username,
                'password': password,
                'realm': realm,
                'client_secret': client_secret,
                'scope': scope,
                'audience': audience,
                'grant_type': grant_type
            },
            timeout=timeout
        )

    def refresh_token(self, client_id, client_secret, refresh_token,
                      grant_type='refresh_token', scope='',
                      timeout=5.0):
        """Calls /oauth/token endpoint with refresh token grant type

        Use this endpoint to refresh an access token, using the refresh token you got during authorization.

        Args:
            grant_type (str): Denotes the flow you're using. For refresh token
            use refresh_token

            client_id (str): your application's client Id

            client_secret (str): your application's client Secret

            refresh_token (str): The refresh token returned from the initial token request.

            scope (str): String value of the different scopes the client is asking for.
            Multiple scopes are separated with whitespace.

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token, id_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token,
                'scope': scope,
                'grant_type': grant_type
            },
            timeout=timeout
        )

    def passwordless_login(self, client_id, client_secret, username,
                           otp, realm, scope, audience,
                           timeout=timeout):
        """Calls /oauth/token endpoint with http://auth0.com/oauth/grant-type/passwordless/otp grant type

        Once the verification code was received, login the user using this endpoint with their
        phone number/email and verification code.

        Args:
            client_id (str): your application's client Id

            client_secret (str): your application's client Secret. Only required for Regular Web Apps.

            username (str): The user's phone number or email address.

            otp (str): the user's verification code.

            realm (str): use 'sms' or 'email'.
            Should be the same as the one used to start the passwordless flow.

            scope(str): String value of the different scopes the client is asking for.
            Multiple scopes are separated with whitespace.

            audience (str): The unique identifier of the target API you want to access.

            timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        Returns:
            access_token, id_token
        """

        return self.post(
            '{}://{}/oauth/token'.format(self.protocol, self.domain),
            data={
                'client_id': client_id,
                'username': username,
                'otp': otp,
                'realm': realm,
                'client_secret': client_secret,
                'scope': scope,
                'audience': audience,
                'grant_type': 'http://auth0.com/oauth/grant-type/passwordless/otp'
            },
            timeout=timeout
        )
