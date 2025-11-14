from .helper_adapter import read_json, write_json
from configura.constants import *

class ReadJson:
    def __init__(self, path: str, encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.encoding = encoding

    def process(self, data):
        # ignore data
        return read_json(
            path=self.path,
            encoding=self.encoding,
        )

class WriteJson:
    def __init__(self, path: str, encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.encoding = encoding

    def process(self, data: TYPE_DATA):
        write_json(
            path=self.path,
            data=data,
            encoding=self.encoding,
        )
        return data
