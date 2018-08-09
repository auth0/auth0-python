class Auth0Error(Exception):
    def __init__(self, status_code, error_code, message):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return '%s: %s' % (self.status_code, self.message)

class TokenVerificationError(Auth0Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'Failed to verify the token: %s' % (self.message)

class JwkProviderError(Auth0Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'Failed to obtain the public key: %s' % (self.message)