from pathlib import Path
from typing import Union

from configura.io import load_config
from configura.loader import process_class
from configura.constants import *

def run_pipeline_from_config(config_path: Union[str, Path], verbose: bool = False) -> None:
    # Convert to str if type(Path)
    config_path_str = str(config_path)

    config = load_config(config_path_str)

    if not isinstance(config, dict):
        raise ValueError(f"Config root must be an object/dict, got: {type(config)}")

    if verbose: print("[DEBUG] Loaded config:", config)

    pipeline: list[dict] = config.get("pipeline", [])
    if not isinstance(pipeline, list):
        raise ValueError("Config key 'pipeline' must be a list.")

    if verbose: print(f"[DEBUG] Executing {len(pipeline)} pipeline steps...")

    data = []
    for step in pipeline:
        print(f"[DEBUG] step: {step}")
        data = process_class(step, data)
        #print(f"data: {data}")
        #print("-")

    if verbose: print("[DONE] Pipeline finished")

# for debug & development
if __name__ == "__main__":
    #default_config = "./data/configs/pipeline.yaml"
    #run_pipeline_from_config(default_config, verbose=True)
    pass