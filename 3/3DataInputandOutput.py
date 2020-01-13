import numpy as np
import pandas as pd

'''
CSV

'''
#CSV Input
df = pd.read_csv('example')
print(df)
#CSV Output
df.to_csv('example',index=False)

'''
Excel
'''
print('--Excel--')
#Excel Input
pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
print(df)
#Excel output
df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

'''
HTML

kita butuh install htmllib4,lxml, dan beautifoup4. Di terminal commandprompt. Jalankan: 
    conda install lxml
    conda install html5lib
    conda install BeautifulSoup4
Lalu restart Jupyter notebook
(atau gunakan pip install jika kamu tidak sedang menggunakan anaconda)

pandas dapat membaca read table di html. For example:
'''

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df)
print(df[0])

'''
SQL (Optional)
'''
print('--SQL--')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
#df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)