
from configura.engine import run_pipeline
from configura.io import read_yaml

if __name__ == "__main__":
    yaml_path = "./data/configs/pipeline.yaml"

    yaml_cfg = read_yaml(yaml_path)

    run_pipeline(yaml_cfg)
    print("Pipeline done")