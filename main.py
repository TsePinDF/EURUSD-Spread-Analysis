import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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