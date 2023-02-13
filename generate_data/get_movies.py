import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'

# Get popular movies from The Movie DB that use our providers
res = []
for page in range(1, 251):
    response_0 = requests.get(f'https://api.themoviedb.org/3/discover/movie?sort_by=vote_count.desc&api_key={api_key}&language={language}&page={page}')
    popular = response_0.json()
    for media in popular['results']:
        res.append({
            'id': media['id'],
            'overview': media['overview'],
            'genre_ids': media['genre_ids'],
            'poster_path': media['poster_path'],
            'media_type': 'movie',
            'title': media['title'],
            'original_title': media['original_title'],
            'release_date': media['release_date'],
            'provider_ids': [],
            'credits': []
        })
with open(f'./data/movies.json', 'w') as jsonf:
    json.dump(res, jsonf)