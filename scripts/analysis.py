# %%
import pandas as pd

df = pd.read_csv("../data/marketing_campaigns.csv")

# %%
df.head()

# %%
df["Campaign_Name"].value_counts()

# %%
df["Channel"].value_counts()
# %%

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
