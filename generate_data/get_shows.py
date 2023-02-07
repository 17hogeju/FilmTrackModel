import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'

# Get popular shows from The Movie DB that use our providers
res = []
for page in range(1,251):
    response_0 = requests.get(f'https://api.themoviedb.org/3/discover/tv?sort_by=vote_count.desc&api_key={api_key}&language={language}&page={page}')
    popular = response_0.json()
    for media in popular['results']:
        first_air_date = "Not Listed"
        try:
            first_air_date = media['first_air_date']
        except: 
            pass
        res.append({
            'id': media['id'],
            'overview': media['overview'],
            'genre_ids': media['genre_ids'],
            'poster_path': media['poster_path'],
            'media_type': 'tv',
            'title': media['name'],
            'original_title': media['original_name'],
            'release_date': first_air_date,
            'provider_ids': [],
            'top_cast': [],
            'top_directing': [],
            'top_production': [],
            'top_writing': []
        })

with open(f'./data/shows.json', 'w') as jsonf:
    json.dump(res, jsonf)