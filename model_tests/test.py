import requests
import json

url = 'https://shan.loca.lt'


movie_indeces = [245891, 109445, 62177, 3170, 808]
past_recs = []

data = {
    "media_type": "movie",
    "data": movie_indeces, 
    "past_recs": past_recs
    }
jsond = json.dumps(data)

headers = {"Content-Length": str(len(jsond))}

try:
    response = requests.post(url, data=jsond, headers=headers)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
