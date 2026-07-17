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

    for column, count in profile["null_counts_per_column"].items():
        lines.append(f"| {column} | {count} |")

    lines.extend([
        "",
        "## Validation results",
        "",
        "| Check | Status |",
        "|---|---|",
    ])

    for validation in validations:
        status = "passed ✅" if validation["passed"] else "failed ❌"
        lines.append(f"| {validation['check_name']} | {status} |")

    return "\n".join(lines)
