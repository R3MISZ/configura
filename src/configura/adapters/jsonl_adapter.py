from .helper_adapter import read_jsonl, write_jsonl
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
    def __init__(self, path: str, encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.encoding = encoding

    def process(self, data: TYPE_DATA):
        write_jsonl(
            path=self.path,
            data=data,
            encoding=self.encoding,
        )
        return data