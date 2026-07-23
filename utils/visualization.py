"""
Marketing Campaign Analytics
============================
Module : Visualization Utilities
File   : visualization.py

Objective
---------
Reusable visualization functions for
Business Intelligence reporting.
"""
from pathlib import Path

import matplotlib.pyplot as plt

# ==========================================
# Create Output Folder
# ==========================================

OUTPUT_DIR = (
    Path(__file__).resolve().parent.parent
    / "outputs"
    / "charts"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def save_chart(filename):
    """
    Save chart inside outputs/charts.
    """

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Chart saved : {filename}")


# ==========================================
# Function 1
# ==========================================
def plot_bar_chart(
    data,
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename=None
):
    """
    Create a vertical bar chart.
    """

    plt.figure(figsize=(9, 5))

    bars = plt.bar(data[x], data[y], width=0.65)

    # Add value labels
    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.08,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=30)
    plt.grid(axis="y", linestyle="--", alpha=0.35)

    if filename:
        save_chart(filename)

    plt.show()


