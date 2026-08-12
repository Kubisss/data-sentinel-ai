from data_sentinel.llm import build_summary_prompt


def test_build_summary_prompt_contains_report_information():
    report = {
        "dataset_name": "customers",
        "input_file": "data/sample/customers.csv",
        "summary": {
            "overall_status": "failed",
            "quality_score": 50.0,
            "failed_checks": 1,
            "failed_check_names": ["not_null_columns"],
        },
        "insights": [
            "Column 'age' contains 1 null value(s)."
        ],
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

    prompt = build_summary_prompt(report)

    assert "customers" in prompt
    assert "not_null_columns" in prompt
    assert "age" in prompt
    assert "quality_score" in prompt