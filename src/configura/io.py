import csv
import json
import yaml

from typing import Any
from pathlib import Path

from configura.constants import *

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
    encoding: str = DEFAULT_ENCODING,
    delimiter: str = ","
) -> TYPE_DATA:
    data = []
    with open(path, mode="r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            data.append(dict(row))
    return data

def write_csv(
    data: TYPE_DATA,
    path: str,
    encoding: str = DEFAULT_ENCODING,
    delimiter: str = ","
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

def write_json(data, path: str, encoding: str = DEFAULT_ENCODING):
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
#endregion

#region JSONL
def read_jsonl(path: str, encoding: str = DEFAULT_ENCODING):
    with open(path, encoding=encoding) as f:
        return [json.loads(line) for line in f if line.strip()]

def write_jsonl(data, path: str, encoding: str = DEFAULT_ENCODING):
    with open(path, "w", encoding=encoding) as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
#endregion