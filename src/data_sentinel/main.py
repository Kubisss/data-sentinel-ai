import os
import json

import pandas as pd

from profiling import profile_dataframe


def main():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age": [25, 30, 35, 40, None],
        "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    })

    report = profile_dataframe(df)

    os.makedirs("reports", exist_ok=True)
    with open("reports/profile_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(report)

if __name__ == "__main__":
    main()