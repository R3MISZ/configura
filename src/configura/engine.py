from typing import Dict, Any
from configura.dynlib import DynamicLib

RUNTIME_MODE = "default"
RUNTIME_CHUNK_SIZE = 0
    
def set_runtime(mode=RUNTIME_MODE, chunk_size=RUNTIME_CHUNK_SIZE):
    global RUNTIME_MODE, RUNTIME_CHUNK_SIZE
    RUNTIME_MODE = mode
    RUNTIME_CHUNK_SIZE = chunk_size

def run_pipeline(yaml_cfg: Dict[str, Any]):
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
        yaml_cfg.get("pipeline", {}).get("steps", []),
        yaml_cfg.get("output", [])
    ]

    data = None

    for step in list_steps:
        print(f"step: {step}")
        data = DynamicLib.run_step(step, data)
        print(f"data: {data}")
        print("-")
