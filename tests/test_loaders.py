import pytest
from data_sentinel.loaders import load_csv

def test_load_csv_raises_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        load_csv("non_existent_file.csv")


