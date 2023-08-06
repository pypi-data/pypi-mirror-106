more history.py
history ~3/1-100
history ~3/1-100 >> history.py
history ~4/1-100
more history.py
history ~3/1-1000 -f history0.py
more history0.py
chunks = pd.read_csv('onow_chatbot_timestamp_tangible.csv', chunksize=10000)
import pandas as pd
chunks = pd.read_csv('onow_chatbot_timestamp_tangible.csv', chunksize=10000)
profit_chunks = []
for chunk in tqdm(chunks):
    print(len(chunk))
    mask = (df.attribute.str.contains('prof') | df.attribute.str.contains('size'))
    profit_chunks.append(chunk.iloc[mask])
from tqdm import tqdm
profit_chunks = []
for chunk in tqdm(chunks):
    # print(len(chunk))
    mask = (df.attribute.str.contains('prof') | df.attribute.str.contains('size'))
    profit_chunks.append(chunk.iloc[mask])
profit_chunks = []
for chunk in tqdm(chunks):
    # print(len(chunk))
    mask = (chunk.attribute.str.contains('prof') | chunk.attribute.str.contains('size'))
    profit = chunk.iloc[mask].copy()
    profit['value'] = profit['value'].str.strip()
    profit['value'] = profit['value'].str.replace(' lakh', '00000')
    profit['value'] = profit['value'].str.replace('lakh', '00000')
    profit['value'] = profit['value'].str.split()[-1]
    profit['value'] = profit['value'].astype(float)
    profit_chunks.append(profit)
profit_chunks = []
for chunk in tqdm(chunks):
    # print(len(chunk))
    mask = (chunk.attribute.str.contains('prof') | chunk.attribute.str.contains('size'))
    profit = chunk[mask].copy()
    profit['value'] = profit['value'].str.strip()
    profit['value'] = profit['value'].str.replace(' lakh', '00000')
    profit['value'] = profit['value'].str.replace('lakh', '00000')
    profit['value'] = profit['value'].str.split()[-1]
    profit['value'] = profit['value'].astype(float)
    profit_chunks.append(profit)
profit_chunks = []
for chunk in tqdm(chunks):
    # print(len(chunk))
    mask = (chunk.attribute.str.contains('prof') | chunk.attribute.str.contains('size'))
    profit = chunk[mask].copy()
    profit['value'] = profit['value'].str.strip()
    profit['value'] = profit['value'].str.replace(' lakh', '00000')
    profit['value'] = profit['value'].str.replace('lakh', '00000')
    profit['value'] = profit['value'].str.split()
    profit['value'] = profit['value'].apply(lambda x: x[-1] if len(x) else x)
    profit['value'] = profit['value'].astype(float)
    profit_chunks.append(profit)
df = pd.concat(profit_chunks, axis=0)
len(df)
df.head()
df.sample(100)
df.to_csv('onow_chatbot_timestamp_tangible.profit_only.csv.gz', index=False, compression='gzip')
ls -hal
chunks = pd.read_csv('onow_chatbot_timestamp_tangible.csv', chunksize=10000)
profit_chunks = []
for chunk in tqdm(chunks):
    # print(len(chunk))
    mask = chunk.attribute.str.contains('prof')
    profit = chunk[mask].copy()
    profit['value'] = profit['value'].str.strip()
    profit['value'] = profit['value'].str.replace(' lakh', '00000')
    profit['value'] = profit['value'].str.replace('lakh', '00000')
    profit['value'] = profit['value'].str.split()
    profit['value'] = profit['value'].apply(lambda x: x[-1] if len(x) else x)
    profit['value'] = profit['value'].astype(float)
    profit_chunks.append(profit.copy())
df = pd.concat(profit_chunks, axis=0)
len(df)
profit_chunks = []
for chunk in tqdm(pd.read_csv('onow_chatbot_timestamp_tangible.csv', chunksize=10000, index_col='id')):
    # print(len(chunk))
    mask = chunk.attribute.str.contains('prof')
    profit = chunk[mask].copy()
    profit['value'] = profit['value'].str.strip()
    profit['value'] = profit['value'].str.replace(' lakh', '00000')
    profit['value'] = profit['value'].str.replace('lakh', '00000')
    profit['value'] = profit['value'].str.split()
    profit['value'] = profit['value'].apply(lambda x: x[-1] if len(x) else x)
    profit['value'] = profit['value'].astype(float)
    profit_chunks.append(profit.copy())
dfsmall = pd.read_csv('onow_chatbot_timestamp_tangible.100k.csv.gz')
len(dfsmall)
dfsmall.head()
ls -al
df.head()
df = df.set_index('id')
df.head()
df.describe()
df.describe(include='all')
df.to_csv('onow_chatbot_timestamp_tangible_profit_only.22874rows.csv.gz', compression='gzip')
ls -hal
git add onow_chatbot_timestamp_tangible_profit_only.22874rows.csv.gz
!git add onow_chatbot_timestamp_tangible_profit_only.22874rows.csv.gz
!git commit -am 'add filtered dataset for all rows that include "profit" in activity string'
git push
!git push
git status
