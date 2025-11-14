from .helper_adapter import read_csv, write_csv
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
    def __init__(self, path: str, delimiter: str = ",", encoding: str = DEFAULT_ENCODING) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding

    def process(self, data: TYPE_DATA):
        write_csv(
            path=self.path,
            data=data,
            delimiter=self.delimiter,
            encoding=self.encoding,
        )
        return data