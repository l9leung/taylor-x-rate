import pandas as pd
from statsmodels.formula.api import ols


def rolling_forecasts(fundamentals):
    """Return rolling forecasts, each fitted using 120 periods of data. Fits
    each model by regressing the 0 index column on all other columns."""

    forecasts = pd.Series(index=fundamentals.index, dtype="float64",
                          name="change_forecast")
    formula = fundamentals.columns[0] + "~" + "+".join(fundamentals.columns[1:].to_list())

    for t in range(120, len(fundamentals)):
        # Fit symmetric Taylor Rule model with smoothing, heterogenous
        # coefficients, constant term
        mod = ols(formula, data=fundamentals[t-120:t])
        res = mod.fit()

        # One-step ahead forecast
        forecasts[t] = res.predict(fundamentals[t:t+1])

    return forecasts
