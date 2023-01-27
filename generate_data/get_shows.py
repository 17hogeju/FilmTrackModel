import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'
our_providers = {8, 9, 15, 337, 384} # found via get_providers.py

# Get popular shows from The Movie DB that use our providers
res = []
for page in range(1,51):
    response_0 = requests.get(f'https://api.themoviedb.org/3/discover/tv?sort_by=vote_count.desc&api_key={api_key}&language={language}&page={page}')
    popular = response_0.json()
    for media in popular['results']:
        response_1 = requests.get(f'https://api.themoviedb.org/3/tv/{media["id"]}/watch/providers?api_key={api_key}')
        providers = response_1.json()
        try:
            providers_media = providers['results'][region]['flatrate']
            ids = {p['provider_id'] for p in providers_media}
            valid_providers = ids.intersection(our_providers)
            if valid_providers:
                res.append({
                    'id': media['id'],
                    'overview': media['overview'],
                    'genre_ids': media['genre_ids'],
                    'poster_path': media['poster_path'],
                    'provider_ids': list(valid_providers),
                    'name': media['name'], # tv only
                    'original_name': media['original_name'], # tv only
                    'first_air_date': media['first_air_date'] # tv only
                })
        except: 
            continue

with open(f'./data/shows.json', 'w') as jsonf:
    json.dump(res, jsonf)