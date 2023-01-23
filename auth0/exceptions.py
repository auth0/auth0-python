class Auth0Error(Exception):
    def __init__(self, status_code, error_code, message, content=None):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        self.content = content

    def __str__(self):
        return f"{self.status_code}: {self.message}"


class RateLimitError(Auth0Error):
    def __init__(self, error_code, message, reset_at):
        super().__init__(status_code=429, error_code=error_code, message=message)
        self.reset_at = reset_at


class TokenValidationError(Exception):
    pass
