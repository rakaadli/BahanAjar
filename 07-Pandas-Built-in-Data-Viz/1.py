import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

print(df1)
print(df2)

# plt.show(df1['A'].hist())

# plt.style.use('ggplot')

# plt.style.use('fivethirtyeight')
# df1['A'].hist()

#For Showing Remove then #
# plt.show(df1['A'].hist())
# For Showing

# # Plot Types

# There are several plot types built-in to pandas, most of them statistical plots by nature:

# * df.plot.area
# * df.plot.barh
# * df.plot.density
# * df.plot.hist
# * df.plot.line
# * df.plot.scatter
# * df.plot.bar
# * df.plot.box
# * df.plot.hexbin
# * df.plot.kde
# * df.plot.pie

# You can also just call df.plot(kind='hist') or replace that kind argument with any of the key terms shown in the list above (e.g. 'box','barh', etc..)
# ___

'''
Area
'''

# plt.show(df2.plot.area(alpha=0.4))

'''
Barplots

'''
# plt.show(df2.plot.bar())
# plt.show(df2.plot.bar(stacked=True))

'''
Histograms
'''

# plt.show(df1['A'].plot.hist(bins=50))

'''
Line Plots
'''

# plt.show(df1.plot.line(x=df1.index, y='B', figsize=(12, 3), lw=1))

'''
Scatter Plots
'''

# plt.show(df1.plot.scatter(x='A', y='B')
# plt.show(df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm'))
