from configura.io import read_csv, write_csv, set_runtime_input, derive_related_path
from configura.constants import *

class ReadCsv:
    def __init__(self, path: str, delimiter: str = ",", encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding

    def process(self, data):
        # ignore data
        set_runtime_input(self.path)

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
        use_input_name: bool = True,
        add_timestamp: bool = False,
        base_dir: str = "data/output",
        suffix: str = "_clean",
    ) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding
        self.use_input_name = use_input_name
        self.add_timestamp = add_timestamp
        self.base_dir = base_dir
        self.suffix = suffix

    def process(self, data: TYPE_DATA):
        resolved_path = derive_related_path(
            kind="output",
            base_dir="data/output",
            explicit_path=self.path or None,
            use_input_name=True,
            add_timestamp=True,
            suffix="_output",
        )

        write_csv(
            path=resolved_path,
            data=data,
            delimiter=self.delimiter,
            encoding=self.encoding,
        )
        return data