import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
import numpy as np
from iteration_utilities import unique_everseen

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
data_file = 'data_3-19'

with open(f'./{data_file}/media_full.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)
all_genres = []
for index, data in enumerate(split_data):
    for media_item in data:
        response = requests.get(f'https://api.themoviedb.org/3/{media_item["media_type"]}/{media_item["id"]}?api_key={api_key}&language={language}')
        details_json = response.json()
        genres = details_json["genres"]

        genre_ids = []
        genre_names = []
        for g in genres:
            genre_ids.append(g["id"])
            genre_names.append(g["name"])
            all_genres.append(g)

        media_item["genre_ids"] = " ".join(str(x) for x in genre_ids)
        media_item["genres"] = ", ".join(genre_names)

    print(f'Completed Split: {index}')


g_res = list(unique_everseen(all_genres))
with open(f'./{data_file}/genres.json', 'w') as f:
    json.dump(g_res, f)

with open(f'./{data_file}/media_full_genres.json', 'w') as f:
    json.dump(temp_data, f)
