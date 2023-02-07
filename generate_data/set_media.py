import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../firebase_credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/media.json') as js:
    for media in json.load(js):
        db.collection('media').document(f'{media["id"]}').set(media)