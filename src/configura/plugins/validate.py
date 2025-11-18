from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError

from configura.constants import TYPE_DATA, DEFAULT_ENCODING, TYPE_ON_FAIL
from configura.io import read_json, write_jsonl

class Validate:
    def __init__(
        self,
        schema_path: str,
        schema_encoding: str = DEFAULT_ENCODING,

        on_fail: TYPE_ON_FAIL = "skip",

        dlq_dir: str = "",
        dlq_name: str = DEFAULT_ENCODING,
    ) -> None:
        self.schema_path = schema_path
        self.schema_encoding = schema_encoding

        self.on_fail: TYPE_ON_FAIL= on_fail

        self.dlq_dir = dlq_dir
        self.dlq_name = dlq_name

    def process(self, data):
        return self.validate(
            data,
            self.schema_path,
            schema_encoding=self.schema_encoding,

            on_fail=self.on_fail,

            dlq_dir=self.dlq_dir,
            dlq_name=self.dlq_name
        )
    
    @staticmethod
    def validate(
        data: TYPE_DATA,
        schema_path: str,
        schema_encoding: str = DEFAULT_ENCODING,

        on_fail: TYPE_ON_FAIL = "skip",

        dlq_dir: str = "data/dlq/",
        dlq_name: str = "dlq_output",
    ) -> TYPE_DATA:
        
        schema = read_json(path=schema_path, encoding=schema_encoding)
        validator = Draft7Validator(schema)

        good, bad = [], []

        for item in data:
            errors : list[ValidationError] = list(validator.iter_errors(item))
            if errors:
                bad.append({
                    "record": item,
                    "errors": [error.message for error in errors]
                })
            else:
                good.append(item)

        if not bad:
            return good

        # Fail diagnosis
        if on_fail == "fail":
            raise ValueError(f"{len(bad)} records failed validation")
        elif on_fail == "skip":
            return good
        elif on_fail == "dlq":
            write_jsonl(data=bad, path=f"{dlq_dir}{dlq_name}.jsonl")
            return good
        else:
            raise ValueError(f"Unknown on_fail mode: {on_fail}")