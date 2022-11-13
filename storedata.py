import pandas as pd

DATAPATH = './data/title.basics.tsv'
PICKLENAME = './data/cached_titles.pkl'

df = pd.read_csv(DATAPATH, sep='\t', header=0, dtype=str)
df.to_pickle(PICKLENAME)
