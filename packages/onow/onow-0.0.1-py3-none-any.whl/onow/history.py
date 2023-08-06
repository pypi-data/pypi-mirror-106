df = pd.read_csv('onow_chatbot_timestamp_tangible.100k.csv.gz')
import pandas as pd
df = pd.read_csv('onow_chatbot_timestamp_tangible.100k.csv.gz')
df.head()
df.attribute.str.contains('prof')
df.attribute.str.contains('prof').sum()
mask = df.attribute.str.contains('prof')
df = df[mask]
df.head()
df.id.unique()
len(df.id.unique())
len(df)
df.head()
df.value.unique()
df.value.str.replace(' lakh', '00000')
df['value'] = df.value.str.replace(' lakh', '00000')
df
value = [s.split()[-1] for s in df.value]
value
df['value'] = history
df['value'] = value
df.head()
df['value'] = df['value'].astype(float)
pd.to_datetime(df.timestamp)
pd.to_datetime(df.timestamp).month
pd.to_datetime(df.timestamp).mo
pd.to_datetime(df.timestamp).dt.month
pd.to_datetime(df.timestamp)[0]
pd.to_datetime(df.timestamp).loc[0]
pd.to_datetime(df.timestamp).iloc[0]
x = _
x.quarter
history -o
history -o -p >> history.md
history >> history.py
