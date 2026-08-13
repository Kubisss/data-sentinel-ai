from data_sentinel.pdf import render_pdf_report


def test_render_pdf_report_creates_pdf_file(tmp_path):
    html_path = tmp_path / "report.html"
    output_path = tmp_path / "report.pdf"

    html_path.write_text(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Report</title>
        </head>
        <body>
            <h1>Data Quality Report</h1>
            <p>Hello PDF.</p>
        </body>
        </html>
        """,
        encoding="utf-8",
    )

    render_pdf_report(str(html_path), str(output_path))

    assert output_path.exists()
    assert output_path.stat().st_size > 0