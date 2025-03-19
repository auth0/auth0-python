from typing import Any


class UsersByEmail:
    def search_users_by_email_async(self: Any, email: str, fields: list[str] | None = None, include_fields: bool = True) -> list[dict[str, Any]]: ...
