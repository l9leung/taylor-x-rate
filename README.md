## Exchange rate forecasting with the Taylor rule
Replication of some of the results from Molodtsova and Papell (2009) and implentation of their methodology to current data. Read a summary [here](https://github.com/l9leung/taylor-x-rate/blob/main/report/report.pdf).

![Alt text](https://raw.githubusercontent.com/l9leung/taylor-x-rate/main/report/forecasts1.png)

## Organization
* `forecast.py`: functions to construct the rolling forecasts
* `tests.py`: functions to statistically test the performance of forecasts
* `replicate.ipynb`: Jupyter Notebook illustrating some of Molodtsova and Papell's results on CAD:USD and GBP:USD exchange rates using the data from their website

#### Data
The `/data` folder contains:
* `get.py`: functions to retrieve exchange rate and macroeconomic data from FRED and the IMF's International Financial Statistics database, respectively
* `transform.py`: functions to transform the data for modeling
* `Taylor rule fundamentals data.xls`: the original data from Molodtsova and Papell (2009) downloaded from the [author's website](https://uh.edu/~dpapell/Taylor%20rule%20fundamentals%20data.xls)
* `Taylor rule fundamentals data.doc`: data description of the above data downloaded from the [author's website](https://uh.edu/~dpapell/Taylor%20rule%20fundamentals%20data.doc)

## References
* Tanya Molodtsova, David H. Papell, Out-of-sample exchange rate predictability with Taylor rule fundamentals, Journal of International Economics, Volume 77, Issue 2, 2009, Pages 167-180, ISSN 0022-1996, https://doi.org/10.1016/j.jinteco.2008.11.001.
