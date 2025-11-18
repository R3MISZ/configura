from configura.adapters.base_adapter import ReadBase, WriteBase
from configura.io import read_jsonl, write_jsonl

class ReadJsonl(ReadBase):
    def process(self, data):
        return read_jsonl(
            path=self.path,
            encoding=self.encoding
        )

class WriteJsonl(WriteBase):
    def process(self, data):
        return write_jsonl(
            data=data,
            path=self.path,
            encoding=self.encoding,
        )