import os
import csv
import json
import yaml

from pathlib import Path

from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError

from configura.constants import *
from configura.engine import runtime

from typing import Optional, Any

from datetime import datetime

#region YAML
def read_yaml(
    path: str,
    encoding: str = DEFAULT_ENCODING
) -> Any:
    if not Path(path).exists():
        raise FileNotFoundError(f"YAML config not found: {path}")
    
    with open(path, mode="r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)
#endregion

#region CSV
def read_csv(
    path: str,
    delimiter: str = ",",
    encoding: str = DEFAULT_ENCODING
) -> TYPE_DATA:
    data = []
    with open(path, mode="r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            data.append(dict(row))
    return data

def write_csv(
    path: str,
    data: TYPE_DATA,
    delimiter: str = ",",
    encoding: str = DEFAULT_ENCODING
) -> None:
    if not data:
        # Empty list -> empty file with no header
        open(path, "w", encoding=encoding).close()
        return
    
    # Reference header from first row
    headers = list(data[0].keys())

    with open(path, mode="w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
#endregion

#region JSON
def read_json(path: str, encoding: str = DEFAULT_ENCODING):
    with open(path, encoding=encoding) as f:
        return json.load(f)

def write_json(path: str, data, encoding: str = DEFAULT_ENCODING):
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
#endregion

#region JSONL
def read_jsonl(path: str, encoding: str = DEFAULT_ENCODING):
    with open(path, encoding=encoding) as f:
        return [json.loads(line) for line in f if line.strip()]

def write_jsonl(path: str, data: TYPE_DATA, encoding: str = DEFAULT_ENCODING):
    with open(path, "w", encoding=encoding) as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
#endregion

# JSON & JSONL & CSV
def validate(
    data: TYPE_DATA,
    schema_path: str,
    schema_encoding: str = DEFAULT_ENCODING,

    on_fail: TYPE_ON_FAIL = "skip",
    dlq_path: str | None = None,
    dlq_format: TYPE_DLQ_FORMAT = "json",
    dlq_encoding: str = DEFAULT_ENCODING,

    dlq_use_input_name: bool = True,
    dlq_add_timestamp: bool = False,

    dlq_base_dir: str = "data/dlq",
    dlq_suffix: str = "_dlq",
) -> TYPE_DATA:
    schema = read_json(schema_path, encoding=schema_encoding)
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
        resolved_path = derive_related_path(
            kind="dlq",
            base_dir=dlq_base_dir,
            explicit_path=dlq_path,
            use_input_name=dlq_use_input_name,
            add_timestamp=dlq_add_timestamp,
            suffix=dlq_suffix
        )

        _write_dlq(bad, resolved_path, dlq_format, dlq_encoding)
        return good
    else:
        raise ValueError(f"Unknown on_fail mode: {on_fail}")

def _write_dlq(
    bad: TYPE_DATA,
    dlq_path: str,
    dlq_format: Literal["json", "jsonl", "csv"],
    dlq_encoding: str,
) -> None:
    
    dirpath = os.path.dirname(dlq_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    if dlq_format == "json":
        write_json(dlq_path, bad, encoding=dlq_encoding)
    elif dlq_format == "jsonl":
        write_jsonl(dlq_path, bad, encoding=dlq_encoding)
    elif dlq_format == "csv":
        write_csv(dlq_path, bad, encoding=dlq_encoding)
    else:
        raise ValueError(f"Unsupported dlq_format: {dlq_format}")
    
def set_runtime_input(str_path: str):
    path = Path(str_path)
    runtime.input_path = str(path)
    runtime.input_basename = path.stem    # "records"
    runtime.input_extension = path.suffix # ".jsonl"
    print(
        "RUNTIME - INPUT",
        str(path),
        str(path.stem),
        str(path.suffix)
    )

def derive_related_path(
    kind: Literal["output", "dlq"],
    base_dir: str,
    *,
    explicit_path: Optional[str] = None,
    use_input_name: bool = True,
    add_timestamp: bool = True,
    suffix: str = "",
) -> str:
    """
    Build a derived path for output or DLQ based on:
      - explicit_path (if provided, that always wins)
      - runtime.input_* (if available)
      - base_dir + optional timestamp + suffix
    """
    # 1. If user provided an explicit path, use it as-is
    if explicit_path:
        return explicit_path

    # 2. If we have no input info → fallback to generic name
    if not use_input_name or runtime.input_basename is None:
        # last-resort fallback name
        name = f"{kind}"
    else:
        name = runtime.input_basename

    if suffix:
        name = f"{name}{suffix}"

    if add_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"{name}_{timestamp}"

    # If we have an input extension, reuse it
    ext = runtime.input_extension or ""

    p = Path(base_dir) / f"{name}{ext}"
    return str(p)