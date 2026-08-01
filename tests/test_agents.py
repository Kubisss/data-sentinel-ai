from data_sentinel.agents import generate_ai_summary


def test_generate_ai_summary_returns_positive_summary_when_report_passed():
    report = {
        "summary": {
            "overall_status": "passed",
            "failed_checks": 0,
            "failed_check_names": [],
        },
        "insights": [
            "Dataset contains 5 rows and 5 columns.",
            "All validation checks passed.",
        ],
    }

    result = generate_ai_summary(report)

    assert result["title"] == "Dataset quality summary"
    assert "passed all configured validation checks" in result["summary"]
    assert len(result["recommendations"]) > 0

def test_generate_ai_summary_mentions_failed_checks_when_report_failed():
    report = {
        "summary": {
            "overall_status": "failed",
            "failed_checks": 1,
            "failed_check_names": ["not_null_columns"],
        },
        "insights": [
            "Column 'age' contains 1 null value(s).",
        ],
    }

    result = generate_ai_summary(report)

    assert "failed 1 validation check" in result["summary"]
    assert "not_null_columns" in result["summary"]
    assert len(result["recommendations"]) > 0