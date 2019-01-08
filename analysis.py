import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import qgrid

df = pd.read_csv('data/May18_turnstiledata.csv')
df
df.columns

df.rename(columns = {'EXITS                                                               ': 'EXITS'},inplace=True)
df.columns
del df['Unnamed: 0']

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
