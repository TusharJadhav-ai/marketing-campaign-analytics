"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 07_time_series_analysis.py

Objective
---------
Analyze marketing performance over time
to identify seasonal trends, campaign
patterns, and engagement behaviour.
"""
# ==========================================
# Imports
# ==========================================

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from utils.validation import validate_summary

from utils.wrangling import (
    enrich_date
)

from utils.reporting import print_section
from utils.reporting import print_subsection
from utils.reporting import print_business_insight

from utils.visualization import plot_line_chart
from utils.visualization import plot_scatter_chart

# ==========================================
# Load Dataset
# ==========================================
df = pd.read_csv(PROJECT_ROOT / "data" / "marketing_campaigns.csv")

df = enrich_date(df, "Date")

# ==========================================
# Wrangling
# ==========================================
validate_summary(df)

# ==========================================
# Overview
# ==========================================
print_section("TIME SERIES ANALYSIS")

print(f"Date Range : {df['Date'].min()} to {df['Date'].max()}")

print(f"Total Months : {df['Month'].nunique()}")

print(f"Total Quarters : {df['Quarter'].nunique()}")

# ==========================================
# Monthly Performance
# ==========================================
monthly_performance = (
    df.groupby("Month")
      .agg(
          Total_Spend=("Spend", "sum"),
          Average_CTR=("CTR", "mean"),
          Average_CPC=("CPC", "mean"),
          Total_Clicks=("Clicks", "sum"),
          Total_Impressions=("Impressions", "sum")
      )
      .round(2)
)

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_performance = monthly_performance.reindex(month_order)

print_subsection("Monthly Performance Analysis")
print(monthly_performance)

# plot_line_chart(
#     data=monthly_performance.reset_index(),
#     x="Month",
#     y="Average_CTR",
#     title="Monthly Average CTR",
#     xlabel="Month",
#     ylabel="Average CTR (%)",
#     filename="monthly_ctr.png"
# )

# ==========================================
# Quarter Performance
# ==========================================

quarter_performance = (
    df.groupby("Quarter")
      .agg(
          Total_Spend=("Spend", "sum"),
          Average_CTR=("CTR", "mean"),
          Average_CPC=("CPC", "mean"),
          Total_Clicks=("Clicks", "sum"),
          Total_Impressions=("Impressions", "sum")
      )
      .round(2)
      .sort_index()
)

print_subsection("Quarter Performance Analysis")
print(quarter_performance)

weekday_performance = (
    df.groupby("Weekday")
      .agg(
          Total_Spend=("Spend", "sum"),
          Average_CTR=("CTR", "mean"),
          Average_CPC=("CPC", "mean"),
          Total_Clicks=("Clicks", "sum"),
          Total_Impressions=("Impressions", "sum")
      )
      .round(2)
      .sort_index()
)

print_subsection("Weekday Performance Analysis")
print(weekday_performance)

plot_scatter_chart(
    data=df,
    x="Spend",
    y="CTR",
    title="Spend vs CTR",
    xlabel="Marketing Spend",
    ylabel="CTR (%)",
    filename="spend_vs_ctr.png"
)

# ==========================================
# Business Insight
# ==========================================
business_insight = """
• Marketing spend remains relatively consistent throughout the year, with October recording the highest total spend (53.33M), indicating increased investment during the final quarter.
• Q4 receives the highest overall marketing budget (155.17M) and generates the highest total clicks (13.18M), highlighting stronger campaign activity towards year-end.
• September achieves the highest average CTR (3.58%), suggesting better campaign engagement despite lower overall spend.
• Wednesday generates the highest total clicks (7.36M) and impressions (303.63M), while Saturday records the highest average CTR (3.49%), indicating stronger user engagement over the weekend.
• Overall performance remains stable across months, quarters, and weekdays, reflecting a balanced marketing strategy with no significant seasonal performance fluctuations.
"""
print_business_insight(business_insight)