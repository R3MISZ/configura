from configura.io import read_yaml, read_json
from configura.loader import process_class
from configura.constants import *
from pathlib import Path

def run_pipeline_from_config(config_path: Path, verbose: bool = False) -> None:
    # Convert to str if type(Path)

    if not config_path.exists():
        raise SystemExit(f"Config file not found: {config_path}")

    if not config_path.is_file():
        raise SystemExit(f"Config path is not a file: {config_path}")

    if config_path.suffix in (".yaml" or ".yml"):
        config = read_yaml(str(config_path))
    elif config_path.suffix == ".json":
        config = read_json(str(config_path))
    else:
        raise SystemExit(
            f"Unsupported config format '{config_path.suffix}'. "
            f"Allowed: .yaml, .yml, .json"
        )

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