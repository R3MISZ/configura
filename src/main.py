import yaml
from configura.engine import run_pipeline

if __name__ == "__main__":
    from pathlib import Path
    config_yaml_path = Path("./data/configs/pipeline.yaml")

    if not config_yaml_path.exists():
        raise FileNotFoundError(f"YAML config not found: {config_yaml_path}")
    
    with config_yaml_path.open("r", encoding="utf-8") as f:
        yaml_cfg = yaml.load(f, Loader=yaml.FullLoader)

    run_pipeline(yaml_cfg)
    print("Pipeline done")