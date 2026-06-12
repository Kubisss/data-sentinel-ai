import pandas as pd
import pytest

from data_sentinel.profiling import profile_dataframe

@pytest.fixture
def df():
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, None],
        "city": ["New York", "Los Angeles", "Chicago", "Houston"]
    })

def test_profile_dataframe_returns_correct_row_count(df):
    result = profile_dataframe(df)
    assert result["num_rows"] == 4

def test_profile_dataframe_returns_correct_column_count(df):
    result = profile_dataframe(df)
    assert result["num_columns"] == 3

def test_profile_dataframe_returns_correct_column_names(df):
    result = profile_dataframe(df)
    assert result["column_names"] == ["name", "age", "city"]

def test_profile_dataframe_returns_correct_null_counts(df):
    result = profile_dataframe(df)
    assert result["null_counts_per_column"] == {"name": 0, "age": 1, "city": 0}

def test_profile_dataframe_returns_correct_duplicate_rows(df):
    result = profile_dataframe(df)
    assert result["duplicate_rows"] == 0

def test_profile_dataframe_returns_data_types_as_strings(df):
    result = profile_dataframe(df)

    assert all(isinstance(value, str) for value in result["data_types"].values())

def test_profile_dataframe_detects_duplicate_rows():
    df = pd.DataFrame({
        "name": ["Alice", "Alice", "Bob"],
        "age": [25, 25, 30],
        "city": ["New York", "New York", "Chicago"]
    })

    result = profile_dataframe(df)

    assert result["duplicate_rows"] == 1