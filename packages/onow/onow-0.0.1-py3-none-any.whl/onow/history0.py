import pandas as pd
ls
df = pd.read_csv('onow_chatbot_timestamp_tangible.csv', nrows=100000)
df.to_csv('onow_chatbot_timestamp_tangible.100k.csv')
ls -hal
df.to_csv('onow_chatbot_timestamp_tangible.100k.csv.gz', compression='gzip')
dfsmall = pd.read_csv('onow_chatbot_timestamp_tangible.100k.csv.gz')
ls -hal
