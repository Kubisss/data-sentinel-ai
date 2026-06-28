from data_sentinel.reporting import summarize_validation_results


def test_summarize_validation_results_returns_passed_when_all_checks_pass():
    validation_results = [
        {"check_name": "required_columns", "passed": True},
        {"check_name": "not_null_columns", "passed": True},
    ]

    result = summarize_validation_results(validation_results)

    assert result["overall_status"] == "passed"
    assert result["total_checks"] == 2
    assert result["passed_checks"] == 2
    assert result["failed_checks"] == 0
    assert result["failed_check_names"] == []

def test_summarize_validation_results_returns_failed_when_any_check_fails():
    validation_results = [
        {"check_name": "required_columns", "passed": True},
        {"check_name": "not_null_columns", "passed": False},
    ]

    result = summarize_validation_results(validation_results)

    assert result["overall_status"] == "failed"
    assert result["total_checks"] == 2
    assert result["passed_checks"] == 1
    assert result["failed_checks"] == 1
    assert result["failed_check_names"] == ["not_null_columns"]