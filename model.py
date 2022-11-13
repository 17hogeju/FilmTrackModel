import pandas as pd
import time

DATAPATH = './data/cached_titles.pkl'

df = pd.read_pickle(DATAPATH)
column_labels = df.columns
print(column_labels)
