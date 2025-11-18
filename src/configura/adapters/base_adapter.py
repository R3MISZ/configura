from configura.constants import DEFAULT_ENCODING

class ReadBase:
    def __init__(
        self,
        path: str,
        encoding: str = DEFAULT_ENCODING,
    ) -> None:
        self.path = path
        self.encoding = encoding

class WriteBase:
    def __init__(
        self,
        path: str = "",
        encoding: str = DEFAULT_ENCODING,
    ) -> None:
        self.path = path
        self.encoding = encoding
