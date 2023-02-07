import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'

res = []
# Gets the providers we need
response = requests.get(f'https://api.themoviedb.org/3/watch/providers/tv?api_key={api_key}&language={language}')
providers = response.json()
for provider in providers['results']:
    res.append({
        'provider_name': provider['provider_name'],
        'provider_id': provider['provider_id'],
        'logo_path': provider['logo_path']
    })

with open('./data/providers_2.json', 'w') as f:
    json.dump(res, f)