import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json
import numpy as np

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'


def filter_crew(item, goal):
    if item == goal:
        return True
    else:
        return False

with open('./data/media.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)

for index, data in enumerate(split_data):
    for media_item in data:
        response = requests.get(f'https://api.themoviedb.org/3/{media_item["media_type"]}/{media_item["id"]}/credits?api_key={api_key}&language={language}')
        credits = response.json()
        cast = credits['cast']
        crew = credits['crew']

        top_cast = map(lambda x: x['id'], cast[:5])
        top_directing = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Directing'), crew))
        top_production = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Production'), crew))
        top_writing = map(lambda x: x['id'], filter(lambda x: filter_crew(x['department'], 'Writing'), crew))
        
        media_item['top_cast'] = list(top_cast)[:5]
        media_item['top_directing'] = list(top_directing)[:3]
        media_item['top_production'] = list(top_production)[:3]
        media_item['top_writing'] = list(top_writing)[:3]
    print(f'Completed Split: {index}')

with open('./data/media_temp.json', 'w') as f:
    json.dump(temp_data, f)