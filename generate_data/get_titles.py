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

res = []
with open(f'./{data_file}/media_full.json') as js:
    temp_data = json.load(js)

for media in temp_data:
    res.append(media['title_lowercase'])

# print(res)
with open(f'./{data_file}/titles.json', 'w') as f:
    json.dump(res, f)