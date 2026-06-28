import pandas as pd

from data_sentinel.validation import validate_required_columns

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