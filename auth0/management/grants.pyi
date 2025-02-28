from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Grants:
    def all_async(self, page: int | None = None, per_page: int | None = None, include_totals: bool = False, extra_params: dict[str, Any] | None = None): ...
    def delete_async(self, id: str) -> Any: ...
