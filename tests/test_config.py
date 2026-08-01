import json

import pytest

from data_sentinel.config import load_json_config


def test_load_json_config_loads_config_file(tmp_path):
    config_path = tmp_path / "schema.json"

    config_data = {
        "dataset_name": "customers",
        "input_file": "data/sample/customers.csv",
        "required_columns": ["id", "name", "email"],
        "not_null_columns": ["id", "email"],
    }

    with config_path.open("w", encoding="utf-8") as file:
        json.dump(config_data, file)

    result = load_json_config(str(config_path))

    assert result == config_data


def test_load_json_config_raises_error_when_file_does_not_exist():
    with pytest.raises(FileNotFoundError):
        load_json_config("config/not_existing_schema.json")