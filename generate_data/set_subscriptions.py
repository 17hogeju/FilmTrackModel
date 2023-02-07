import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../film-track-05276ec63da6.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/subscriptions.json') as js:
    for sub in json.load(js):
        db.collection('subscriptions').document(f'{sub["id"]}').set(sub)

