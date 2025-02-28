from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Stats:
    def active_users(self) -> int: ...
    def daily_stats_async(self, from_date: str | None = None, to_date: str | None = None) -> list[dict[str, Any]]: ...
