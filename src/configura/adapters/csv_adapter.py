from configura.adapters.base_adapter import ReadBase, WriteBase
from configura.io import read_csv, write_csv

from configura.constants import DEFAULT_ENCODING

DELIMITER = ","

class ReadCsv(ReadBase):
    def __init__(
        self,
        path: str,
        encoding: str = DEFAULT_ENCODING,
        delimiter: str = DELIMITER
    ) -> None:
        super().__init__(path, encoding)
        self.delimiter = delimiter

    def process(self, data):
        return read_csv(
            path=self.path,
            encoding=self.encoding,
            delimiter=self.delimiter
        )

class WriteCsv(WriteBase):
    def __init__(
        self,
        path: str,
        encoding: str = DEFAULT_ENCODING,
        delimiter: str = DELIMITER
    ) -> None:
        super().__init__(path, encoding)
        self.delimiter = delimiter

    def process(self, data):
        write_csv(
            data=data,
            path=self.path,
            encoding=self.encoding,
            delimiter=self.delimiter
        )
        return data