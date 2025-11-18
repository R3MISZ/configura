from configura.adapters.base_adapter import ReadBase, WriteBase
from configura.io import read_json, write_json

class ReadJson(ReadBase):
    def process(self, data):
        return read_json(
            path=self.path,
            encoding=self.encoding
        )

class WriteJson(WriteBase):
    def process(self, data):
        return write_json(
            data=data,
            path=self.path,
            encoding=self.encoding,
        )