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
Fig 1. iInitial plot of Spread vs Index (ordered by time of price tick)<br><br>
Primary observations:<br>
    1. There appears to be (slightly consistent) seasons of spikes in spreads
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
*modelling test results can be found under results.txt in assets*<br><br>
Summary: We have:<br>
Model 1: $\sum_{i=1}^{k}$ 	$\tau_{i} T_{i}$


<br>

## Additional Notes and Graphs <br><br>
![FigExtra1](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot4.png)<br>
Plot of differencing lags [Delta at t vs Delta at t-1]<br><br>
To do and update test for significance later

