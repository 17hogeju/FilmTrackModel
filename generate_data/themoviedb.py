import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'
media_type = 'movie' # can be tv or movie, adjust res variables as needed


# # Gets the providers we need
# response = requests.get(f'https://api.themoviedb.org/3/watch/providers/tv?api_key={api_key}&language=en-US')
# providers = response.json()
# providers = providers['results']
# goal = {'Netflix', 'Amazon Prime Video', 'Disney Plus', 'HBO Max', 'Hulu'}
# res = []
# for p in providers:
#     if p['provider_name'] in goal:
#         res.append({
#             'provider_name': p['provider_name'], 
#             'provider_id': p['provider_id'],
#             'logo_path': p['logo_path']
#             })
# with open('./providers.json', 'w') as f:
#     json.dump(res, f)
our_providers = {8, 9, 15, 337, 384} # found via the above code


# # Get new media based on media_type: tv or movie
# res = []
# for page in range(1,51):
#     response = requests.get(f'https://api.themoviedb.org/3/discover/{media_type}?sort_by=vote_count.desc&api_key={api_key}&language={language}&page={page}')
#     pop = response.json()
#     for media in pop['results']:
#         res.append({
#             'id': media['id'],
#             'overview': media['overview'],
#             'genre_ids': media['genre_ids'],
#             'poster_path': media['poster_path'],
#             # 'title': media['title'], # movie only
#             # 'original_title': media['original_title'], # movie only
#             # 'release_date': media['release_date'], # movie only
#             # 'adult': media['adult'] # movie only
#             'name': media['name'], # tv only
#             'original_name': media['original_name'], # tv only
#             'first_air_date': media['first_air_date'] # tv only
        
#         })
# with open(f'./base_{media_type}.json', 'w') as f:
#     json.dump(res,f)


# # Gets the valid providers for the given media collection
# res = []
# with open(f'./base_{media_type}.json') as jsonf:
#     for media in json.load(jsonf):
#         response = requests.get(f'https://api.themoviedb.org/3/{media_type}/{media["id"]}/watch/providers?api_key={api_key}')
#         providers = response.json()
#         try:
#             providers_media = providers['results'][region]['flatrate']
#             # print(providers_film)
#             ids = {p['provider_id'] for p in providers_media}
#             valid_providers = ids.intersection(our_providers)
#             if valid_providers:
#                 res.append({
#                     'id': media['id'],
#                     'overview': media['overview'],
#                     'genre_ids': media['genre_ids'],
#                     'poster_path': media['poster_path'],
#                     'provider_ids': list(valid_providers),
#                     'title': media['title'], # movie only
#                     'original_title': media['original_title'], # movie only
#                     'release_date': media['release_date'], # movie only
#                     'adult': media['adult'] # movie only
#                     # 'name': media['name'], # tv only
#                     # 'original_name': media['original_name'], # tv only
#                     # 'first_air_date': media['first_air_date'] # tv only
#                 })
#         except: 
#             continue

# with open(f'./new_{media_type}.json', 'w') as jsonf:
#     json.dump(res, jsonf)


# Combine intermediate data
res = []
with open('./new_tv.json') as tv:
    for tv_d in json.load(tv):
        res.append(tv_d)

with open('./new_movie.json') as movie:
    for movie_d in json.load(movie):
        res.append(movie_d)

with open('./new_media.json', 'w') as jsf:
    json.dump(res, jsf)
