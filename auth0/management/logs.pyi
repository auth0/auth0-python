from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Logs:
    def search_async(self, page: int = 0, per_page: int = 50, sort: str | None = None, q: str | None = None, include_totals: bool = True, fields: list[str] | None = None, from_param: str | None = None, take: int | None = None, include_fields: bool = True): ...
    def get_async(self, id: str) -> dict[str, Any]: ...
