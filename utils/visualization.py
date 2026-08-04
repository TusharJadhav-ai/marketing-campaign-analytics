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
from matplotlib.ticker import StrMethodFormatter

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

# ==========================================
# Function 2
# ==========================================


def plot_horizontal_bar_chart(
    data,
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename=None
):


    """
    Create a horizontal bar chart.
    """
    data = data.sort_values(y, ascending=True)
    
    plt.figure(figsize=(9, 5))

    bars = plt.barh(data[x], data[y], height=0.65)

    # Add value labels
    # Add value labels
    for bar in bars:
        width = bar.get_width()

        plt.text(
        width + (data[y].max() * 0.01),
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}",
        va="center",
        fontsize=9
        )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=30)
    plt.grid(axis="y", linestyle="--", alpha=0.35)

    if filename:
        save_chart(filename)

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.show()

# ==========================================
# Function 3
# ==========================================
def plot_line_chart(
    data,
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename=None
):
    """
    Create a line chart.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        data[x],
        data[y],
        marker="o",
        markersize=7,
        linewidth=2.5
    )

    # Add value labels
    for x_value, y_value in zip(data[x], data[y]):
        plt.annotate(
        f"{y_value:.2f}",
        (x_value, y_value),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        fontsize=8
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(
        linestyle="--",
        alpha=0.35
    )

    ax = plt.gca()
    # ax.spines["top"].set_visible(False)
    # ax.spines["right"].set_visible(False)

    # plt.margins(y=0.08)

    plt.ylim(
        data[y].min() - 0.03,
        data[y].max() + 0.03
        )

    if filename:
        save_chart(filename)

    plt.show()

# ==========================================
# Function 5
# ==========================================
def plot_pie_chart(
    data,
    labels,
    values,
    title,
    explode=None,
    filename=None
):
    """
    Create a pie chart.
    """

    plt.figure(figsize=(7,7))

    explode = (0.03, 0, 0, 0)

    plt.pie(
        data[values],
        labels=data[labels],
        explode=explode,
        autopct="%1.1f%%",
        startangle=140,
        shadow=True,
        wedgeprops={
            "edgecolor": "white",
            "linewidth": 1
        },
        textprops={
            "fontsize":11
        }
    )

    plt.axis("equal")
    plt.title(title)

    plt.gca().xaxis.set_major_formatter(
    StrMethodFormatter('{x:,.0f}')
)
    if filename:
        save_chart(filename)

    plt.show()

# ==========================================
# Function 6
# ==========================================
def plot_scatter_chart(
    data,
    x,
    y,
    title,
    xlabel,
    ylabel,
    filename=None
):
    """
    Create a scatter chart.
    """

    plt.figure(figsize=(11, 6))

    plt.scatter(
        data[x],
        data[y],
        s=14,
        alpha=0.35,
        edgecolors="white",
        linewidth=0.2
    )

    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()

    plt.grid(
        linestyle="--",
        alpha=0.35
    )

    

    if filename:
        save_chart(filename)

    plt.show()