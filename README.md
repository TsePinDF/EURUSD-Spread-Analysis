# Portfolio1_EURUSDSpreadAnalysis

Exploratory Data Analysis on Dukascopy EURUSD tick data

## Preliminary analysis

The goal of this portfolio is to analyse Bid-Ask price data in EURUSD. <br>
Trading in FX/CFD markets often incur costs, in the form of pure spread or spreads + commission.<br>
Commissions are often constant values but spreads are highly variable, which may significantly <br>
affect the testing of trading or investment models.<br><br>
Sample Data in repo retrieved from DukasCopy by QuantDataManager, 2023/11/15 - 2023/12/15, UTC + 2

Step 1: Visualise the naked dataset <br><br>
![Fig 1.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot1.png)<br>
Fig 1. iInitial plot of Spread vs Index (ordered by time of price tick)<br><br>
Primary observations:<br>
    1. There appears to be (slightly consistent) seasons of spikes in spreads
    2. Outside of the spikes, spreads sppear to vary around a relatively consistent range
<br><br>
That being said, we need to validate these observations.<br>
We know that trading sessions exist, and that liquidity may be time-dependent, so we could first try to classify the datasets based on the hour of day. <br><br>
Step 2: Box plot of spread range vs Hour-Of-Day <br><br>
![Fig 2.](https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/assets/Plot2.png)
<br>
Fig 2. Box Plot of Spread Ranges vs Hour-Of-Day<br><br>
Already, we could see a potential pattern when we use Hours as a classification factor.<br>
For the most preliminary model, we could build a simple classification model with 1 factor and 24 levels.