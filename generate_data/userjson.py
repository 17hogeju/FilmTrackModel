import csv
import json


CSVPATH = './csv_data/users.csv'
JSONPATH = '../data/users.json'

users = {}
with open(CSVPATH, 'r', encoding="utf-8") as csvf:
    reader = csv.DictReader(csvf)
    
    for line in reader:
        uid = line.pop('UID')
        try:
            line['subscriptions'] = line['subscriptions'].split(',')
            line['subscriptions'] = [int(s) for s in line['subscriptions']]
        except:
            line['subscriptions'] = []
        
        try:
            line['watched'] = line['watched'].split(',')
            for i in range(len(line['watched'])):
                # print("hi")
                temp = {}
                tconst, rating = line['watched'][i].split(':')
                temp[tconst] = int(rating)
                line['watched'][i] = temp
        except:
            line['watched'] = []

        try:
            line['to_watch'] = line['to_watch'].split(',')
        except:
            line['to_watch'] = []

        try:
            line['dislikes'] = line['dislikes'].split(',')
        except:
            line['dislikes'] = []
        users[uid] = line

with open(JSONPATH, 'w', encoding="utf-8") as jsonf:
    json.dump(users, jsonf)

