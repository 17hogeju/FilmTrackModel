import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../firebase_credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/providers.json') as js:
    for provider in json.load(js):
        db.collection('providers').document(f'{provider["provider_id"]}').set(provider)


