import csv
import json


CSVPATH = './csv_data/subscriptions.csv'
JSONPATH = '../data/subscriptions.json'

subscriptions = {}
with open(CSVPATH, 'r', encoding="utf-8") as csvf:
    reader = csv.DictReader(csvf)
    
    for line in reader:
        id = line.pop('subID')
        line['plan_price'] = int(line['plan_price'])
        subscriptions[id] = line

with open(JSONPATH, 'w', encoding="utf-8") as jsonf:
    json.dump(subscriptions, jsonf)
