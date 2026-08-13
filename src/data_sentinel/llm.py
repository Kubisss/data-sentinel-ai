import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from google import genai

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


def get_llm_provider() -> str:
    load_dotenv()
    return os.getenv("LLM_PROVIDER", "none").lower()


def is_llm_enabled() -> bool:
    provider = get_llm_provider()

    if provider == "openai":
        return bool(os.getenv("OPENAI_API_KEY"))

    if provider == "gemini":
        return bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))

    return False

def generate_gemini_summary(report: dict) -> dict:
    load_dotenv()

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    client = genai.Client()

    prompt = build_summary_prompt(report)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    text = response.text

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return {
            "title": "Dataset quality summary",
            "summary": text,
            "recommendations": [],
            "provider": "gemini",
            "model": model,
        }

    parsed["provider"] = "gemini"
    parsed["model"] = model

    return parsed

def generate_openai_summary(report: dict) -> dict:
    load_dotenv()

    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
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

def generate_llm_summary(report: dict) -> dict:
    provider = get_llm_provider()

    if provider == "gemini":
        return generate_gemini_summary(report)

    if provider == "openai":
        return generate_openai_summary(report)

    raise ValueError(f"Unsupported LLM provider: {provider}")