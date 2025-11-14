from configura.constants import *
from configura.engine import runtime

class SetRuntime:
    def __init__(
            self,
            mode: TYPE_RUNTIME_MODE = DEFAULT_RUNTIME_MODE,
            chunk_size: TYPE_CHUNK_SIZE = DEFAULT_RUNTIME_CHUNK_SIZE
    ) -> None:
        self.mode = mode
        self.chunk_size = chunk_size

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        runtime.mode = self.mode
        runtime.chunk_size = self.chunk_size
        return data
