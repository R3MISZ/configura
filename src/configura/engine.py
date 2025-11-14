from typing import Any
from configura.loader import process_class
from configura.constants import *

class EngineRuntime:
    def __init__(
            self,
            mode: TYPE_RUNTIME_MODE = DEFAULT_RUNTIME_MODE,
            chunk_size: TYPE_CHUNK_SIZE = DEFAULT_RUNTIME_CHUNK_SIZE
    ) -> None:
        self.mode = mode
        self.chunk_size = chunk_size

runtime: EngineRuntime = EngineRuntime()

def run_pipeline(yaml_cfg: TYPE_PIPELINE_STEP):
    #TODO
    #import datetime
    #today = datetime.date.today().isoformat()
    #vars = {
    #    "id": yaml_cfg.get("id", "default"),
    #    "date": today,
    #}

    #start_runtime(yaml_cfg.get("runtime", {}))

    list_steps = [
        yaml_cfg.get("runtime", []),
        yaml_cfg.get("input", []),
        yaml_cfg.get("validation", []),
    ]

    list_steps.extend(item for item in yaml_cfg.get("pipeline", {}).get("steps", []))
    list_steps.append(yaml_cfg.get("output", []))

    data = []

    for step in list_steps:
        print(f"step: {step}")
        data = process_class(step, data)
        print(f"data: {data}")
        print("-")