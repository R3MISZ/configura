import argparse
from pathlib import Path
from typing import Optional

from configura.engine import run_pipeline_from_config

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="configura",
        description="Run Configura using a config file (YAML/JSON)",
    )
    parser.add_argument(
        "-c",
        "--config",
        required=True,
        metavar="FILE",
        help="filepath to config",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose logging",
    )

    args = parser.parse_args(argv)

    config_path = Path(args.config)

    run_pipeline_from_config(config_path=config_path, verbose=args.verbose)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())