# Portfolio1_EURUSDSpreadAnalysis

Exploratory Data Analysis on Dukascopy EURUSD tick data

## Preliminary analysis

The goal of this portfolio is to analyse Bid-Ask price data in EURUSD. <br>
Trading in FX/CFD markets often incur costs, in the form of pure spread or spreads + commission.<br>
Commissions are often constant values but spreads are highly variable, which may significantly <br>
affect the testing speculative and investment models.<br><br>
Sample Data in repo retrieved from DukasCopy by QuantDataManager, 2023/11/15 - 2023/12/15, UTC + 2

Step 1: Visualise the naked dataset (line 19) <br><br>
!(https://github.com/TsePinDF/Portfolio1_EURUSDSpreadAnalysis/blob/main/First%20Plot.png)<br>
Fig 1. Screenshot of initial plot of Spread vs Index (ordered by time of price tick)
