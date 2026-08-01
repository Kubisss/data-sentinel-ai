import pytest

from data_sentinel.renderers import render_markdown_report, render_html_report


@pytest.fixture
def sample_report():
    return {
        "input_file": "data/sample/customers.csv",
        "summary": {
            "overall_status": "failed",
            "quality_score": 50.0,
            "total_checks": 2,
            "passed_checks": 1,
            "failed_checks": 1,
            "failed_check_names": ["not_null_columns"],
        },
        "profile": {
            "num_rows": 5,
            "num_columns": 5,
            "column_names": ["id", "name", "age", "city", "email"],
            "null_counts_per_column": {
                "id": 0,
                "name": 0,
                "age": 1,
                "city": 0,
                "email": 0,
            },
            "duplicate_rows": 0,
            "data_types": {
                "id": "int64",
                "name": "str",
                "age": "float64",
                "city": "str",
                "email": "str",
            },
        },
        "validations": [
            {
                "check_name": "required_columns",
                "passed": True,
                "missing_columns": [],
            },
            {
                "check_name": "not_null_columns",
                "passed": False,
                "columns_with_nulls": {
                    "age": 1,
                },
            },
        ],
    }


def test_render_markdown_report_returns_string(sample_report):
    markdown = render_markdown_report(sample_report)

    assert isinstance(markdown, str)


def test_render_markdown_report_contains_title(sample_report):
    markdown = render_markdown_report(sample_report)

    assert "# Data Quality Report" in markdown


def test_render_markdown_report_contains_summary(sample_report):
    markdown = render_markdown_report(sample_report)

    assert "Quality score" in markdown
    assert "50.0%" in markdown
    assert "failed" in markdown


def test_render_markdown_report_contains_null_counts(sample_report):
    markdown = render_markdown_report(sample_report)

    assert "| age | 1 |" in markdown


def test_render_markdown_report_contains_validation_results(sample_report):
    markdown = render_markdown_report(sample_report)

    assert "required_columns" in markdown
    assert "not_null_columns" in markdown
    assert "age" in markdown

def test_render_html_report_contains_report_title(sample_report):
    html = render_html_report(sample_report)

    assert "Data Quality Report" in html
    assert "data/sample/customers.csv" in html
    assert "50.0%" in html