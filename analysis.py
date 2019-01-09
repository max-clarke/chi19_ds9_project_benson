import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('data/May18_turnstiledata.csv')
df
df.columns = [column.strip() for column in df.columns]
df.columns

df = df.drop(['Unnamed: 0'], axis=1)

grouped = df.groupby(['C/A', 'UNIT', 'SCP', 'STATION','DATE','TIME'], as_index=False)
grouped['DATETIME'] = pd.to_datetime(df['DATE']+" "+df['TIME'])
df['EXITS'] = df['EXITS'].diff()
df['ENTRIES'] = df['ENTRIES'].diff()

df['CONC'] = df['STATION'] + df['SCP'] + df['C/A']
len(df['CONC'].unique())
df['CONC2'] = df['SCP'] + df['C/A']
len(df['CONC2'].unique())
len(df.groupby(['STATION','CONC2','DATE','TIME']).sum())
df_diff = df.groupby(['CONC2','DATE','TIME']).sum()
df_diff = df_diff[df_diff['ENTRIES'] > -1]
df_diff = df_diff[df_diff['ENTRIES'] < 100000]
df_diff = df_diff[df_diff['EXITS'] > -1]
df_diff = df_diff[df_diff['EXITS'] < 100000]

df_diff
