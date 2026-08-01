from pathlib import Path

import matplotlib.pyplot as plt


def generate_null_counts_chart(null_counts, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    columns = list(null_counts.keys())
    counts = list(null_counts.values())

    plt.figure()
    plt.bar(columns, counts)
    plt.title("Null values by column")
    plt.xlabel("Column")
    plt.ylabel("Null count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()