import csv
import json
from collections import defaultdict

DATAPATH = './csv_data/title.basics.tsv'


media = {}
with open(DATAPATH, 'r', encoding="utf-8") as tsvf:
    tsvReader = csv.DictReader(tsvf, delimiter='\t')

    with open('../data/media.json') as f:
        data = json.load(f)

    mylist = [x['title'] for x in list(data.values())]
    
    res = defaultdict(lambda: [])
    for row in tsvReader:
        if row['titleType'] == 'movie' or row['titleType'] == 'tvseries':
            if row['primaryTitle'] in mylist:
                res[row['primaryTitle']].append(row['tconst'])

    with open('./temp.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)


    # temp = {}
    # if not (row['titleType'] == 'movie' or row['titleType'] == 'tvseries' or row['titleType'] == 'tvepisode'):
    #     continue
    # temp['titleType'] = row['titleType']
    # temp['primaryTitle'] = row['primaryTitle']
    # temp['originalTitle'] = row['originalTitle']
    # try:
    #     temp['isAdult'] = bool(int(row['isAdult']))
    # except:
    #     pass
    # try:
    #     temp['startYear'] = int(row['startYear'])
    # except:
    #     pass  
    # try:
    #     temp['endYear'] = int(row['endYear'])
    # except:
    #     pass
    # try:
    #     temp['runtimeMinutes'] = int(row['runtimeMinutes'])
    # except:
    #     pass
    # try:
    #     temp['genres'] = row['genres'].split(',')
    # except:
    #     pass
    # media[row['tconst']] = temp

# with open(MEDIAPATH, 'w', encoding="utf-8") as jsonf:
# json.dump(media, jsonf)
