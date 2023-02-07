import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../film-track-05276ec63da6.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/genres.json') as js:
    for genre in json.load(js):
        db.collection('genres').document(f'{genre["id"]}').set(genre)