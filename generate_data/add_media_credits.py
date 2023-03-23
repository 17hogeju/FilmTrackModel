import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
import numpy as np

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'
data_file = 'data_3-19'


def filter_crew(item, goal):
    if item == goal:
        return True
    else:
        return False

with open(f'./{data_file}/media_full_genres.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)

for index, data in enumerate(split_data):
    for media_item in data:
        response = requests.get(f'https://api.themoviedb.org/3/{media_item["media_type"]}/{media_item["id"]}/credits?api_key={api_key}&language={language}')
        credits_json = response.json()
        cast = credits_json['cast']
        crew = credits_json['crew']
        credits = ""

        try:
            top_cast = map(lambda x: x['id'], cast[:5])
            top_directing = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Directing'), crew))
            top_production = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Production'), crew))
            top_writing = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Writing'), crew))
            
            credits += f'cast: {" ".join(str(x) for x in list(top_cast))}\n'
            credits += f'directors: {" ".join(str(x) for x in list(top_directing)[:3])}\n'
            credits += f'producers: {" ".join(str(x) for x in list(top_production)[:3])}\n'
            credits += f'writers: {" ".join(str(x) for x in list(top_writing)[:3])}'

            media_item['credits'] = credits

        except:
            print(f'exception for: {media_item}')
            break
    print(f'Completed Split: {index}')


with open(f'./{data_file}/media_full_genres_credits.json', 'w') as f:
    json.dump(temp_data, f)