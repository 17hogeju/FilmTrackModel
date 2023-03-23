import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
import numpy as np

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'
data_file = 'data_3-19'

with open(f'./{data_file}/media_full_genres_credits.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)

for index, data in enumerate(split_data):
    for media in data:
        response = requests.get(f'https://api.themoviedb.org/3/{media["media_type"]}/{media["id"]}/watch/providers?api_key={api_key}')
        providers = response.json()
        try:
            providers_media = providers['results'][region]['flatrate']
            media['provider_ids'] = " ".join(str(x['provider_id']) for x in providers_media)
            media['provider_names'] = ", ".join(x['provider_name'] for x in providers_media)
        except:
            continue
        # print(media)
        # break

    print(f'Completed Split: {index}')
    # break

with open(f'./{data_file}/media_full_genres_credits_providers.json', 'w') as f:
    json.dump(temp_data, f)