### Exchange rate forecasting with the Taylor rule

![Alt text](https://raw.githubusercontent.com/l9leung/taylor-x-rate/main/forecasts.png?token=ARCDHBWLBGX75OH6PB26Y33ADN43I)

The uncovered interest rate parity condition tells us that $$\frac{1+i}{1+\tilde{i}} = \frac{\hat{E}_{t+1}}{E_t}.$$ Then the difference of the logarithm of the two countries's interest rates must also be the expected one-period ahead change in the logarithm of the exchange rate. 
$$log(1+i)-log(1+\tilde{i}) = log(\hat{E}_{t+1}) - log(E_t) \approx \%\Delta \hat{E}_{t+1}.$$


By using the Taylor Rule as an indicator of what a country's interest rate will be, we can generate forecasts of the 1 period ahead change in exchange rates. The Taylor Rule is
$$i_t^* = \pi_t + \phi(\pi_t-\pi^*) + \gamma(y_t-\bar{y}_t) + r^*,$$
where $i_t^*$ is the target short-term nominal interest rate, $\pi_t$ is the current inflation rate, $\pi^*$ is the target level of inflation, $y_t$ is the logarithm of real GDP, $\bar{y}_t$ is the logarithm of potential GDP, and $r^*$ is the equilibrium real interest rate.


Since we do not expect interest rates to adjust according to the Taylor Rule immediately, we include each country's lagged interest rate $i_{t-1}$ as a covariate to "smooth out" the model. Assuming that the two countries ahre the same inflation target and neutral interest rate, the model specification we obtain is
$$i_t-i_t^*=w+w_{u\pi}\pi_t-w_{f\pi}\tilde{\pi}_t+w_{uy}y_t-w_{fy}\tilde{y}_t+w_{ui}i_{t-1}-w_{fi}\tilde{i}_{t-1}+\eta_t,$$
where ~ indicates foreign variables.


We will try to use this specification to make one-month ahead forecasts of the CAD:USD and GBP:USD exchange rates. Rolling forecasts are initialized using 120 periods of monthly data starting January 1975 for Canada and March 1973 for the U.K.. At each step, a model is estimated using $OLS$ and the one-period ahead forecast is made. The first data point is then dropped, one data point is added at the end of the sample, and the process is repeated until the forecasts for June 2006 are made.

### References
* Tanya Molodtsova, David H. Papell, Out-of-sample exchange rate predictability with Taylor rule fundamentals, Journal of International Economics, Volume 77, Issue 2, 2009, Pages 167-180, ISSN 0022-1996, https://doi.org/10.1016/j.jinteco.2008.11.001.
