import json
import csv

# First, get imdb title data

# with open('../data/media.json') as f:
#     media = json.load(f)

# DATAPATH = './csv_data/title.basics.tsv'
# res = {}
# with open(DATAPATH, 'r', encoding="utf-8") as tsvf:
#     tsvReader = csv.DictReader(tsvf, delimiter='\t')

#     for row in tsvReader:
#         temp_tconst = row['tconst']
#         if temp_tconst in media:
#             del row['tconst']
#             del row['isAdult']
#             row['genres'] = row['genres'].split(',')
#             res[temp_tconst] = row
    
#     with open('./more_media.json', 'w', encoding="utf-8") as jsonf:
#         json.dump(res, jsonf)


# Next, get imdb principles data

with open('./more_media.json') as f:
    media = json.load(f)

DATAPATH = './csv_data/title.crew.tsv'
with open(DATAPATH, 'r', encoding="utf-8") as tsvf:
    tsvReader = csv.DictReader(tsvf, delimiter='\t')

    for row in tsvReader:
        temp_tconst = row['tconst']
        if temp_tconst in media:
            # print(row)
            # break
            media[temp_tconst]['directors'] = row['directors'].split(',')
            media[temp_tconst]['writers'] = row['writers'].split(',')
    
    with open('./more_media.json', 'w', encoding="utf-8") as jsonf:
        json.dump(media, jsonf)





    



    


     

