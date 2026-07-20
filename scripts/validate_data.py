import pandas as pd

df = pd.read_csv("../data/marketing_campaigns.csv")

print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("COLUMN INFORMATION")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("FIRST 5 RECORDS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)
print(df.duplicated().sum())

print(df["Campaign_Name"].value_counts())
