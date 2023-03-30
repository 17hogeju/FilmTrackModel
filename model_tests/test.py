import requests
import json

url = 'https://filmtrack.loca.lt'

# local tunnel: lt --port 8000 --subdomain filmtrack --local-host "127.0.0.1" --print-requests


movie_indeces = [808, 245891, 49026, 913290, 607, 27205]
past_recs = []

data = {
    'media_type': 'movie',
    'data': movie_indeces, 
    'past_recs': past_recs
    }
jsond = json.dumps(data)

headers = {"Content-Length": str(len(jsond))}

try:
    response = requests.post(url, data=jsond, headers=headers)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
