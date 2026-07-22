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

df = pd.read_csv(PROJECT_ROOT / "data" / "marketing_campaigns.csv")

df = enrich_date(df, "Date")

print("=" * 60)
print("CAMPAIGN ANALYSIS")
print("=" * 60)

print(f"Total Records      : {len(df):,}")
print(f"Unique Campaigns   : {df['Campaign_Name'].nunique()}")
print(f"Campaign Types     : {df['Campaign_Type'].nunique()}")

campaign_distribution = (
    df["Campaign_Name"]
      .value_counts()
      .to_frame("Count")
)

campaign_distribution["Percentage"] = (
    campaign_distribution["Count"] / len(df) * 100
).round(2)

print(campaign_distribution)

campaign_type_distribution = (
    df["Campaign_Type"]
      .value_counts()
      .to_frame("Count")
)

campaign_type_distribution["Percentage"] = (
    campaign_type_distribution["Count"] / len(df) * 100
).round(2)

print(campaign_type_distribution)

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

print(campaign_budget)

campaign_budget["Spend Share (%)"] = (
    campaign_budget["Total_Spend"]
    / campaign_budget["Total_Spend"].sum()
    * 100
).round(2)


campaign_budget["Total_Spend"] = campaign_budget["Total_Spend"].map("{:,.0f}".format)
campaign_budget["Average_Spend"] = campaign_budget["Average_Spend"].map("{:,.2f}".format)
campaign_budget["Min_Spend"] = campaign_budget["Min_Spend"].map("{:,.0f}".format)
campaign_budget["Max_Spend"] = campaign_budget["Max_Spend"].map("{:,.0f}".format)

print(campaign_budget)