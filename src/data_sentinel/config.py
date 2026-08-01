import json
from pathlib import Path


def load_json_config(config_path: str) -> dict:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file does not exist: {config_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)