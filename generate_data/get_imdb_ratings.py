import json
import csv
# Creates the sorted json with titles organinzed by most popular

tsvReader = csv.DictReader(open('./csv_data/title.ratings.tsv'), delimiter='\t')

ratingdict = {}
for d in tsvReader:
    ratingdict[d['tconst']] = d['numVotes']

with open('./media_tconsts.json') as f:
    data = json.load(f)

res = {}
for title in data:
    tmp = data[title]
    tmp = [(x, ratingdict[x]) for x in tmp if x in ratingdict]
    tmp = sorted(tmp, key=lambda x: int(x[1]), reverse=True)
    res[title] = tmp

with open('./media_by_popularity.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)

    
