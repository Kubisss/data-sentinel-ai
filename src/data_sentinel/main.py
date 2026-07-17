import os
import json

import pandas as pd

from data_sentinel.profiling import profile_dataframe
from data_sentinel.loaders import load_csv
from data_sentinel.validation import validate_required_columns, validate_not_null_columns
from data_sentinel.reporting import summarize_validation_results


def main():
    input_file = "data/sample/customers.csv"
    output_file = "reports/profile_report.json"

    df = load_csv(input_file)
    profile_report = profile_dataframe(df)

    validation_results = [
        validate_required_columns(df, ["id", "name", "age", "city", "email"]),
        validate_not_null_columns(df, ["id", "age", "name", "email"]),
    ]

    summary = summarize_validation_results(validation_results)

    final_report = {
        "input_file": input_file,
        "profile": profile_report,
        "validations": validation_results,
        "summary": summary,
    }

    os.makedirs("reports", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(final_report, file, indent=4, ensure_ascii=False)

    print(f"Report generated successfully at: {output_file}")

if __name__ == "__main__":
    main()