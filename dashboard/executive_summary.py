"""
Marketing Campaign Analytics
============================
Module : Executive Dashboard
File   : executive_summary.py

Objective
---------
Provide a high-level business summary of the
marketing campaign performance by consolidating
key insights from all analytical modules.
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
from utils.wrangling import enrich_date

from utils.reporting import (
    print_section,
    print_subsection,
    print_business_insight
)

from utils.reporting import print_key_findings
from utils.reporting import print_recommendations

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
# EXECUTIVE SUMMARY
# ==========================================

print_section("EXECUTIVE SUMMARY")

print_subsection("Campaign Overview")

print(f"Dataset Size         : {len(df):,}")
print(f"Campaigns           : {df['Campaign_Name'].nunique()}")
print(f"Campaign Types      : {df['Campaign_Type'].nunique()}")
print(f"Channels            : {df['Channel'].nunique()}")
print(f"Customer Segments   : {df['Customer_Segment'].nunique()}")
print(f"Regions             : {df['Region'].nunique()}")
print(f"Devices             : {df['Device'].nunique()}")
print(f"Date Range          : {df['Date'].min().date()} to {df['Date'].max().date()}")

# ==========================================
# Business KPIs
# ==========================================
print_subsection("Business KPIs")
total_spend = df["Spend"].sum()
average_ctr = df["CTR"].mean()
average_cpc = df["CPC"].mean()
total_clicks = df["Clicks"].sum()
total_impressions = df["Impressions"].sum()

print(f"Total Spend         : {total_spend:,.0f}")
print(f"Average CTR         : {average_ctr:.2f}%")
print(f"Average CPC         : {average_cpc:.2f}")
print(f"Total Clicks        : {total_clicks:,}")
print(f"Total Impressions   : {total_impressions:,}")

key_findings = """
• Festival campaigns receive the highest marketing investment.
• Email delivers the highest average CTR among all marketing channels.
• Loyal customers demonstrate stronger engagement than other customer segments.
• Mobile devices generate the majority of campaign clicks and impressions.
• Regional marketing performance remains balanced across all markets.
• Q4 records the highest marketing investment and campaign activity.
"""

print_key_findings(key_findings)

recommendations = """
• Continue prioritizing Festival campaigns to maximize marketing return on investment.
• Expand Email campaigns to capitalize on their superior click-through performance.
• Maintain a Mobile-first marketing strategy while optimizing Desktop campaigns for premium customer engagement.
• Strengthen retention initiatives targeting Loyal and Returning customers to improve long-term customer value.
• Continue balanced regional investment while monitoring performance trends for optimization opportunities.
• Increase marketing investment during Q4 to leverage stronger seasonal campaign performance.
"""

print_recommendations(recommendations)