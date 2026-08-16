# Data Sentinel AI

Data Sentinel AI is a Python data quality reporting tool for profiling CSV datasets, validating configurable rules, and generating human-readable reports with optional AI-assisted summaries.

The project is built as a portfolio project focused on data engineering, data quality, reporting, testing, and practical AI integration.

## Features

- CSV data loading
- JSON-based validation configuration
- Dataset profiling:
  - row and column counts
  - column names
  - null counts
  - duplicate row count
  - detected data types
- Data quality validation:
  - required columns
  - not-null columns
- Quality score calculation
- Rule-based insights
- Optional LLM summary provider:
  - Gemini
  - OpenAI-ready structure
  - rule-based fallback when no provider is configured
- Report generation:
  - JSON
  - Markdown
  - HTML
  - PDF
- Null-count chart generation
- Automated tests with pytest
- GitHub Actions CI pipeline

## Pipeline

```text
CSV + JSON config
        ↓
Load dataset
        ↓
Profile data
        ↓
Validate rules
        ↓
Calculate quality score
        ↓
Generate insights
        ↓
Generate AI summary
        ↓
Create charts
        ↓
Export JSON / Markdown / HTML / PDF reports
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
├── src/
│   └── data_sentinel/
├── tests/
├── .github/
│   └── workflows/
├── pyproject.toml
├── requirements.txt
├── .env.example
└── README.md
```

## Configuration

Validation rules are defined in a JSON file.

Example:

```json
{
  "dataset_name": "customers",
  "input_file": "data/sample/customers.csv",
  "required_columns": ["id", "name", "age", "city", "email"],
  "not_null_columns": ["id", "name", "email"]
}
```

The configuration controls which columns must exist in the dataset and which columns are not allowed to contain null values.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd data-sentinel-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

Install Playwright browser support for PDF export:

```bash
python -m playwright install chromium
```

## Running the project

Run the pipeline:

```bash
python -m data_sentinel.main
```

Generated reports are saved into the `reports/` directory:

```text
reports/
├── profile_report.json
├── profile_report.md
├── profile_report.html
├── profile_report.pdf
└── charts/
    └── null_counts.png
```

## Optional AI summary

The project supports optional LLM-generated summaries.

Create a local `.env` file based on `.env.example`:

```env
LLM_PROVIDER=none

# Gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite

# OpenAI
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5-mini
```

Supported provider values:

```text
none
gemini
openai
```

When no LLM provider is configured, the project automatically falls back to a deterministic rule-based summary.

This means the project can run without any API key.

## Running tests

Run all tests:

```bash
pytest
```

The test suite covers:

- CSV loading
- configuration loading
- dataframe profiling
- validation checks
- validation summary and quality score
- insights generation
- AI summary fallback behavior
- Markdown report rendering
- HTML report rendering
- chart file generation
- PDF export

## Example outputs

Sample reports are available in:

```text
examples/reports/
```

Included examples:

- `sample_profile_report.json`
- `sample_profile_report.md`
- `sample_profile_report.html`
- `sample_profile_report.pdf`
- `charts/null_counts.png`

The JSON report is intended for machines and downstream processing.

The Markdown, HTML, and PDF reports are intended for human-readable data quality review.

## CI

GitHub Actions runs the test suite automatically on push and pull request events.

The CI pipeline installs dependencies, prepares the project, installs Playwright browser support, and runs `pytest`.

## Tech stack

- Python
- pandas
- matplotlib
- Jinja2
- pytest
- Playwright
- Gemini / OpenAI provider structure
- GitHub Actions

## Roadmap

Possible future improvements:

- support multiple input datasets
- add more validation rules
- add historical report comparison
- add CLI arguments for config and output paths
- add database input support
- add dashboard view

## Why this project matters

Data quality is a key part of reliable data engineering and analytics workflows.

This project demonstrates how raw data can be loaded, profiled, validated, summarized, and exported into reports that are useful for both technical and non-technical users.

It also demonstrates a practical AI integration pattern: LLM-generated summaries are supported, but the project remains fully usable through a deterministic fallback when no external provider is configured.