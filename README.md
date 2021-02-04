### Exchange rate forecasting with the Taylor rule
The uncovered interest rate parity condition tells us that $$\frac{1+i}{1+\tilde{i}} = \frac{\hat{E}_{t+1}}{E_t}.$$ Then the difference of the logarithm of the two countries's interest rates must also be the expected one-period ahead change in the logarithm of the exchange rate. 
$$log(1+i)-log(1+\tilde{i}) = log(\hat{E}_{t+1}) - log(E_t) \approx \%\Delta \hat{E}_{t+1}.$$


By using the Taylor Rule as an indicator of what a country's interest rate will be, we can generate forecasts of the 1 period ahead change in exchange rates. The Taylor Rule is
$$i_t^* = \pi_t + \phi(\pi_t-\pi^*) + \gamma(y_t-\bar{y}_t) + r^*,$$
where $i_t^*$ is the target short-term nominal interest rate, $\pi_t$ is the current inflation rate, $\pi^*$ is the target level of inflation, $y_t$ is the logarithm of real GDP, $\bar{y}_t$ is the logarithm of potential GDP, and $r^*$ is the equilibrium real interest rate.


Since we do not expect interest rates to adjust according to the Taylor Rule immediately, we include each country's lagged interest rate $i_{t-1}$ as a covariate to "smooth out" the model. Assuming that the two countries ahre the same inflation target and neutral interest rate, the model specification we obtain is
$$i_t-i_t^*=w+w_{u\pi}\pi_t-w_{f\pi}\tilde{\pi}_t+w_{uy}y_t-w_{fy}\tilde{y}_t+w_{ui}i_{t-1}-w_{fi}\tilde{i}_{t-1}+\eta_t,$$
where ~ indicates foreign variables.


We will try to use this specification to make one-month ahead forecasts of the CAD:USD and GBP:USD exchange rates. Rolling forecasts are initialized using 120 periods of monthly data starting January 1975 for Canada and March 1973 for the U.K.. At each step, a model is estimated using $OLS$ and the one-period ahead forecast is made. The first data point is then dropped, one data point is added at the end of the sample, and the process is repeated until the forecasts for June 2006 are made.


After we make our forecasts, we can compare whether the forecasts using Taylor Rule fundamentals perform better than a random walk model using two statistical tests: the Diebold-Mariano-West Test and the Clark-West Test.


The DMW test statistic is
$$DMW = \frac{\hat{\sigma}^2_{rw}-\hat{\sigma}^2_{l}}{\sqrt{\frac{1}{P}\hat{V}}} \sim N(0,1),$$
where $\hat{\sigma}^2_{rw}$ is the prediction $MSE$ for a random walk model, $\hat{\sigma}^2_{l}$ is the prediction $MSE$ for the linear model we are testing, $P$ is the number of predictions, and $$\hat{V}=\frac{1}{P}\sum^T_{t=T-P+1} ((s_{t+1}-s^{rw}_{t+1})^2-(s_{t+1}-s^{l}_{t+1})^2 - (\hat{\sigma}^2_{rw}-\hat{\sigma}^2_{l}))^2$$ where $s_{t+1}$ and $s^{l}_{t+1}$ are the forecasted values from the random walk and linear model, respectively.


The CW test statistic can be written as a function of the DMW test statistic, that is
$$CW = DMW + \frac{1}{\sqrt{\frac{1}{P}\hat{V}}}\frac{1}{P}\sum^T_{t=T-P+1}(X'_{t+1}\hat{\beta}_t)^2 \sim N(0, 1),$$
where $X'_{t+1}\hat{\beta}_t$ is the forecasted change in exchange rate.


Using the $DMW$ test, we fail to reject the null that the $MSPE$ from the Taylor rule model is lower than the $MSPE$ from a random walk model. Using the $CW$ test, we reject the null that $\beta=0$ in the linear model for both CAD:USD and GBP:USD exchange rates.


For the Canadian exchange rate, we reject the null at the $p=0.01$ level and for the U.K. exchange rate, we reject the null at the $p=0.05$ level. Therefore we conclude that in this setting, the Taylor rule model has more predictive power than a random walk model.

Since the $CW$ test statistic can be written as the sum of the $DMW$ test statistic plus a positive term, it is clear to see that the $CW$ test statistic will always be greater than the $DMW$ test statistic, giving it a different $p$-value for the same sample. For this reason, a lower $p$-value was obtained for the Clark-West test than the Diebold-Mariano-West test.

### References
* Tanya Molodtsova, David H. Papell, Out-of-sample exchange rate predictability with Taylor rule fundamentals, Journal of International Economics, Volume 77, Issue 2, 2009, Pages 167-180, ISSN 0022-1996, https://doi.org/10.1016/j.jinteco.2008.11.001.
