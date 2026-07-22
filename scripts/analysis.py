# %%
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from utils.mr_tables import mr_crosstab
from generator.marketing_rules import CHANNEL_METRICS
from generator.config import CHANNELS
from generator.business_rules import CAMPAIGN_TYPES

from utils.validation import (
    validate_shape,
    validate_missing,
    validate_duplicates,
    validate_dtypes,
    validate_summary
)

from utils.wrangling import (
    convert_date,
    add_year,
    add_month,
    add_quarter,
    add_weekday
)



df = pd.read_csv("../data/marketing_campaigns.csv")

print("=" * 50)
print("Marketing Campaign Analytics")
print("=" * 50)
print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")
# %%
df.head()

# %%
df["Campaign_Name"].value_counts()

# %%
df["Channel"].value_counts()
# %%
pd.crosstab(df["Campaign_Name"], df["Channel"])
mr_crosstab(
    df,
    rows="Campaign_Name",
    cols="Channel"
)
# %%
df["Campaign_Name"].value_counts()
# %%

# %%
campaign_counts = df["Campaign_Name"].value_counts()

print(campaign_counts)

print("\nPercentage Distribution")
print((campaign_counts / len(df) * 100).round(2))
# %%
df["Channel"].value_counts()
# %%
print(df["Campaign_Type"].value_counts())
# %%
print(sys.path)
# %%


print(CHANNEL_METRICS)
# %%
print(CHANNEL_METRICS.keys())
# %%
print(CHANNEL_METRICS["Google Search"])
# %%
for channel, metrics in CHANNEL_METRICS.items():
    print(channel, metrics)
# %%

print(set(CHANNELS) == set(CHANNEL_METRICS.keys()))
# %%
print(CAMPAIGN_TYPES.values())
# %%
df[["Spend", "CTR", "CPC", "Clicks", "Impressions"]].describe().round(2)
# %%
summary = df[["Spend", "CTR", "CPC", "Clicks", "Impressions"]].describe()

summary.map(lambda x: f"{x:,.2f}")
# %%
len(df)
# %%
df.isna().sum()
# %%
df["Campaign_ID"].duplicated().sum()
# %%
df.info()
# %%
df["Spend"].describe()
# %%
df["CTR"].describe()
# %%
df["CPC"].describe()
# %%
df["Date"] = pd.to_datetime(df["Date"])
# %%
df["Year"] = df["Date"].dt.year
# %%
df.groupby("Campaign_Type")["Spend"].mean()
# %%
df.groupby("Channel")["CTR"].mean()
# %%
df.groupby("Channel")["CPC"].mean()
# %%
df.groupby("Channel")["Clicks"].mean()
# %%
validate_shape(df)

validate_missing(df)

validate_duplicates(df)

validate_dtypes(df)

validate_summary(df)
# %%
df = convert_date(df, "Date")
# %%
df = add_year(df, "Date")
# %%
df = add_month(df, "Date")
# %%
df = add_quarter(df, "Date")
# %%
df = add_weekday(df, "Date")
# %%
df.groupby("Month")["Spend"].sum()
# %%
df.groupby("Quarter")["CTR"].mean()
# %%
df.groupby("Weekday")["CPC"].mean()
# %%
df.groupby("Year").size()
# %%
