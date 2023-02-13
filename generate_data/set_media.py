import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np

cred = credentials.Certificate('../firebase_credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/media.json') as js:
    temp_data = json.load(js)

split_data = np.array_split(temp_data, 100)

for index, data in enumerate(split_data):
    for media in data:
        db.collection('media').document(f'{media["id"]}').set(media)
    print(f'Completed Split: {index}')