import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
# %matplotlib inline

df = pd.read_csv('911.csv')

df.info()


df.head(3)

df['zip'].value_counts().head(5)
