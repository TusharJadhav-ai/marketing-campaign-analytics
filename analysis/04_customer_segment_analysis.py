"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 04_customer_segment_analysis.py

Objective
---------
Analyze marketing performance across customer segments
to identify high-value audiences based on spend,
engagement, and campaign effectiveness.
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
# Customer Segment Overview
# ==========================================
print_section("Customer Segment Analysis")

print(f"Total Customer Segments : {df['Customer_Segment'].nunique()}")

print(df["Customer_Segment"].unique())

# ==========================================
# Customer Segment Distribution
# ==========================================
segment_distribution = (
    df["Customer_Segment"]
      .value_counts()
      .to_frame("Count")
)

segment_distribution["Percentage"] = (
    segment_distribution["Count"]
    / len(df)
    * 100
).round(2)

print_subsection("Customer Segment Distribution")
print(segment_distribution)

# ==========================================
# Customer Segment Budget Analysis
# ==========================================
segment_budget = (
    df.groupby("Customer_Segment")
      .agg(
          Total_Spend=("Spend","sum"),
          Average_Spend=("Spend","mean"),
          Min_Spend=("Spend","min"),
          Max_Spend=("Spend","max")
      )
      .round(2)
      .sort_values("Total_Spend", ascending=False)
)
segment_budget["Spend Share (%)"] = (
    segment_budget["Total_Spend"]
    / segment_budget["Total_Spend"].sum()
    *100
).round(2)

print_subsection("Customer Segment Budget Analysis")
print(segment_budget)

# ==========================================
# Customer Segment Performance Analysis
# ==========================================
segment_performance = (
    df.groupby("Customer_Segment")
      .agg(
          Average_CTR=("CTR","mean"),
          Average_CPC=("CPC","mean"),
          Total_Clicks=("Clicks","sum"),
          Total_Impressions=("Impressions","sum")
      )
      .round(2)
)

segment_performance["Click Share (%)"] = (
    segment_performance["Total_Clicks"]
    / segment_performance["Total_Clicks"].sum()
    *100
).round(2)

# segment_performance = segment_performance.sort_values(
#     "Click Share (%)",
#     ascending=False
# )

segment_performance["Impression Share (%)"] = (
    segment_performance["Total_Impressions"]
    / segment_performance["Total_Impressions"].sum()
    *100
).round(2)

print_subsection("Customer Segment Performance Analysis")
print(segment_performance)

business_insight = """
• Loyal customers achieve the highest average CTR (4.60%), indicating stronger engagement compared to other customer segments.
• Returning customers contribute the highest Click Share (28.04%), making them the largest source of campaign engagement.
• New customers account for the highest Impression Share (36.46%), suggesting that current marketing efforts are heavily focused on customer acquisition.
• Premium customers have the highest average CPC (30.98), reflecting the higher cost of targeting high-value customer audiences.
• A balanced marketing strategy should continue acquiring New customers while increasing retention campaigns for Loyal and Returning customers to maximize engagement efficiency.
"""

print_business_insight(business_insight)


