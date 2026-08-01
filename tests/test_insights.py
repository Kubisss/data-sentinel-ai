from data_sentinel.insights import generate_insights


def test_generate_insights_returns_passed_message_when_all_checks_pass():
    report = {
        "profile": {
            "num_rows": 5,
            "num_columns": 5,
        },
        "summary": {
            "overall_status": "passed",
            "quality_score": 100.0,
            "failed_checks": 0,
        },
        "validations": [
            {
                "check_name": "required_columns",
                "passed": True,
            }
        ],
    }

    insights = generate_insights(report)

    assert "Dataset contains 5 rows and 5 columns." in insights
    assert "Overall quality score is 100.0%." in insights
    assert "All validation checks passed." in insights

def test_generate_insights_describes_failed_not_null_check():
    report = {
        "profile": {
            "num_rows": 5,
            "num_columns": 5,
        },
        "summary": {
            "overall_status": "failed",
            "quality_score": 50.0,
            "failed_checks": 1,
        },
        "validations": [
            {
                "check_name": "not_null_columns",
                "passed": False,
                "columns_with_nulls": {
                    "age": 1,
                },
            }
        ],
    }

    insights = generate_insights(report)

    assert "1 validation check(s) failed." in insights
    assert "Check 'not_null_columns' failed." in insights
    assert "Column 'age' contains 1 null value(s)." in insights