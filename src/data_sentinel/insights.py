def generate_insights(report: dict) -> list[str]:
    profile = report["profile"]
    summary = report["summary"]
    validations = report["validations"]

    insights = []

    insights.append(
        f"Dataset contains {profile['num_rows']} rows and {profile['num_columns']} columns."
    )

    insights.append(
        f"Overall quality score is {summary['quality_score']}%."
    )

    if summary["overall_status"] == "passed":
        insights.append("All validation checks passed.")
    else:
        insights.append(
            f"{summary['failed_checks']} validation check(s) failed."
        )

    for validation in validations:
        if validation["passed"]:
            continue

        check_name = validation["check_name"]

        insights.append(f"Check '{check_name}' failed.")

        if check_name == "not_null_columns":
            columns_with_nulls = validation.get("columns_with_nulls", {})

            for column, count in columns_with_nulls.items():
                insights.append(
                    f"Column '{column}' contains {count} null value(s)."
                )

        if check_name == "required_columns":
            missing_columns = validation.get("missing_columns", [])

            if missing_columns:
                insights.append(
                    "Missing required columns: " + ", ".join(missing_columns) + "."
                )

    return insights