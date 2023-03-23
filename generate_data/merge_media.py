import json

data_file = 'data_3-19'

res = []
with open(f'./{data_file}/movies.json') as movies:
    for movie in json.load(movies):
        res.append(movie)

with open(f'./{data_file}/shows.json') as shows:
    for show in json.load(shows):
        res.append(show)

with open(f'./{data_file}/media_full.json', 'w') as json_file:
    json.dump(res, json_file)