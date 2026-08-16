from pathlib import Path

import matplotlib.pyplot as plt


def generate_null_counts_chart(null_counts: dict, output_path: str) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    items_with_nulls = [
        (column, count)
        for column, count in null_counts.items()
        if count > 0
    ]

    if items_with_nulls:
        chart_items = items_with_nulls
    else:
        chart_items = list(null_counts.items())

    columns = [item[0] for item in chart_items]
    counts = [item[1] for item in chart_items]

    figure_height = max(4, len(columns) * 0.5)

    plt.figure(figsize=(10, figure_height))
    plt.barh(columns, counts)

    plt.title("Null values by column")
    plt.xlabel("Null count")
    plt.ylabel("Column")

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()