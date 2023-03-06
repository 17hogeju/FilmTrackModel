import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
import numpy as np

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'

with open('./data/media_temp.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)

for index, data in enumerate(split_data):
    for media in data:
        response = requests.get(f'https://api.themoviedb.org/3/{media["media_type"]}/{media["id"]}/watch/providers?api_key={api_key}')
        providers = response.json()
        try:
            providers_media = providers['results'][region]['flatrate']
            ids = [p['provider_id'] for p in providers_media]
            media['provider_ids'] = ids
        except:
            continue
    print(f'Completed Split: {index}')

with open('./data/media_temp_2.json', 'w') as f:
    json.dump(temp_data, f)