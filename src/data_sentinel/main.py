import os
import json

import pandas as pd

from data_sentinel.profiling import profile_dataframe
from data_sentinel.loaders import load_csv
from data_sentinel.validation import validate_required_columns, validate_not_null_columns
from data_sentinel.reporting import summarize_validation_results
from data_sentinel.renderers import render_markdown_report
from data_sentinel.charts import generate_null_counts_chart
from data_sentinel.renderers import render_markdown_report, render_html_report
from data_sentinel.config import load_json_config
from data_sentinel.insights import generate_insights
from data_sentinel.agents import generate_summary_with_fallback
from data_sentinel.pdf import render_pdf_report


def main():
    schema = load_json_config("config/customers_large_schema.json")

    input_file = schema["input_file"]
    output_file = "reports/profile_report.json"

    print("Loading data...")
    df = load_csv(input_file)

    print("Profiling data...")
    profile_report = profile_dataframe(df)

    print("Running validations...")
    validation_results = [
        validate_required_columns(df, schema["required_columns"]),
        validate_not_null_columns(df, schema["not_null_columns"]),
    ]

    print("Generating summary...")
    summary = summarize_validation_results(validation_results)

    final_report = {
        "dataset_name": schema["dataset_name"],
        "input_file": input_file,
        "profile": profile_report,
        "validations": validation_results,
        "summary": summary,
    }

    print("Generating insights...")
    final_report["insights"] = generate_insights(final_report)

    print("Generating AI summary...")
    final_report["ai_summary"] = generate_summary_with_fallback(final_report)

    print("Generating null counts chart...")
    generate_null_counts_chart(profile_report["null_counts_per_column"],"reports/charts/null_counts.png")

    print("Rendering reports...")
    os.makedirs("reports", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(final_report, file, indent=4, ensure_ascii=False)

    markdown_report = render_markdown_report(final_report)
    html_report = render_html_report(final_report)

    with open("reports/profile_report.md", "w", encoding="utf-8") as file:
        file.write(markdown_report)

    with open("reports/profile_report.html", "w", encoding="utf-8") as file:
        file.write(html_report)

    print("PDF report generated at: reports/profile_report.pdf")
    render_pdf_report(
    html_path="reports/profile_report.html",
    output_path="reports/profile_report.pdf",
    )

    print(f"JSON report generated at: {output_file}")
    print(f"Markdown report generated at: reports/profile_report.md")
    print(f"HTML report generated at: reports/profile_report.html")

if __name__ == "__main__":
    main()