import json
import re
import os

from dotenv import load_dotenv
from openai import OpenAI
from google import genai
from google.genai import types

def build_summary_prompt(report: dict) -> str:
    compact_report = {
        "dataset_name": report.get("dataset_name"),
        "summary": report.get("summary"),
        "insights": report.get("insights", []),
    }

    return (
        "You are a data quality analyst.\n"
        "Create a concise executive summary for this data quality report.\n"
        "Return only valid JSON with this structure:\n"
        "{\n"
        '  "title": "string",\n'
        '  "summary": "string",\n'
        '  "recommendations": ["string"]\n'
        "}\n\n"
        f"Report:\n{json.dumps(compact_report, ensure_ascii=False)}"
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

def parse_llm_summary_response(text: str, provider: str, model: str) -> dict:
    cleaned_text = text.strip()

    if cleaned_text.startswith("```"):
        cleaned_text = re.sub(r"^```json\s*", "", cleaned_text)
        cleaned_text = re.sub(r"^```\s*", "", cleaned_text)
        cleaned_text = re.sub(r"\s*```$", "", cleaned_text)

    json_match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)

    if json_match:
        cleaned_text = json_match.group(0)

    try:
        parsed = json.loads(cleaned_text)
    except json.JSONDecodeError:
        return {
            "title": "Dataset quality summary",
            "summary": text,
            "recommendations": [],
            "provider": provider,
            "model": model,
            "parsed": False,
        }

    recommendations = parsed.get("recommendations", [])

    if isinstance(recommendations, str):
        recommendations = [recommendations]

    if not isinstance(recommendations, list):
        recommendations = []

    return {
        "title": parsed.get("title", "Dataset quality summary"),
        "summary": parsed.get("summary", ""),
        "recommendations": recommendations,
        "provider": provider,
        "model": model,
        "parsed": True,
    }

def generate_gemini_summary(report: dict) -> dict:
    load_dotenv()

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    timeout_ms = int(os.getenv("LLM_TIMEOUT_MS", "30000"))

    client = genai.Client(
         http_options=types.HttpOptions(timeout=timeout_ms)
    )

    prompt = build_summary_prompt(report)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
            max_output_tokens=500,
        ),
    )

    return parse_llm_summary_response(
        text=response.text,
        provider="gemini",
        model=model,
    )

def generate_openai_summary(report: dict) -> dict:
    load_dotenv()

    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
    client = OpenAI()

    prompt = build_summary_prompt(report)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return parse_llm_summary_response(
    text=response.output_text,
    provider="openai",
    model=model,
)

def generate_llm_summary(report: dict) -> dict:
    provider = get_llm_provider()

    if provider == "gemini":
        return generate_gemini_summary(report)

    if provider == "openai":
        return generate_openai_summary(report)

    raise ValueError(f"Unsupported LLM provider: {provider}")