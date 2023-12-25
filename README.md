# Portfolio1_EURUSDSpreadAnalysis

Exploratory Analysis and Modelling on Dukascopy EURUSD tick data

## Preliminary analysis

The goal of this portfolio is to analyse Bid-Ask price data in EURUSD. <br>
Trading in FX/CFD markets often incur costs, in the form of pure spread or spreads + commission.<br>
Commissions are often constant values but spreads are highly variable, which may significantly <br>
affect the testing of trading or investment models.<br><br>
Sample Data in repo retrieved from DukasCopy by QuantDataManager, 2023/11/15 - 2023/12/15, UTC + 2

### Step 1: Visualise the naked dataset <br><br>
![Fig 1.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot1.png)<br>
Fig 1. Initial plot of Spread vs Index (ordered by time of price tick)<br><br>
Primary observations:<br>
    1. There appears to be (slightly consistent) seasons of spikes in spreads<br>
    2. Outside of the spikes, spreads sppear to vary around a relatively consistent range
<br><br>
That being said, we need to validate these observations.<br>

### Step 2: Box plot of spread range vs Hour-Of-Day <br><br>
We know that trading sessions exist, and that liquidity may be time-dependent, so we could first try to classify the datasets based on the hour of day. <br><br>
![Fig 2.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot2.png)
<br>
Fig 2. Box Plot of Spread Ranges vs Hour-Of-Day<br><br>
Already, we could see a potential pattern when we use Hours as a classification factor.<br>
Large spreads tend to appear consistently at midnight, as well as certain windows of the day.<br>

### Step 3: Scatter plot of Spread vs t-1 Spread <br><br>
Preliminary analysis (Fig 1) of the dataset also suggests some form of autoregressive behaviour (low spreads precede low spreads, high spreads precede high spreads). We could test that first by plotting the spread against the its t-1 value<br><br>
![Fig 3.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot3.png)
<br>
Fig 3. Scatter Plot of Spread vs t-1 Spread<br>
Visually, we could see another potential linear relationship between the the spread and its lagged value. This should provide sufficient information to build a few basic models<br>

## Model building <br> <br>
This project will primarily focuses on simplistic models using the features available, so below are the current approaches we will be comparing:<br>
model 1: naive model<br>
model 2: hour-classification model<br>
model 3: SLR AR1 model<br>
model 4: GLM with AR1 + hour classification<br><br>
*modelling test results can be found under results.txt in assets*<br>
<br><br>
Summary: estimating spread (y) at ith time index, we have:<br>
Model 1: $$y_{i} = \overline{y} + \epsilon_{i}$$ ,<br>
Model 2: $$y_{i} = \sum_{i=1}^{23} \tau_{i} T_{i} + \epsilon_{i}$$, for dummy variables $T_{i}$, and treament coefficients $\tau_{i}$<br>
Model 3: $$y_{i} = B y_{i-1} + \epsilon_{i}$$
Model 4: $$y_{i} = \sum_{i=1}^{23} \tau_{i} T_{i} + B y_{i-1} + \epsilon_{i}$$<br><br>
Performance for models:<br>
Model 1: <br>
$SSE = SST = 0.002084023259183432$ <br>
Model 2:<br>
$SSE = 0.0012556210936629866$ <br>
$Adj R^{2} = 0.397$ <br>
Model 3:<br>
$SSE = 0.0003617617705678061$ <br>
$Adj R^{2} = 0.826$ <br>
Model 4:<br>
$SSE = 0.0003504725457872613$ <br>
$Adj R^{2} = 0.832$ <br>
<br>
## Additional tests<br>
We should perform a test for stationarity before any modelling. As the dataset is too large for my local machine, I performed an Adjusted Dicky-Fuller test on the first 200,000 data points. We are testing for null hypothesis that a unit root exists in the sample. <br>
$Test Statistic: -11.861966...$
$p-value: 6.813351...e^{-22}$<br><br>
With this, we can reject $H_{0}$ and assume that the dataset is stationary.<br><br>
When comparing models, we should also validate the significance of additional factors versus the previous model. This should allow us to minimise needless complexity through factors that may be strongly correlated or insignificant factors. Since Model 3 (AR1) is a reduced form of Model 4(AR1 + Hour factor), we will perform a test comparing the Mean Extra Sum-Of-Squares (MSEXT) against the MSE of the full model. The ratio produces an F-statistic, and hence we will use an F distribution.<br><br>
Formula: $$\frac{MSEXT}{MSE_{model 4}} = \frac{SSEXT / (k - 1)}{SSE_{model 4} / (n - p - k)} \sim {\sf F}(k-1, n-p-k)$$ , k = no. of levels, p = no. of regressors, n = sample size <br>
$Test Statistic: 3247.15106405486$
$p-value: 0. 00000...$<br><br>
With this, we can reject $H_{0}$ and assume that the treatment effects are significant, hence model 4 will be preferred over model 3.<br><br>
## Limitations <br>
Although the adjusted r^2 values are good, the results show some issues that should be addressed in future adjustments. Primarily, the dataset does not appear to follow a normal distribution, which violates a key assumption for any estimations regarding variances (check skew and kurtosis in results.txt). When we perform a normality plot (QQ-plot), the curvature of both ends show significantly fat tails on the distribution, congruent with the high levels of kurtosis observed. 
<br><br>
![Fig 4.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot5.png)
<br>
Fig 4: Normality qq plot of model 4<br>
##
Future renditions should adjust or account for the non-normaltiy of the datset. One method could be to seek additional key factors that could cause extreme events. For instance, it may make sense to incorporate a news release classification variable, in the form of binary outcomes (news releasing vs no news) or a multi-level factor (news impact). Another method would be to perform transformations to the dataset to address the kurtosis, such as Box-Cox, logarithmic or square root transformations. However, this may impact the way we interpret the model so it should only be considered as a last resort.<br>

<br>

## Additional Notes and Graphs <br><br>
![FigExtra1](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot4.png)<br>
Plot of differencing lags [Delta at t vs Delta at t-1]<br><br>
Additional plot of Differencing factor applied to dataset 

