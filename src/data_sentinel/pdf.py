from pathlib import Path

from playwright.sync_api import sync_playwright


def render_pdf_report(html_path: str, output_path: str) -> None:
    html_path = Path(html_path).resolve()
    output_path = Path(output_path).resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"HTML report does not exist: {html_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(html_path.as_uri(), wait_until="networkidle")

        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
        )

        browser.close()