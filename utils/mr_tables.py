import pandas as pd


def mr_crosstab(df, rows, cols):

    counts = pd.crosstab(df[rows], df[cols])

    row_pct = (
        pd.crosstab(
            df[rows],
            df[cols],
            normalize="index"
        ) * 100
    ).round(1)

    result = counts.astype(str) + " (" + row_pct.astype(str) + "%)"

    return result