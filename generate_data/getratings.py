import json
import csv


tsvReader = csv.DictReader(open('./csv_data/title.ratings.tsv'), delimiter='\t')
# print(next(iter(tsvReader)))

ratingdict = {}
for d in tsvReader:
    ratingdict[d['tconst']] = d['numVotes']
    # break

# print(ratingdict['tt0241232'])

with open('./temp.json') as f:
    data = json.load(f)

res = {}
for title in data:
    tmp = data[title]
    tmp = [(x, ratingdict[x]) for x in tmp if x in ratingdict]
    tmp = sorted(tmp, key=lambda x: int(x[1]), reverse=True)
    res[title] = tmp
    # break
    # res[title] = sorted(tmp, key=lambda x: ratingdict[x], reverse=True)
    # print([ratingdict[x] for x in tmp])
    # print(sorted(tmp, key=lambda x: ratingdict[x], reverse=True))
    # break

with open('./sorted.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)
    

    # res[title] = sorted(data[title], key=lambda x: ratingdict[x])
    
