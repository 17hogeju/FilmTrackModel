import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../film-track-05276ec63da6.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/media.json') as js:
    for media in json.load(js):
        db.collection('media').document(f'{media["id"]}').set(media)