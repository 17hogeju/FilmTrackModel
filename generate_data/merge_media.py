import json

res = []
with open('./data/movies.json') as movies:
    for movie in json.load(movies):
        res.append(movie)

with open('./data/shows.json') as shows:
    for show in json.load(shows):
        res.append(show)

with open('./data/media.json', 'w') as json_file:
    json.dump(res, json_file)