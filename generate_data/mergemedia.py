import json
from pathlib import Path

MEDIAPATH = '../data/media.json'

directory = '../data'
files = Path(directory).glob("*")


# title for all media
medialst = []
media_temp = {}
count = 0
for file in files:
    with open(file) as f:
        data = json.load(f)

    for title in data['titles']:
        if title in media_temp:
            media_temp[title]['platforms'].append(data["affiliate"])
        else:
            media_temp[title] = {
                "ttype": data['ttype'],
                "title": title,
                "platforms": [data["affiliate"]]
            }

# create id for all media
media = {}
count = 0
for key in media_temp:
    media[f'{count:07}'] = media_temp[key]
    count += 1

with open(MEDIAPATH, 'w', encoding='utf-8') as jsonf:
    json.dump(media, jsonf)


# TODO: Still need to remove duplicate year items like kindred on hulu that is a movie and tv show
# need to get the year of the title and maybe use the id from imdb
