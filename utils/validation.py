"""
Data Validation Utilities
-------------------------
Reusable data quality validation functions.

Version: 1.0
"""

import pandas as pd


def validate_shape(df):

    print("=" * 50)
    print("Dataset Shape")
    print("=" * 50)

    print(f"Rows    : {df.shape[0]:,}")
    print(f"Columns : {df.shape[1]}")


def validate_missing(df):

    print("=" * 50)
    print("Missing Values")
    print("=" * 50)

    print(df.isna().sum())


def validate_duplicates(df):

    print("=" * 50)
    print("Duplicate Records")
    print("=" * 50)

    print(df.duplicated().sum())


def validate_dtypes(df):

    print("=" * 50)
    print("Data Types")
    print("=" * 50)

    print(df.dtypes)


def validate_summary(df):

    print("=" * 50)
    print("Summary Statistics")
    print("=" * 50)

    print(df.describe().round(2))