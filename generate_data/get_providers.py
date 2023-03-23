import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
from iteration_utilities import unique_everseen

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
data_file = 'data_3-19'

res_set = set()
res = []
with open(f'./{data_file}/media_full_genres_credits_providers.json') as js:
    temp_data = json.load(js)

tv_response = requests.get(f'https://api.themoviedb.org/3/watch/providers/tv?api_key={api_key}&language={language}')
movie_response = requests.get(f'https://api.themoviedb.org/3/watch/providers/movie?api_key={api_key}&language={language}')

tv_json = tv_response.json()
movie_json = movie_response.json()
myDict = {}
for show in tv_json["results"]:
    myDict[show["provider_id"]] = {"name": show["provider_name"], "id": show["provider_id"], "logo_path": show["logo_path"]}

for movie in movie_json["results"]:
    myDict[show["provider_id"]] = {"name": show["provider_name"], "id": show["provider_id"], "logo_path": show["logo_path"]}

# print(myDict)
for media in temp_data:
    temp = media["provider_ids"].split()
    for x in temp:
        res_set.add(int(x))
    # res.add()

# print(res_set)
for item in res_set:
    res.append(myDict[item])

# print(res)
with open(f'./{data_file}/providers.json', 'w') as f:
    json.dump(res, f)