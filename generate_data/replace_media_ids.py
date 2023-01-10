import json
# puts imdb number for id for media


with open('../data/media.json') as f:
    media = json.load(f)

with open('./media_by_popularity.json') as f:
    sortedj = json.load(f)

res = {}
for key in media:
    if not key[0] == 't':
        try:
            newkey = sortedj[media[key]['title'].lower()][0][0]
            res[newkey] = media[key]
        except:
            print(media[key]['title'])

with open('../data/media.json', 'w', encoding="utf-8") as jsonf:
        json.dump(res, jsonf)
