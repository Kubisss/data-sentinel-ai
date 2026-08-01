# Data Sentinel AI

Data Sentinel AI is a Python-based data quality and reporting project focused on profiling datasets, validating configurable rules, generating human-readable reports, and preparing a foundation for AI-assisted data quality insights.

The project is designed as a portfolio project for data engineering, data science, and AI-agent-oriented workflows.

## Project goal

The goal of this project is to build a small but realistic data quality pipeline that can:

* load tabular data from a CSV file,
* generate a dataset profile,
* validate data quality rules from a configuration file,
* calculate an overall quality score,
* generate rule-based insights,
* create JSON, Markdown, and HTML reports,
* generate charts for selected data quality metrics,
* provide a foundation for a future LLM-powered AI summary agent.

## Current features

* CSV data loading
* JSON-based dataset schema configuration
* Data profiling:

  * row count
  * column count
  * column names
  * null counts per column
  * duplicate row count
  * detected data types
* Data validation:

  * required columns check
  * not-null columns check
* Validation summary:

  * overall status
  * total checks
  * passed checks
  * failed checks
  * failed check names
  * quality score
* Rule-based insights summary
* AI-style summary layer
* Markdown report generation
* HTML report generation
* Null-count chart generation
* Unit tests with pytest

## Pipeline overview

```text
CSV input
   ↓
Load dataset
   ↓
Profile dataframe
   ↓
Validate configured rules
   ↓
Calculate summary and quality score
   ↓
Generate insights
   ↓
Generate AI-style summary
   ↓
Generate charts
   ↓
Export JSON, Markdown and HTML reports
```

## Project structure

```text
data-sentinel-ai/
├── config/
│   └── customers_schema.json
├── data/
│   └── sample/
│       └── customers.csv
├── examples/
│   └── reports/
│       ├── sample_profile_report.json
│       ├── sample_profile_report.md
│       ├── sample_profile_report.html
│       └── charts/
│           └── null_counts.png
├── reports/
├── src/
│   └── data_sentinel/
│       ├── agents.py
│       ├── charts.py
│       ├── config.py
│       ├── insights.py
│       ├── loaders.py
│       ├── main.py
│       ├── profiling.py
│       ├── renderers.py
│       ├── reporting.py
│       ├── validation.py
│       └── templates/
│           └── report.html
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Configuration

Validation rules are defined in a JSON schema file.

Example:

```json
{
    "dataset_name": "customers",
    "input_file": "data/sample/customers.csv",
    "required_columns": ["id", "name", "age", "city", "email"],
    "not_null_columns": ["id", "name", "email"]
}
```

The configuration controls which columns must exist and which columns are not allowed to contain null values.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd data-sentinel-ai
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the project in editable mode:

```bash
pip install -e .
```

## Running the project

Run the pipeline:

```bash
python -m data_sentinel.main
```

The generated reports will be saved into the `reports/` directory:

```text
reports/
├── profile_report.json
├── profile_report.md
├── profile_report.html
└── charts/
    └── null_counts.png
```

## Running tests

Run all tests:

```bash
pytest
```

The test suite covers:

* CSV loading
* configuration loading
* dataframe profiling
* validation checks
* validation summary and quality score
* insights generation
* AI-style summary generation
* Markdown report rendering
* HTML report rendering
* chart file generation

## Example outputs

Curated sample outputs are available in:

```text
examples/reports/
```

Included examples:

* `sample_profile_report.json`
* `sample_profile_report.md`
* `sample_profile_report.html`
* `charts/null_counts.png`

The JSON report is intended for machines and downstream processing.
The Markdown and HTML reports are intended for human-readable data quality review.

## AI summary layer

The current AI summary layer is rule-based and deterministic. It generates a human-readable summary and recommendations based on validation results and generated insights.

This design prepares the project for future integration with an LLM provider, while keeping the project fully runnable without an API key.

## Roadmap

Planned improvements:

* Add support for multiple datasets
* Add more validation rules:

  * duplicate checks by selected columns
  * accepted value ranges
  * regex-based email validation
  * numeric range validation
  * date format validation
* Add historical report comparison
* Add LLM-powered summary generation
* Add PDF export
* Add Streamlit dashboard
* Add Docker support
* Add GitHub Actions CI pipeline

## Tech stack

* Python
* pandas
* matplotlib
* Jinja2
* pytest
* JSON configuration
* Markdown and HTML reporting

## Why this project matters

Data quality is a critical part of data engineering and analytics workflows. This project demonstrates how raw data can be loaded, profiled, validated, summarized, and transformed into reports that are useful for both technical and non-technical users.

The project is intentionally built step by step, with clean modules and tests, so it can grow into a more advanced data quality monitoring tool with AI-assisted explanations.