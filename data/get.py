import requests
import pandas as pd


def get_fundamentals(country):
    """Return a pandas DataFrame with fundamentals data from the IMF."""

    fundamentals = pd.DataFrame()

    # Get fundamentals from IMF
    url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/"
    indicators = {"PCPI_IX": "infl", "AIP_SA_IX": "y", "FIMM_PA": "i"}
    for indicator in indicators.items():
        key = f"CompactData/IFS/M.{country}.{indicator[0]}"
        r = requests.get(url + key)
        r = r.json()["CompactData"]["DataSet"]["Series"]
        fundamentals[indicator[1]+"_"+country] = pd.Series(data=[obs["@OBS_VALUE"] for obs in r["Obs"]],
                                                           index=[obs["@TIME_PERIOD"] for obs in r["Obs"]],
                                                           dtype="float64")
    fundamentals.index = pd.DatetimeIndex(fundamentals.index, freq="MS")

    return fundamentals


def get_xrate(country):
    """Return a pandas DataFrame with monthly exchange rate data from FRED."""
    if country == "CA":
        xrate = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=EXCAUS&scale=left&cosd=1971-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2021-02-18&revision_date=2021-02-05&nd=1971-01-01"

        xrate = pd.read_csv(xrate, names=["CADUSD"], index_col=0, skiprows=1)
        xrate = 1/xrate

    elif country == "GB":
        xrate = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=EXUSUK&scale=left&cosd=1971-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2021-02-18&revision_date=2021-02-18&nd=1971-01-01"

        xrate = pd.read_csv(xrate, names=["GBPUSD"], index_col=0, skiprows=1)

    xrate.index = pd.DatetimeIndex(xrate.index, freq="MS")

    return xrate
