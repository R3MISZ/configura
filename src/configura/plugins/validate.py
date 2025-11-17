from configura.io import validate
from configura.constants import *

class Validate:
    def __init__(
        self,
        schema_path: str,
        *,
        schema_encoding: str = DEFAULT_ENCODING,
        on_fail: TYPE_ON_FAIL = "skip",

        #DLQ ITEMS
        path: str | None = None,
        format: TYPE_DLQ_FORMAT = "json",
        encoding: str = DEFAULT_ENCODING,

        use_input_name: bool = True,
        add_timestamp: bool = False,

        base_dir: str = "data/dlq",
        suffix: str = "_dlq",

    ) -> None:
        self.schema_path = schema_path
        self.schema_encoding = schema_encoding
        self.on_fail: TYPE_ON_FAIL= on_fail

        self.dlq_path = path
        self.dlq_format: TYPE_DLQ_FORMAT = format
        self.dlq_encoding = encoding

        self.dlq_use_input_name = use_input_name
        self.dlq_add_timestamp = add_timestamp

        self.dlq_base_dir = base_dir
        self.dlq_suffix = suffix

    def process(self, data):
        return validate(
            data,
            self.schema_path,
            schema_encoding=self.schema_encoding,
            on_fail=self.on_fail,

            dlq_path=self.dlq_path,
            dlq_format=self.dlq_format,
            dlq_encoding=self.dlq_encoding,

            dlq_use_input_name=self.dlq_use_input_name,
            dlq_add_timestamp=self.dlq_add_timestamp,
            dlq_suffix=self.dlq_suffix
        )