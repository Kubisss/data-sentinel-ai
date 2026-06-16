import pandas as pd

from pathlib import Path

def load_csv(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        raise