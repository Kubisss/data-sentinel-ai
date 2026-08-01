from pathlib import Path

from jinja2 import Environment, FileSystemLoader

def render_markdown_report(report):
    summary = report["summary"]
    profile = report["profile"]
    validations = report["validations"]

    lines = [
        "# Data Quality Report",
        "",
        f"Input file: `{report['input_file']}`",
        "",
        "## Summary",
        "",
        f"- Overall status: **{summary['overall_status']}**",
        f"- Quality score: **{summary['quality_score']}%**",
        f"- Total checks: {summary['total_checks']}",
        f"- Passed checks: {summary['passed_checks']}",
        f"- Failed checks: {summary['failed_checks']}",
        "",
        "## Dataset profile",
        "",
        f"- Rows: {profile['num_rows']}",
        f"- Columns: {profile['num_columns']}",
        "",
        "## Null counts",
        "",
        "| Column | Null count |",
        "|---|---:|",
    ]

    lines.extend([
        "",
        "## Insights",
        "",
    ])

    for insight in report.get("insights", []):
        lines.append(f"- {insight}")

    lines.extend([
            "",
        ])

    for column, count in profile["null_counts_per_column"].items():
        lines.append(f"| {column} | {count} |")

    lines.extend([
    "",
    "## Null counts chart",
    "",
    "![Null counts](charts/null_counts.png)",
    ])

    lines.extend([
    "",
    "## Validation results",
    "",
    "| Check | Status | Details |",
    "|---|---|---|",
    ])

    for validation in validations:
        status = "passed ✅" if validation["passed"] else "failed ❌"
        details = ""

        if validation["check_name"] == "not_null_columns" and not validation["passed"]:
            columns_with_nulls = validation["columns_with_nulls"]

            details = ", ".join(
                f"{column} ({count} nulls)"
                for column, count in columns_with_nulls.items()
            )

        elif validation["check_name"] == "required_columns" and not validation["passed"]:
            missing_columns = validation["missing_columns"]

            details = "Missing columns: " + ", ".join(missing_columns)

        lines.append(
            f"| {validation['check_name']} | {status} | {details} |"
        )

    return "\n".join(lines)


def render_html_report(report):
    templates_dir = Path(__file__).parent / "templates"

    environment = Environment(
        loader=FileSystemLoader(templates_dir)
    )

    template = environment.get_template("report.html")

    return template.render(report=report)