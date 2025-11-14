
from configura.adapters.helper_adapter import validate
from configura.constants import *

class Validate:
    def __init__(
        self,
        schema_path: str,
        schema_encoding: str = DEFAULT_ENCODING,
        on_fail: TYPE_ON_FAIL = "skip",
        dlq_path: str = "",
        dlq_format: TYPE_DLQ_FORMAT = "json",
        dlq_encoding: str = DEFAULT_ENCODING
    ) -> None:
        self.schema_path = schema_path
        self.schema_encoding = schema_encoding
        self.on_fail: TYPE_ON_FAIL= on_fail
        self.dlq_path = dlq_path
        self.dlq_format: TYPE_DLQ_FORMAT = dlq_format
        self.dlq_encoding = dlq_encoding
    
    def process(self, data):
        return validate(
            data,
            self.schema_path,
            schema_encoding=self.schema_encoding,
            on_fail=self.on_fail,
            dlq_path=self.dlq_path,
            dlq_format=self.dlq_format,
            dlq_encoding=self.dlq_encoding
        )