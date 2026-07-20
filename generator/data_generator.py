"""
Marketing Campaign Data Generator
---------------------------------
Generates a synthetic marketing campaign dataset.
Version: 1.0
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from config import (
    NUM_RECORDS,
    START_DATE,
    END_DATE,
    CAMPAIGNS,
    CHANNELS,
    REGIONS,
    DEVICES,
    CUSTOMER_SEGMENTS,
    RANDOM_SEED
)

# Set random seed
random.seed(RANDOM_SEED)

start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
end_date = datetime.strptime(END_DATE, "%Y-%m-%d")

date_range = (end_date - start_date).days

records = []

for i in range(NUM_RECORDS):

    record = {
        "Campaign_ID": i + 1,
        "Date": start_date + timedelta(days=random.randint(0, date_range)),
        "Campaign_Name": random.choice(CAMPAIGNS),
        "Channel": random.choice(CHANNELS),
        "Region": random.choice(REGIONS),
        "Device": random.choice(DEVICES),
        "Customer_Segment": random.choice(CUSTOMER_SEGMENTS)
    }

    records.append(record)

df = pd.DataFrame(records)

df = df.sort_values("Date")

df.to_csv("data/marketing_campaigns.csv", index=False)    

print("=" * 50)
print("Dataset generated successfully!")
print("=" * 50)

print(f"Total Records : {len(df):,}")
print(f"Columns       : {len(df.columns)}")
print(f"Output File   : data/marketing_campaigns.csv")

print(df.shape)
import pandas as pd

df = pd.read_csv("data/marketing_campaigns.csv")

print(df.shape)
print(df.info())