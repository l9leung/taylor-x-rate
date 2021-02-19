import os
import sys
sys.path.insert(0, os.getcwd() + "\\data")
import time
import numpy as np
import pandas as pd
from get import get_fundamentals, get_xrate
from transform import cpi_to_inflation, output_gap, lag_rate
from forecast import rolling_forecasts
from tests import dmw_test


def main(targets):
    country = targets[0]
    print("Retrieving foreign data...")
    # Fetch data
    foreign = get_fundamentals(country)
    print("Retrieved foreign data")
    time.sleep(5)
    print("Retrieving domestic data...")
    domestic = get_fundamentals("US")
    print("Retrieved domestic data")
    xrate = get_xrate(country)

    print("Cleaning data...")
    # Transform exchange rate
    xrate.iloc[:, 0] = np.log(xrate.iloc[:, 0])
    xrate["change"] = xrate.iloc[:, 0].shift(-1) - xrate.iloc[:, 0]
    # Transform foreign data
    foreign[f"infl_{country}"] = cpi_to_inflation(foreign[f"infl_{country}"])
    foreign[f"y_{country}"] = output_gap(foreign[f"y_{country}"])
    foreign[f"i_{country}"] = lag_rate(foreign[f"i_{country}"])
    # Transform domestic data
    domestic["infl_US"] = cpi_to_inflation(domestic["infl_US"])
    domestic["y_US"] = output_gap(domestic["y_US"])
    domestic["i_US"] = lag_rate(domestic["i_US"])
    fundamentals = pd.concat([xrate.iloc[:, 1], foreign, domestic], axis=1)
    # fundamentals.to_csv(country + "_cleaned.csv")

    if "forecast" in targets:
        print("Forecasting...")
        # Make forecasts
        forecasts = rolling_forecasts(fundamentals.dropna())
        # Recover forecasted rate
        xrate["forecasted_change"] = forecasts
        xrate["forecasted_rate"] = xrate.iloc[:, 0] + xrate["forecasted_change"]
        xrate = xrate.dropna()

        print("Evaluating...")
        # Test forecasts
        DMW = dmw_test(xrate)
        print(DMW)


if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
