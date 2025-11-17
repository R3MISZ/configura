from configura.io import read_json, write_json, set_runtime_input, derive_related_path
from configura.constants import *

class ReadJson:
    def __init__(self, path: str, encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.encoding = encoding

    def process(self, data):
        # ignore data
        set_runtime_input(self.path)

        return read_json(
            path=self.path,
            encoding=self.encoding,
        )

class WriteJson:
    def __init__(
        self,
        path: str | None = None,
        encoding: str = DEFAULT_ENCODING,
        use_input_name: bool = True,
        add_timestamp: bool = False,
        base_dir: str = "data/output",
        suffix: str = "_clean",
    ) -> None:
        self.path = path
        self.encoding = encoding
        self.use_input_name = use_input_name
        self.add_timestamp = add_timestamp
        self.base_dir = base_dir
        self.suffix = suffix

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        resolved_path = derive_related_path(
            kind="output",
            base_dir=self.base_dir,
            explicit_path=self.path,
            use_input_name=self.use_input_name,
            add_timestamp=self.add_timestamp,
            suffix=self.suffix,
        )

        write_json(
            path=resolved_path,
            data=data,
            encoding=self.encoding,
        )
        return data
