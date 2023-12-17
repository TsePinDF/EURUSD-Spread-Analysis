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
plt.scatter(df.iloc[:, -2], df.iloc[:, -1], label=df.columns[-1] + ' vs ' + df.columns[-2], s = 5)

#Adding a legend
plt.legend()

#Display the plot (Takes a while to load)
plt.show()