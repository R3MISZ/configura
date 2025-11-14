from typing import Any, Dict, Literal, TypeAlias, List

DEFAULT_ENCODING = "utf-8"

TYPE_RECORD: TypeAlias = Dict[str, Any]
TYPE_DATA = List[TYPE_RECORD] | None


TYPE_ON_FAIL = Literal["skip", "fail", "dlq"]
TYPE_DLQ_FORMAT = Literal["json", "jsonl", "csv"]