from data_sentinel.llm import build_summary_prompt, parse_llm_summary_response


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


def test_parse_llm_summary_response_parses_plain_json():
    text = """
    {
        "title": "Dataset quality summary",
        "summary": "The dataset has good quality.",
        "recommendations": ["Continue monitoring."]
    }
    """

    result = parse_llm_summary_response(
        text=text,
        provider="gemini",
        model="gemini-2.5-flash-lite",
    )

    assert result["title"] == "Dataset quality summary"
    assert result["summary"] == "The dataset has good quality."
    assert result["recommendations"] == ["Continue monitoring."]
    assert result["provider"] == "gemini"
    assert result["parsed"] is True

def test_parse_llm_summary_response_parses_markdown_json_block():
    text = """
    ```json
    {
        "title": "Dataset quality summary",
        "summary": "One validation check failed.",
        "recommendations": ["Review the age column."]
    }
    """

    result = parse_llm_summary_response(
        text=text,
        provider="gemini",
        model="gemini-2.5-flash-lite",
    )

    assert result["title"] == "Dataset quality summary"
    assert result["summary"] == "One validation check failed."
    assert result["recommendations"] == ["Review the age column."]
    assert result["parsed"] is True

def test_parse_llm_summary_response_falls_back_when_text_is_not_json():
    text = "This is not valid JSON."

    result = parse_llm_summary_response(
        text=text,
        provider="gemini",
        model="gemini-2.5-flash-lite",
    )

    assert result["title"] == "Dataset quality summary"
    assert result["summary"] == "This is not valid JSON."
    assert result["recommendations"] == []
    assert result["parsed"] is False