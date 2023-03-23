import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../firebase_credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
data_file = 'data_3-19'

with open(f'./{data_file}/providers.json') as js:
    for provider in json.load(js):
        db.collection('providers').document(f'{provider["id"]}').set(provider)


