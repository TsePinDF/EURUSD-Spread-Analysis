import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression import linear_model
from scipy.stats import f
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

#Checking for autoregression factor at lag 1
df['SpreadLag1'] = df['Spread'].shift(1)
df['SpreadDelta1'] = df['Spread'] - df['Spread'].shift(1)
df['SpreadDelta2'] = df['Spread'].shift(1) - df['Spread'].shift(2)
df = df.dropna()
'''
plt.scatter(df['SpreadLag1'], df['Spread'], label='Spread vs Spread at lag 1', s = 5)
plt.legend()
plt.show()
'''

'''
plt.scatter(df['SpreadDelta2'], df['SpreadDelta1'], label='Spread Increment vs Lag 1 Increment', s = 5)
plt.legend()
plt.show()
'''


# Model1 (naive), simply take the intercept
# Design matrix with solely intercept estimates the mean of dependent var using sample
design1 = pd.DataFrame({'Intercept':pd.Series(1, index=df.index)})
model1 = linear_model.OLS(df['Spread'], design1['Intercept'])
results = model1.fit() 
# Get the residuals
residuals = results.resid
# Calculate SSE (Sum of Squared Errors)
sse1 = (residuals**2).sum()
print("SSE: ", sse1)
# SSE:  0.002084023259183432
print(results.summary())

# Model 2: basic classification model, with categorical dummy variables
# Dummy encoding of k-1 levels
design2 = pd.get_dummies(df['Hour'], prefix = 'category').astype(int)
design2 = design2.iloc[:,1:]
# Intercept represents hour 0
design2['Intercept'] = pd.Series(1, index=df.index)
model2 = linear_model.OLS(df['Spread'], design2[list(design2.columns)])
results = model2.fit() 
# Get the residuals
residuals = results.resid
# Calculate SSE (Sum of Squared Errors)
sse2 = (residuals**2).sum()
print("SSE: ", sse2)
# SSE:  0.0012556210936629866, 
print(results.summary())
'''
# Perform Dicky-Fuller Test on stationarity, insufficient memory so i'll sample the first 200,000 points
dfslice = df.iloc[:200000,:]
result = adfuller(dfslice['Spread'])

# Extract and print the test statistics and p-value
test_statistic, p_value, _, _, _, _ = result
print(f'Test Statistic: {test_statistic}')
print(f'P-value: {p_value}')
# H0: unit root exists in dataset
# Test Statistic: -11.861966493646301
# P-value: 6.8133511303628465e-22'''

# Model 3: Fitting an AR(1) model (Includes series of 1s for constant coef)
design3 = pd.DataFrame({'Intercept':pd.Series(1, index=df.index),'SpreadLag1':df['SpreadLag1']})
model3 = linear_model.OLS(df['Spread'], design3[list(design3.columns)])
results = model3.fit()
# Get the residuals
residuals = results.resid
# Calculate SSE (Sum of Squared Errors)
sse3 = (residuals**2).sum()
print("SSE: ", sse3)
# SSE:  0.0003617617705678061
print(results.summary())

# Model 4: GLM based on AR1 model and Categorical factors
design4 = design2
design4['SpreadLag1'] = df['SpreadLag1']
print(design4)
model4 = linear_model.OLS(df['Spread'], design4[list(design4.columns)])
results = model4.fit()
# Get the residuals
residuals = results.resid
# Calculate SSE (Sum of Squared Errors)
sse4 = (residuals**2).sum()
print("SSE: ", sse4)
# SSE:  0.0003617617705678061
print(results.summary())

# Performing F test on SSEXT from treatment effects
# aka single-factor ANCOVA testing Full Model 4 vs Reduced Model 3
# Degrees of freedom for the numerator and denominator
dfn = design4.shape[1] - design3.shape[1]  # Difference in the number of parameters
dfd = design4.shape[0] - design4.shape[1]  # Total number of observations - number of parameters in Model 4

# F-test statistic and p-value
f_statistic = ((sse3 - sse4) / dfn) / (sse4 / dfd)
p_value = f.sf(f_statistic, dfn, dfd)

# Print results
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")
# F-statistic: 3247.15106405486
# P-value: 0.0
# Reject H0 that treatments are ineffective, aka Hour-Of-Day is significant

