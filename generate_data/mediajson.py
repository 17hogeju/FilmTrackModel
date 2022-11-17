import csv
import json

DATAPATH = './csv_data/data.tsv'
MEDIAPATH = '../data/media.json'


media = {}
with open(DATAPATH, 'r', encoding="utf-8") as tsvf:
    tsvReader = csv.DictReader(tsvf, delimiter='\t')

    for row in tsvReader:
        temp = {}
        if not (row['titleType'] == 'movie' or row['titleType'] == 'tvseries' or row['titleType'] == 'tvepisode'):
            continue
        temp['titleType'] = row['titleType']
        temp['primaryTitle'] = row['primaryTitle']
        temp['originalTitle'] = row['originalTitle']
        try:
            temp['isAdult'] = bool(int(row['isAdult']))
        except:
            pass
        try:
            temp['startYear'] = int(row['startYear'])
        except:
            pass  
        try:
            temp['endYear'] = int(row['endYear'])
        except:
            pass
        try:
            temp['runtimeMinutes'] = int(row['runtimeMinutes'])
        except:
            pass
        try:
            temp['genres'] = row['genres'].split(',')
        except:
            pass
        media[row['tconst']] = temp

with open(MEDIAPATH, 'w', encoding="utf-8") as jsonf:
    json.dump(media, jsonf)
