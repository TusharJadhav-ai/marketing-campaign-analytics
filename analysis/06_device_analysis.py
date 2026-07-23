"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 06_device_analysis.py

Objective
---------
Analyze marketing performance across devices
to understand spending patterns,
user engagement, and campaign effectiveness.
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
print_section("DEVICE ANALYSIS")

print(f"Total Devices : {df['Device'].nunique()}")

print(df["Device"].unique())

# ==========================================
# Distribution
# ==========================================
device_distribution = (
    df["Device"]
      .value_counts()
      .to_frame("Count")
)

device_distribution["Percentage"] = (
    device_distribution["Count"]
    / len(df)
    * 100
).round(2)

print_subsection("Device Distribution")

print(device_distribution)

# ==========================================
# Budget Analysis
# ==========================================
device_budget = (
    df.groupby("Device")
      .agg(
          Total_Spend=("Spend","sum"),
          Average_Spend=("Spend","mean"),
          Min_Spend=("Spend","min"),
          Max_Spend=("Spend","max")
      )
      .round(2)
      .sort_values("Total_Spend", ascending=False)
)

device_budget["Spend Share (%)"] = (
    device_budget["Total_Spend"]
    / device_budget["Total_Spend"].sum()
    * 100
).round(2)

device_budget["Total_Spend"] = (
    device_budget["Total_Spend"]
    .map("{:,.0f}".format)
)

print_subsection("Device Budget Analysis")

print(device_budget)

# ==========================================
# Performance Analysis
# ==========================================
device_performance = (
    df.groupby("Device")
      .agg(
          Average_CTR=("CTR","mean"),
          Average_CPC=("CPC","mean"),
          Total_Clicks=("Clicks","sum"),
          Total_Impressions=("Impressions","sum")
      )
      .round(2)
)

device_performance["Click Share (%)"] = (
    device_performance["Total_Clicks"]
    / device_performance["Total_Clicks"].sum()
    *100
).round(2)

device_performance["Impression Share (%)"] = (
    device_performance["Total_Impressions"]
    / device_performance["Total_Impressions"].sum()
    *100
).round(2)

print_subsection("Customer Device Performance Analysis")
print(device_performance)

# ==========================================
# Business Insight
# ==========================================
business_insight = """
• Mobile devices generate the highest Click Share (63.35%) and Impression Share (73.49%), confirming that mobile is the primary platform for campaign reach and audience engagement.
• Desktop users achieve the highest average CTR (4.39%), indicating stronger engagement despite reaching a smaller audience.
• Desktop campaigns also have the highest average CPC (30.20) compared to Mobile (23.76), reflecting the premium cost of reaching desktop users.
• Mobile advertising delivers significantly higher traffic volumes at a lower cost, making it the preferred platform for scaling campaign reach.
• An effective digital marketing strategy should prioritize Mobile for audience acquisition while leveraging Desktop campaigns for higher engagement and premium customer interactions.
"""
print_business_insight(business_insight)
