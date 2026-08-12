from data_sentinel.llm import generate_llm_summary, is_llm_enabled

def generate_ai_summary(report: dict) -> dict:
    summary = report["summary"]
    insights = report.get("insights", [])

    if summary["overall_status"] == "passed":
        summary_text = (
            "The dataset passed all configured validation checks. "
            "No critical data quality issues were detected."
        )

        recommendations = [
            "Continue monitoring data quality over time.",
            "Consider adding more validation rules as the dataset grows.",
        ]
    else:
        failed_check_names = summary.get("failed_check_names", [])

        summary_text = (
            f"The dataset failed {summary['failed_checks']} validation check(s). "
            f"Failed checks: {', '.join(failed_check_names)}. "
            "These issues should be reviewed before using the dataset in production analytics."
        )

        recommendations = [
            "Review failed validation checks.",
            "Investigate affected columns in the source data.",
            "Consider adding stricter checks to the ingestion pipeline.",
        ]

    return {
        "title": "Dataset quality summary",
        "summary": summary_text,
        "recommendations": recommendations,
        "source_insights": insights,
    }



def generate_summary_with_fallback(report: dict) -> dict:
    if not is_llm_enabled():
        fallback_summary = generate_ai_summary(report)
        fallback_summary["provider"] = "rule_based"
        return fallback_summary

    try:
        return generate_llm_summary(report)
    except Exception as error:
        fallback_summary = generate_ai_summary(report)
        fallback_summary["provider"] = "rule_based"
        fallback_summary["fallback_reason"] = str(error)
        return fallback_summary