import numpy as np
from scipy.stats import norm


def dmw_test(forecasts):
    """Perform the Diebold-Mariano-West and Clark-West tests on a DataFrame
    containing the forecasted exchange rate in the 1 index column and actual
    exchange rate in the 0 index column. Return the p-values."""

    forecasts["rw"] = forecasts.iloc[:, 0]
    forecasts = forecasts.dropna()
    error_rw = forecasts.iloc[:, 0].shift(-1) - forecasts["rw"]
    MSPE_rw = np.mean(error_rw**2)
    error_l = forecasts.iloc[:, 0].shift(-1) - forecasts["forecasted_rate"]
    MSPE_l = np.mean(error_l**2)

    P = len(forecasts)
    V_hat = np.mean((error_rw**2 - error_l**2 - (MSPE_rw-MSPE_l)**2)**2)
    # Test statistic
    DMW = (MSPE_rw - MSPE_l)/(np.sqrt(V_hat/P))
    # p value
    p_DMW = norm.sf(DMW)

    CW = DMW + 1/(np.sqrt(V_hat/P)) * np.mean(forecasts.iloc[:, 2]**2)
    p_CW = norm.sf(CW)

    # return DMW, CW
    return f"p={p_DMW} p={p_CW}"
