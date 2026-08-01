from data_sentinel.charts import generate_null_counts_chart


def test_generate_null_counts_chart_creates_file(tmp_path):
    null_counts = {
        "id": 0,
        "name": 0,
        "age": 1,
    }

    output_path = tmp_path / "null_counts.png"

    generate_null_counts_chart(null_counts, output_path)

    assert output_path.exists()