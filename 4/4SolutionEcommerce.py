import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')

#check the DataFrame
ecom.head()
#check ifo how many rows and columns?
ecom.info()

#Berapa rata2 harga jual?
print(ecom['Purchase Price'].mean())

#Berapa harga jual tertingi dan terendah?
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

#Berapa jumlah orang yang memakai bahasa inggris 
print(ecom[ecom['Language']=='en'].count())

#Berapa jumlah orang yang punya pekerjaan sebagai lwyer
print(ecom[ecom['Job'] == 'Lawyer'].info())

#Berapa jumah orang beli pada AM (sebelum tengah hari) atau PM ( setelah tengah hari)
print(ecom['AM or PM'].value_counts())

#Sebutkan 5 pekerjaan yang paling common
print(ecom['Job'].value_counts().head(5))

#Sesorang telah membeli lot: "90 WT" what was the purchase price for this transacation?
print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])

#cari email dengan nomor kredit card 4926535242672853
print(ecom[ecom["Credit Card"] == 4926535242672853]['Email'] )

#berapa orang yang memakai american express sebagai kartu kredit dan memelakukan pembelanjaan diatas 95 dollar?
print(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count())

#hard : berapa orang mempunyai kartu kredit yang expired tgl 25?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))

#hard  top 5 domain yang dipakai untuk email
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))

