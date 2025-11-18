from configura.io import read_csv, write_csv, derive_related_path
from configura.constants import *

class ReadCsv:
    def __init__(self, path: str, delimiter: str = ",", encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding

    def process(self, data):
        # ignore data
        return read_csv(
            path=self.path,
            delimiter=self.delimiter,
            encoding=self.encoding,
        )

class WriteCsv:
    def __init__(
        self,
        path: str | None = None,
        delimiter: str = ",",
        encoding: str = DEFAULT_ENCODING,
        add_timestamp: bool = False,
        base_dir: str = "data/output",
        file_name: str = "clean",
    ) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding
        self.add_timestamp = add_timestamp
        self.base_dir = base_dir
        self.file_name = file_name

    def process(self, data: TYPE_DATA):
        resolved_path = derive_related_path(
            kind="output",
            explicit_path=self.path,
            add_timestamp=self.add_timestamp,
            base_dir=self.base_dir,
            file_name=self.file_name,
        )

        write_csv(
            path=resolved_path,
            data=data,
            delimiter=self.delimiter,
            encoding=self.encoding,
        )
        return data