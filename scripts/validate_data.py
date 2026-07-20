import pandas as pd

df = pd.read_csv("../data/marketing_campaigns.csv")

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\nData Types")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())