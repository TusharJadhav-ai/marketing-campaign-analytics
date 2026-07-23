"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 02_campaign_analysis.py

Objective
---------
Analyze campaign distribution, marketing spend, and
campaign performance.
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
print_section("CAMPAIGN ANALYSIS")

print(f"Total Records      : {len(df):,}")
print(f"Unique Campaigns   : {df['Campaign_Name'].nunique()}")
print(f"Campaign Types     : {df['Campaign_Type'].nunique()}")

# ==========================================
# Distribution
# ==========================================
campaign_distribution = (
    df["Campaign_Name"]
      .value_counts()
      .to_frame("Count")
)

campaign_distribution["Percentage"] = (
    campaign_distribution["Count"] 
    / len(df) 
    * 100
).round(2)

print_subsection("Campaign Distribution")
print(campaign_distribution)

# ==========================================
# Campaign Type Distribution
# ==========================================

campaign_type_distribution = (
    df["Campaign_Type"]
      .value_counts()
      .to_frame("Count")
)

campaign_type_distribution["Percentage"] = (
    campaign_type_distribution["Count"] / len(df) * 100
).round(2)

print_subsection("Campaign Type Distribution")
print(campaign_type_distribution)

# ==========================================
# Budget Analysis
# ==========================================

campaign_budget = (
    df.groupby("Campaign_Type")
      .agg(
          Total_Spend=("Spend", "sum"),
          Average_Spend=("Spend", "mean"),
          Min_Spend=("Spend", "min"),
          Max_Spend=("Spend", "max")
      )
      .round(2)
      .sort_values("Total_Spend", ascending=False)
)

campaign_budget["Spend Share (%)"] = (
    campaign_budget["Total_Spend"]
    / campaign_budget["Total_Spend"].sum()
    * 100
).round(2)

campaign_budget["Total_Spend"] = (
    campaign_budget["Total_Spend"]
    .map("{:,.0f}".format)
)

print_subsection("Campaign Budget Analysis")
print(campaign_budget)

# ==========================================
# Performance Analysis
# ==========================================

campaign_performance = (
    df.groupby("Campaign_Type")
      .agg(
          Average_CTR=("CTR","mean"),
          Average_CPC=("CPC","mean"),
          Total_Clicks=("Clicks","sum"),
          Total_Impressions=("Impressions","sum")
      )
      .round(2)
      .sort_values("Average_CTR", ascending=False)
)

campaign_performance["Click Share (%)"] = (
    campaign_performance["Total_Clicks"]
    / campaign_performance["Total_Clicks"].sum()
    *100
).round(2)

campaign_performance["Impression Share (%)"] = (
    campaign_performance["Total_Impressions"]
    / campaign_performance["Total_Impressions"].sum()
    *100
).round(2)

print_subsection("Campaign Performance Analysis")
print(campaign_performance)

# ==========================================
# Business Insight
# ==========================================
business_insight = """
• Festival campaigns receive the highest marketing investment, accounting for over half of the total campaign budget.
• Seasonal campaigns represent approximately one-quarter of the total marketing spend, supporting recurring promotional activities.
• Promotional campaigns maintain moderate investment levels, balancing customer engagement and sales objectives.
• Clearance campaigns receive the lowest budget allocation, reflecting their tactical role in inventory management.
• Marketing investment should continue prioritizing high-performing campaign types while regularly evaluating return on investment across all campaign categories.
"""
print_business_insight(business_insight)
