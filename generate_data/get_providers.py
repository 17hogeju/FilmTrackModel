import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file

# Gets the providers we need
response = requests.get(f'https://api.themoviedb.org/3/watch/providers/tv?api_key={api_key}&language=en-US')
providers = response.json()
providers = providers['results']
goal = {'Netflix', 'Amazon Prime Video', 'Disney Plus', 'HBO Max', 'Hulu'}
res = []
for p in providers:
    if p['provider_name'] in goal:
        res.append({
            'provider_name': p['provider_name'], 
            'provider_id': p['provider_id'],
            'logo_path': p['logo_path']
            })
with open('./data/providers.json', 'w') as f:
    json.dump(res, f)
    
our_providers = {8, 9, 15, 337, 384} # found via the above code with ids filtered that were not in media data