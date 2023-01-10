import csv
import json
from collections import defaultdict
# creates media_tconsts.json with all imdb tconsts for each title in media

DATAPATH = './csv_data/title.basics.tsv'
media = {}
with open(DATAPATH, 'r', encoding="utf-8") as tsvf:
    tsvReader = csv.DictReader(tsvf, delimiter='\t')

    with open('../data/media.json') as f:
        data = json.load(f)

    mylist = [x['title'].lower() for x in list(data.values())]
    
    res = defaultdict(lambda: [])
    for row in tsvReader:
        if row['titleType'] == 'movie' or row['titleType'] == 'tvSeries' or row['titleType'] == 'tvMiniSeries':
            if row['primaryTitle'].lower() in mylist:
                res[row['primaryTitle'].lower()].append(row['tconst'])

    with open('./media_tconsts.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)
