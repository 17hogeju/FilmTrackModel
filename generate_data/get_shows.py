import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
data_file = 'data_3-19'

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
            'credits': "",
            'genres': "",
            'genre_ids': media['genre_ids'],
            'id': media['id'],
            'media_type': 'tv',
            'original_title': media['original_name'],
            'overview': media['overview'],
            'poster_path': media['poster_path'],
            'provider_ids': "",
            'release_date': first_air_date,
            'title': media['name'],
            'title_lowercase': media['name'].lower()
        })


# print(res)
with open(f'./{data_file}/shows.json', 'w') as jsonf:
    json.dump(res, jsonf)