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

def test_summarize_validation_results_returns_quality_score_100_when_all_checks_pass():
    validation_results = [
        {"check_name": "required_columns", "passed": True},
        {"check_name": "not_null_columns", "passed": True},
    ]

    result = summarize_validation_results(validation_results)

    assert result["quality_score"] == 100.0

def test_summarize_validation_results_returns_quality_score_0_when_no_checks_pass():
    validation_results = [
        {"check_name": "required_columns", "passed": False},
        {"check_name": "not_null_columns", "passed": False},
    ]

    result = summarize_validation_results(validation_results)

    assert result["quality_score"] == 0.0

def test_summarize_validation_results_returns_quality_score_50_when_half_checks_pass():
    validation_results = [
        {"check_name": "required_columns", "passed": True},
        {"check_name": "not_null_columns", "passed": False},
    ]

    result = summarize_validation_results(validation_results)

    assert result["quality_score"] == 50.0