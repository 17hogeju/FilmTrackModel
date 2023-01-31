
# "job": "Director"
# "department": "Writing"

# anything with "cast_id"  sort by popularity


import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )
import json

api_key = config.tmdb_api_key # get TMDB API key from config.py file
language = 'en-US'
region = 'US'

def get_id_data(id, search_item, crew_lst):
    res = []
    for dict_item in crew_lst:
        if dict_item[id] == search_item:
            res.append(dict_item)
        if len(res) == 5:
            break
    return res
    

def try_del(d, key):
    try:
        del d[key]
    except:
        pass

with open('./data/media.json') as jsf:
    media_data = json.load(jsf)
    id_set = set()
    res = []
    for media_item in media_data:
        response = requests.get(f'https://api.themoviedb.org/3/{media_item["media_type"]}/{media_item["id"]}/credits?api_key={api_key}&language={language}')
        credits = response.json()
        top_cast = credits['cast'][:5]
        media_item['top_cast'] = [x['id'] for x in top_cast]

        for person in top_cast:
            if not person['id'] in id_set:
                id_set.add(person['id'])
                try_del(person, 'cast_id')
                try_del(person, 'character')
                try_del(person, 'credit_id')
                try_del(person, 'order')
                res.append(person)

        if media_item["media_type"] == 'movie':
            directors = get_id_data('job', 'Director', credits['crew'])
            media_item['directors'] = [x['id'] for x in directors]

            writers = get_id_data('department', 'Writing', credits['crew'])
            media_item['writers'] = [x['id'] for x in writers]

            for person in directors:
                if not person['id'] in id_set:
                    id_set.add(person['id'])
                    try_del(person, 'credit_id')
                    try_del(person, 'department')
                    try_del(person, 'job')
                    res.append(person)
            for person in writers:
                if not person['id'] in id_set:
                    id_set.add(person['id'])
                    try_del(person, 'credit_id')
                    try_del(person, 'department')
                    try_del(person, 'job')
                    res.append(person)
        else:
            producers = get_id_data('job', 'Producer', credits['crew'])
            media_item['producers'] = [x['id'] for x in producers]

            exec_producers = get_id_data('job', 'Executive Producer', credits['crew'])
            media_item['exec_producers'] = [x['id'] for x in exec_producers]

            for person in producers:
                if not person['id'] in id_set:
                    id_set.add(person['id'])
                    try_del(person, 'credit_id')
                    try_del(person, 'department')
                    try_del(person, 'job')
                    res.append(person)
            for person in exec_producers:
                if not person['id'] in id_set:
                    id_set.add(person['id'])
                    try_del(person, 'credit_id')
                    try_del(person, 'department')
                    try_del(person, 'job')
                    res.append(person)


with open('./data/people.json', 'w') as jsf:
    json.dump(res, jsf)
with open('./data/media_new.json', 'w') as jsf:
    json.dump(media_data, jsf)
