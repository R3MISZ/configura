from typing import Any, Dict, Literal

DEFAULT_ENCODING = "utf-8"

TYPE_ON_FAIL = Literal["skip", "fail", "dlq"]
TYPE_DLQ_FORMAT = Literal["json", "jsonl", "csv"]

TYPE_DATA = list[Dict[str, Any]]