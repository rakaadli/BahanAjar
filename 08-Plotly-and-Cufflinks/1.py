import pandas as pd
import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import matplotlib.pyplot as plt
# For offline use
cf.go_offline()

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())

print(df.head())

df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

print(df.head())


# Scatter
print('--scatter--')
df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10)
# cf.show()
df.show()
