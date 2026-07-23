"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 03_channel_analysis.py

Objective
---------
Analyze marketing channel distribution, spend allocation,
and performance metrics (CTR, CPC, Clicks, and Impressions)
to identify the most effective digital marketing channels.
"""

# ==========================================
# Imports
# ==========================================

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from utils.validation import (
    validate_shape,
    validate_dtypes,
    validate_missing,
    validate_duplicates,
    validate_summary
)

from utils.wrangling import (
    enrich_date
)

from utils.reporting import print_section
from utils.reporting import print_subsection
from utils.reporting import print_business_insight

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
# Channel Overview
# ==========================================
print_section("CHANNEL ANALYSIS")

print(f"Total Channels : {df['Channel'].nunique()}")

print(df["Channel"].unique())

# ==========================================
# Channel Distribution
# ==========================================
channel_distribution = (
    df["Channel"]
      .value_counts()
      .to_frame("Count")
)

channel_distribution["Percentage"] = (
    channel_distribution["Count"]
    / len(df)
    * 100
).round(2)

print_subsection("Channel Distribution")
print(channel_distribution)

# ==========================================
# channel Budget Analysis
# ==========================================

channel_budget = (
    df.groupby("Channel")
      .agg(
          Total_Spend=("Spend","sum"),
          Average_Spend=("Spend","mean"),
          Min_Spend=("Spend","min"),
          Max_Spend=("Spend","max")
      )
      .round(2)
      .sort_values("Total_Spend",ascending=False)
)

channel_budget["Spend Share (%)"] = (
    channel_budget["Total_Spend"]
    / channel_budget["Total_Spend"].sum()
    *100
).round(2)

channel_budget["Total_Spend"] = (
    channel_budget["Total_Spend"]
    .map("{:,.0f}".format)
)

print_subsection("Channel Budget Analysis")
print(channel_budget)

# ==========================================
# Customer Segment Performance Analysis
# ==========================================

channel_performance = (
    df.groupby("Channel")
      .agg(
          Average_CTR=("CTR","mean"),
          Average_CPC=("CPC","mean"),
          Total_Clicks=("Clicks","sum"),
          Total_Impressions=("Impressions","sum")
      )
      .round(2)
      .sort_values("Average_CTR", ascending=False)
)

channel_performance["Click Share (%)"] = (
    channel_performance["Total_Clicks"]
    / channel_performance["Total_Clicks"].sum()
    *100
).round(2)

channel_performance["Impression Share (%)"] = (
    channel_performance["Total_Impressions"]
    / channel_performance["Total_Impressions"].sum()
    *100
).round(2)

print_subsection("Channel Performance Analysis")
print(channel_performance)

business_insight = """
• Google Search and Email demonstrate strong click-through performance,
• while LinkedIn has the highest CPC, indicating a premium advertising channel.
"""
print_business_insight(business_insight)

