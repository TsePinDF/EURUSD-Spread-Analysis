import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression import linear_model
df = pd.read_csv("assets/2023.12.17EURUSD(2)_TICK_UTCPlus02-TICK-No Session.csv")
#visualise the df
#print(df)
df['Index'] = df.index
#create new column with Ask - Bid
df['Spread'] = df['Ask'] - df['Bid']

#Plotting the scatter plot (& shrink marker size)
'''plt.scatter(df.iloc[:, -2], df.iloc[:, -1], label=df.columns[-1] + ' vs ' + df.columns[-2], s = 5)
plt.legend()
plt.show()'''

#datetime row is str formatted as yyyymmdd hh:mm:ss.sss
#create new column by classifying based on hour of day
#print(type(df.iloc[0,0]))
df['Hour'] = df['DateTime'].str[9:11]
# Plotting a boxplot
# boxinput splits the entire column into a list of 24 lists based on hour iteration
'''boxinput = [df['Spread'][df['Hour'] == hour] for hour in sorted(df['Hour'].unique())]
plt.boxplot(boxinput, labels=sorted(df['Hour'].unique()))
plt.xlabel('Hour')
plt.ylabel('Spread')
plt.title('Boxplot of Spread for each Hour')
plt.show()'''

#test new model

#Checking for autoregression factor at lag 1
df['SpreadLag1'] = df['Spread'].shift(1)
df = df.dropna()
'''
plt.scatter(df['SpreadLag1'], df['Spread'], label='Spread vs Spread at lag 1', s = 5)
plt.legend()
plt.show()'''

# Fit a linear regression model (Includes series of 1s for constant coef)
model = linear_model.OLS(df['Spread'], pd.concat([df['SpreadLag1'], pd.Series(1, index=df.index)], axis=1))
results = model.fit()

# Print regression summary
print(results.summary())
'''df = df.iloc[:100000,:]
#Perform Dicky-Fuller Test on stationarity
result = adfuller(df['Spread'])

# Extract and print the test statistics and p-value
test_statistic, p_value, _, _, _, _ = result
print(f'Test Statistic: {test_statistic}')
print(f'P-value: {p_value}')'''