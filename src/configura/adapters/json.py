import json
import os
from typing import Iterable, Dict, Any, List

import jsonschema
from jsonschema.exceptions import ValidationError

class JsonAdapter:
    def __init__(self,
                 encoding: str = "utf-8",
                 input_path: str = "",
                 output_path: str = "",
                 schema_file: str = "",
                 on_fail: str = "skip",
                 dlq_path: str = ""
                 ) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.schema_file = schema_file
        self.encoding = encoding
        self.on_fail = on_fail
        self.dlq_path = dlq_path

    def _read(self, path : str, encoding: str):
        if path.endswith(".jsonl"): return JsonAdapter._read_jsonl(path, encoding)
        elif path.endswith(".json"): return JsonAdapter._read_json(path, encoding)
        else:
            raise ValueError(f"Unsupported file format for path: {path}")

    @staticmethod
    def _read_jsonl(path : str, encoding: str) -> List[Dict[str, Any]]:
        rows = []
        with open(path, "r", encoding=encoding) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rows.append(json.loads(line))
        return rows
    
    @staticmethod
    def _read_json(path: str, encoding: str) -> dict[str, Any]:
        try:
            with open(path, "r", encoding=encoding) as f:
                return json.load(f)
        except Exception:
            print(f"Json-File not found or invalid: {path}")
        return {}
        
    @staticmethod
    def _write_jsonl(path : str, encoding : str, records):

        text = "\n".join(json.dumps(record, ensure_ascii=False) for record in records)

        with open(path, "w", encoding=encoding) as f:
            f.write(text)

        print(f"Jsonl-File written: {path}")

        return True
    
    @staticmethod
    def _validate(schema_path: str, encoding: str, dlq_path: str, on_fail: str, records):
        # records sicherheitshalber materialisieren
        if not isinstance(records, list):
            records = list(records)

        schema = JsonAdapter._read_json(schema_path, encoding)
        validator = jsonschema.Draft7Validator(schema)

        good, bad = [], []

        for rec in records:
            errors : list[ValidationError] = list(validator.iter_errors(rec))
            if errors:
                bad.append({
                    "record": rec,
                    "errors": [error.message for error in errors]
                })
            else:
                good.append(rec)

        if bad:
            if on_fail == "fail":
                example = "; ".join(bad[0]["errors"])
                raise ValueError(f"Validation failed for {len(bad)} records. Example: {example}")
            elif on_fail == "dlq":
                if dlq_path:
                    os.makedirs(os.path.dirname(dlq_path) or ".", exist_ok=True)
                    JsonAdapter._write_jsonl(dlq_path, encoding, bad)
            # on_fail == "skip": einfach nur good zurückgeben

        return good

    def process(self, data) -> Any:
        if self.input_path:
            return self._read(self.input_path, self.encoding)
        
        if self.schema_file:
            return self._validate(self.schema_file, self.encoding, self.dlq_path, self.on_fail, data)

        if self.output_path:
            return self._write_jsonl(self.output_path, self.encoding, data)