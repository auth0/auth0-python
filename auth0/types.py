from typing import Any, Dict, List, Tuple, TypedDict, Union

TimeoutType = Union[float, Tuple[float, float]]

RequestData = Union[Dict[str, Any], List[Any], TypedDict]
