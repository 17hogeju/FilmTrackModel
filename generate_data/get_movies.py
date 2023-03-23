import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
data_file = 'data_3-19'

# Get popular movies from The Movie DB that use our providers
res = []
for page in range(1, 251):
    response_0 = requests.get(f'https://api.themoviedb.org/3/discover/movie?sort_by=vote_count.desc&api_key={api_key}&language={language}&page={page}')
    popular = response_0.json()
    for media in popular['results']:
        res.append({
            'credits': "",
            'genres': "",
            'genre_ids': media['genre_ids'],
            'id': media['id'],
            'media_type': 'movie',
            'original_title': media['original_title'],
            'overview': media['overview'],
            'poster_path': media['poster_path'],
            'provider_ids': "",
            'release_date': media['release_date'],
            'title': media['title'],
            'title_lowercase': media['title'].lower()
        })
with open(f'./{data_file}/movies.json', 'w') as jsonf:
    json.dump(res, jsonf)