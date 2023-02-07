import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'

res = []
genre_set = set()
movie_response = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language={language}')
movie_genres = movie_response.json()
tv_response = requests.get(f'https://api.themoviedb.org/3/genre/tv/list?api_key={api_key}&language={language}')
tv_genres = tv_response.json()

for m_genre in movie_genres['genres']:
    if m_genre['id'] not in genre_set:
        genre_set.add(m_genre['id'])
        res.append(m_genre)
for tv_genre in tv_genres['genres']:
    if tv_genre['id'] not in genre_set:
        genre_set.add(tv_genre['id'])
        res.append(tv_genre)


with open(f'./data/genres.json', 'w') as jsonf:
    json.dump(res, jsonf)