import json

with open('./csv_data/media.json') as f:
        data = json.load(f)

data = data['media']

# print(data[next(iter(data))])
for key in data:
    data[key] = data[key]['primaryTitle']

# print(data[next(iter(data))])
# print(list(data.values()).index('Let the Right One In'))




with open('../data/media.json') as f:
    media = json.load(f)

count = -1
for key in media:
    indeces = [i for i, x in enumerate(data.values()) if x == media[key]['title']]
    print(media[key]['title'])
    print(indeces)
    break
    # if len(indeces)  1:
    #     print('hi')

    
        # if temp[0] in media:
        #     media[f'{count}'] = media[temp[0]]
        #     media[temp[0]] = 


        # else:
        #     media[temp[0]] =
