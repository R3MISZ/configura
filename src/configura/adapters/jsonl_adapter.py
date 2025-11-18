from configura.io import read_jsonl, write_jsonl, derive_related_path
from configura.constants import *

class ReadJsonl:
    def __init__(self, path: str, encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.encoding = encoding

    def process(self, data):
        # ignore data
        return read_jsonl(
            path=self.path,
            encoding=self.encoding,
        )

class WriteJsonl:
    def __init__(
        self,
        path: str | None = None,
        encoding: str = DEFAULT_ENCODING,
        add_timestamp: bool = False,
        base_dir: str = "data/output",
        file_name: str = "clean",
    ) -> None:
        self.path = path
        self.encoding = encoding
        self.add_timestamp = add_timestamp
        self.base_dir = base_dir
        self.file_name = file_name

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        resolved_path = derive_related_path(
            kind="output",
            explicit_path=self.path,
            add_timestamp=self.add_timestamp,
            base_dir=self.base_dir,
            file_name=self.file_name,
        )

        write_jsonl(
            path=resolved_path,
            data=data,
            encoding=self.encoding,
        )
        return data