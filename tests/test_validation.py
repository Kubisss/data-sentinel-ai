import pandas as pd

from data_sentinel.validation import validate_required_columns, validate_not_null_columns

def test_validate_required_columns():
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)

    required_columns = ["name", "age", "city"]

    result = validate_required_columns(df, required_columns)

    assert result["passed"] is True
    assert result["missing_columns"] == []

def test_validate_required_columns_missing():
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    }
    df = pd.DataFrame(data)

    required_columns = ["name", "age", "city"]

    result = validate_required_columns(df, required_columns)

    assert result["passed"] is False
    assert result["missing_columns"] == ["city"]

    def test_validate_not_null_columns():
        data = {
            "name": ["Alice", "Bob", None],
            "age": [25, 30, 35],
            "city": ["New York", "Los Angeles", "Chicago"]
        }
        df = pd.DataFrame(data)

        columns_to_check = ["name", "age"]

        result = validate_not_null_columns(df, columns_to_check)

        assert result["passed"] is False
        assert result["null_columns"] == ["name"]

    def test_validate_not_null_columns_no_nulls():
        data = {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "city": ["New York", "Los Angeles", "Chicago"]
        }
        df = pd.DataFrame(data)

        columns_to_check = ["name", "age"]

        result = validate_not_null_columns(df, columns_to_check)

        assert result["passed"] is True
        assert result["null_columns"] == []