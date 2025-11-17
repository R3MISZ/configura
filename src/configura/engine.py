from dataclasses import dataclass, field

from datetime import datetime

from typing import Any
from configura.loader import process_class
from configura.constants import *

def make_run_id() -> str:
    # e.g. "2025-11-15T14-33-12"
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

@dataclass
class EngineRuntime:
    mode: TYPE_RUNTIME_MODE = DEFAULT_RUNTIME_MODE
    chunk_size: TYPE_CHUNK_SIZE = DEFAULT_RUNTIME_CHUNK_SIZE

    # New: information about the current input
    input_path: str | None = None
    input_basename: str | None = None  # e.g. "records"
    input_extension: str | None = None # e.g. ".jsonl"

    # Optional: unique run id for this pipeline execution
    run_id: str = field(default_factory=make_run_id)

runtime: EngineRuntime = EngineRuntime()

def run_pipeline(yaml_cfg: TYPE_PIPELINE_STEP):
    
    steps: list = yaml_cfg.get("pipeline", {}).get("steps", [])
    data = []

    for step in steps:
        print(f"step: {step}")
        data = process_class(step, data)
        print(f"data: {data}")
        print("-")