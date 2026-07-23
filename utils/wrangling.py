"""
Data Wrangling Utilities
------------------------
Reusable data preparation and transformation functions.

Version: 1.0
"""

import pandas as pd


def convert_date(df, column):

    df[column] = pd.to_datetime(df[column])

    return df


def add_year(df, column):

    df["Year"] = df[column].dt.year

    return df


def add_month(df, column):

    df["Month"] = df[column].dt.month_name()

    return df


def add_quarter(df, column):

    df["Quarter"] = df[column].dt.quarter

    return df


def add_weekday(df, column):

    df["Weekday"] = df[column].dt.day_name()

    return df

def enrich_date(df, column):

    df = convert_date(df, column)
    df = add_year(df, column)
    df = add_month(df, column)
    df = add_quarter(df, column)
    df = add_weekday(df, column)

    return df