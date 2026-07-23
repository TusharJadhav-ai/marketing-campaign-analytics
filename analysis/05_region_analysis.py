"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 05_region_analysis.py

Objective
---------
Analyze marketing performance across regions
to identify regional spending patterns,
customer engagement, and campaign effectiveness.
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
print_section("REGION ANALYSIS")

print(f"Total Regions : {df['Region'].nunique()}")

print(df["Region"].unique())

# ==========================================
# Distribution
# ==========================================
region_distribution = (
    df["Region"]
      .value_counts()
      .to_frame("Count")
)

region_distribution["Percentage"] = (
    region_distribution["Count"]
    / len(df)
    * 100
).round(2)

print_subsection("Region Distribution")

print(region_distribution)

# ==========================================
# Budget Analysis
# ==========================================
region_budget = (
    df.groupby("Region")
      .agg(
          Total_Spend=("Spend","sum"),
          Average_Spend=("Spend","mean"),
          Min_Spend=("Spend","min"),
          Max_Spend=("Spend","max")
      )
      .round(2)
      .sort_values("Total_Spend", ascending=False)
)

region_budget["Spend Share (%)"] = (
    region_budget["Total_Spend"]
    / region_budget["Total_Spend"].sum()
    *100
).round(2)

region_budget["Total_Spend"] = (
    region_budget["Total_Spend"]
    .map("{:,.0f}".format)
)

print_subsection("Customer Region Budget Analysis")
print(region_budget)

# ==========================================
# Performance Analysis
# ==========================================
region_performance = (
    df.groupby("Region")
      .agg(
          Average_CTR=("CTR","mean"),
          Average_CPC=("CPC","mean"),
          Total_Clicks=("Clicks","sum"),
          Total_Impressions=("Impressions","sum")
      )
      .round(2)
)

region_performance["Click Share (%)"] = (
    region_performance["Total_Clicks"]
    / region_performance["Total_Clicks"].sum()
    *100
).round(2)

region_performance["Impression Share (%)"] = (
    region_performance["Total_Impressions"]
    / region_performance["Total_Impressions"].sum()
    *100
).round(2)

print_subsection("Customer Region Performance Analysis")
print(region_performance)

# ==========================================
# Business Insight
# ==========================================
business_insight = """
• Marketing performance is relatively balanced across all regions, indicating a well-distributed campaign strategy.
• West contributes the highest Impression Share (20.99%), providing the widest audience reach among all regions.
• Central generates the highest Click Share (21.00%), demonstrating strong audience engagement.
• North records the highest average CTR (3.53%), suggesting slightly better campaign effectiveness despite a similar budget allocation.
• Average CPC remains consistent across regions (approximately 25–26), indicating uniform advertising costs and efficient budget distribution.
"""

print_business_insight(business_insight)




