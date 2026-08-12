import json
import os

from dotenv import load_dotenv
from openai import OpenAI


def is_llm_enabled() -> bool:
    load_dotenv()
    return bool(os.getenv("OPENAI_API_KEY"))


def build_summary_prompt(report: dict) -> str:
    compact_report = {
        "dataset_name": report.get("dataset_name"),
        "input_file": report.get("input_file"),
        "summary": report.get("summary"),
        "insights": report.get("insights", []),
        "validations": report.get("validations", []),
    }

    return (
        "You are a data quality analyst. "
        "Create a concise executive summary for this data quality report. "
        "Focus on the overall status, failed checks, affected columns, and practical recommendations. "
        "Return the answer as JSON with keys: title, summary, recommendations. "
        "Recommendations must be a list of strings.\n\n"
        f"Report:\n{json.dumps(compact_report, indent=2, ensure_ascii=False)}"
    )


def generate_llm_summary(report: dict) -> dict:
    load_dotenv()

    model = os.getenv("OPENAI_MODEL", "gpt-5.1-mini")
    client = OpenAI()

    prompt = build_summary_prompt(report)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    text = response.output_text

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return {
            "title": "Dataset quality summary",
            "summary": text,
            "recommendations": [],
            "provider": "openai",
            "model": model,
        }

    parsed["provider"] = "openai"
    parsed["model"] = model

    return parsed