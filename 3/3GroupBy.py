import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

#liat object
print(df.groupby('Company'))

#save object menjadi variable
by_comp = df.groupby("Company")

#lalu panggil aggregate method ke object
print(by_comp.mean())
print(df.groupby('Company').mean())

#more example aggregate methods
print(by_comp.std())
print(by_comp.min())
print(by_comp.max())
print(by_comp.count())
print(by_comp.describe())
print(by_comp.describe().transpose())
print(by_comp.describe().transpose()['GOOG'])