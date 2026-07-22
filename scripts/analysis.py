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
