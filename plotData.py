import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as np
import seaborn as sns

df = pd.read_csv("s&p_data\\plot_data.csv", names=['Company', 'Complexity', 'Performance'])
df = df.replace(to_replace='None', value=np.nan).dropna()
df = df.replace(to_replace='inf', value=np.nan).dropna()
df["Performance"] = pd.to_numeric(df["Performance"])
print(df)

# Create a scatter plot of complexity vs performance
sns.scatterplot(data=df, x="Complexity", y="Performance", hue="Company", legend=False)

# Add appropriate labels to each axis
pyplot.xlabel("Complexity Rating of 10-K")
pyplot.ylabel("Performance 1990-2021")

# Show the plot
pyplot.show()

