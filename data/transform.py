import numpy as np
import pandas as pd
from statsmodels.formula.api import ols


def cpi_to_inflation(series):
    """Convert a monthly pandas series of CPI to yearly inflation."""

    inflation = np.log(series/series.shift(12))

    return inflation


def output_gap(series):
    """Estimate the output gap using a linear time trend."""

    formula = series.name + " ~ time_index"
    series = pd.DataFrame(series).dropna()
    series["time_index"] = [t for t in range(len(series))]
    potential = pd.Series(index=series.index, dtype="float64")

    for t in series.index:
        # Regress output on time index using all available data before t
        lin_trend = ols(formula, data=series[:t]).fit()

        # Estimate potential using fitted values
        potential[t] = lin_trend.predict()[-1]

    gap = np.log(series.iloc[:, 0]/potential)

    return gap


def lag_rate(series):
    """Retrieve lagged interest rates for smoothing."""

    lagged = series.shift(-1)

    return lagged
