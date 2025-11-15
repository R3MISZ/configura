from typing import Any, Literal, TypeAlias

# ----------------------
# Types
# ----------------------

TYPE_PIPELINE_STEP = dict[str, Any]

TYPE_RECORD: TypeAlias = dict[str, Any]
TYPE_DATA: TypeAlias = list[TYPE_RECORD]

TYPE_ON_FAIL = Literal["skip", "fail", "dlq"]
TYPE_DLQ_FORMAT = Literal["json", "jsonl", "csv"]

TYPE_RUNTIME_MODE = Literal["stream", "batch"]
TYPE_CHUNK_SIZE = int

# ----------------------
# Default Values
# ----------------------

DEFAULT_ENCODING = "utf-8"

DEFAULT_ON_FAIL = "skip"
DEFAULT_DLQ_FORMAT = "json"

DEFAULT_RUNTIME_MODE = "stream"
DEFAULT_RUNTIME_CHUNK_SIZE = 1000