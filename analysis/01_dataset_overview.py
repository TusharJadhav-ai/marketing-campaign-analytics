"""
Marketing Campaign Analytics
============================
Module : Business Intelligence & EDA
File   : 01_dataset_overview.py

Objective
---------
Validate the generated dataset and prepare it for
exploratory data analysis.
"""

# ==========================================
# Imports
# ==========================================

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from utils.validation import (
    validate_shape,
    validate_dtypes,
    validate_missing,
    validate_duplicates,
    validate_summary
)

from utils.wrangling import (
    enrich_date
)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(PROJECT_ROOT / "data" / "marketing_campaigns.csv")

# ==========================================
# Dataset Validation
# ==========================================

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

validate_shape(df)
validate_dtypes(df)
validate_missing(df)
validate_duplicates(df)
validate_summary(df)

# ==========================================
# Data Wrangling
# ==========================================

df = enrich_date(df, "Date")

# ==========================================
# Preview Dataset
# ==========================================

print("\nDataset Preview")
print("-" * 60)

print(df.head())

print("\nColumns")
print("-" * 60)

print(df.columns.tolist())