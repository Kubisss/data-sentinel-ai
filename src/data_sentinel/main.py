import os
import json

import pandas as pd

from profiling import profile_dataframe
from loaders import load_csv


def main():
    input_file = "data/sample/customers.csv"
    output_file = "reports/profile_report.json"

    df = load_csv(input_file)
    report = profile_dataframe(df)

    os.makedirs("reports", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"Report generated successfully at: {output_file}")

if __name__ == "__main__":
    main()