"""
Marketing Campaign Data Generator
---------------------------------
Generates a synthetic marketing campaign dataset.
Version: 1.0
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from marketing_rules import CHANNEL_METRICS

from business_rules import (
    CAMPAIGN_TYPES,
    CHANNEL_WEIGHTS,
    DEVICE_WEIGHTS,
    CUSTOMER_SEGMENT_WEIGHTS,
)

from marketing_rules import (
    CHANNEL_METRICS,
    CAMPAIGN_BUDGET_RANGES,
)


def get_channel(campaign):

    channel_weights = CHANNEL_WEIGHTS[campaign]

    return random.choices(
        population=list(channel_weights.keys()),
        weights=list(channel_weights.values()),
        k=1
    )[0]

def get_device(channel):

    device_weights = DEVICE_WEIGHTS[channel]

    return random.choices(
        population=list(device_weights.keys()),
        weights=list(device_weights.values()),
        k=1
    )[0]

def get_customer_segment(channel):

    segment_weights = CUSTOMER_SEGMENT_WEIGHTS[channel]

    return random.choices(
        population=list(segment_weights.keys()),
        weights=list(segment_weights.values()),
        k=1
    )[0]

def get_marketing_metrics(channel):

    metrics = CHANNEL_METRICS[channel]

    ctr = round(
        random.uniform(*metrics["CTR"]),
        2
    )

    cpc = round(
        random.uniform(*metrics["CPC"]),
        2
    )

    return ctr, cpc

def get_campaign_budget(campaign_type):

    budget_range = CAMPAIGN_BUDGET_RANGES[campaign_type]

    return random.randint(
        budget_range[0],
        budget_range[1]
    )

def get_marketing_metrics(channel):

    metrics = CHANNEL_METRICS[channel]

    ctr = round(
        random.uniform(*metrics["CTR"]),
        2
    )

    cpc = round(
        random.uniform(*metrics["CPC"]),
        2
    )

    return ctr, cpc

def get_clicks(spend, cpc):

    return int(spend / cpc)

def get_clicks(spend, cpc):

    return round(spend / cpc)

def get_impressions(clicks, ctr):

    return round(clicks / (ctr / 100))

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
    campaign_name = random.choice(CAMPAIGNS)

    campaign_type = CAMPAIGN_TYPES[campaign_name]

    channel = get_channel(campaign_name)

    device = get_device(channel)

    customer_segment = get_customer_segment(channel)

    spend = get_campaign_budget(campaign_type)

    region = random.choice(REGIONS)

    ctr, cpc = get_marketing_metrics(channel)

    clicks = get_clicks(spend, cpc)

    impressions = get_impressions(clicks, ctr)
    
    record = {
    "Campaign_ID": i + 1,
    "Date": start_date + timedelta(days=random.randint(0, date_range)),
    "Campaign_Name": campaign_name,
    "Campaign_Type": campaign_type,
    "Channel": channel,
    "Region": random.choice(REGIONS),
    "Device": device,
    "Customer_Segment": customer_segment,
    "Spend": spend,
    "CTR": ctr,
    "CPC": cpc,
    "Clicks": clicks,
    "Impressions": impressions
    }

    records.append(record)

df = pd.DataFrame(records)

df = df.sort_values("Date")

import os

print(os.getcwd())

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
df.head()