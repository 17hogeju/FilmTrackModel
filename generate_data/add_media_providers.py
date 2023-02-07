import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'

with open('./data/media.json') as js:
    data = json.load(js)

for media in data:
    response = requests.get(f'https://api.themoviedb.org/3/movie/{media["id"]}/watch/providers?api_key={api_key}')
    providers = response.json()
    try:
        providers_media = providers['results'][region]['flatrate']
        ids = [p['provider_id'] for p in providers_media]
        media['provider_ids'] = ids
    except:
        continue

with open('./data/media_temp.json', 'w') as f:
    json.dump(data, f)