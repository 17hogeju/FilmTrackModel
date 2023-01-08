import json

with open('../data/media.json') as f:
    data = json.load(f)

for item in data:
    seen = set(data[item]['platforms'])
    if len(seen) != len(data[item]['platforms']):
        print(data[item])
