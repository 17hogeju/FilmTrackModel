import json

with open('../data/media.json') as f:
    media = json.load(f)

res = []
for id in media:
    temp = {}
    temp = media[id]
    temp['tconst'] = id
    res.append(temp)

with open('../data/media.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)