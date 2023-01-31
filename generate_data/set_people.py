import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../film-track-05276ec63da6.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

with open('./data/people.json') as js:
    data = json.load(js)
print('data loaded')

for person in data[:1000]:
    db.collection('people').document(f'{person["id"]}').set(person)
print('done')
for person in data[1000:2000]:
    db.collection('people').document(f'{person["id"]}').set(person)
print('done')
for person in data[2000:3000]:
    db.collection('people').document(f'{person["id"]}').set(person)
print('done')
for person in data[3000:4000]:
    db.collection('people').document(f'{person["id"]}').set(person)
print('done')
for person in data[4000:]:
    db.collection('people').document(f'{person["id"]}').set(person)
print('done')

# test = list(range(25))
# print(test[:5])
# print(test[5:10])
# print(test[10:15])
# print(test[15:20])
# print(test[20:])
