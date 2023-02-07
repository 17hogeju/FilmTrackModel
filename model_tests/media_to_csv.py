import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('../generate_data/data/media.json') as json_file:
    data = json.load(json_file)
    
# now we will open a file for writing
data_file = open('media_test.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file, quotechar='"', quoting=csv.QUOTE_ALL)

csv_writer.writerow(['id', 'overview', 'genre_ids', 'poster_path', 'provider_ids', 'media_type', 'title', 'original_title', 'release_date', 'top_cast', 'credits'])
 
for media_item in data:
    media_item["id"] = str(media_item["id"])
    media_item["overview"] = media_item["overview"].replace('"', "'")
    media_item["genre_ids"] = ' '.join(str(i) for i in media_item["genre_ids"])
    media_item["provider_ids"] = ' '.join(str(i) for i in media_item["provider_ids"])
    media_item["top_cast"] = ' '.join(str(i) for i in media_item["top_cast"])
    
    directors = ' '.join(str(i) for i in media_item["directors"])
    writers = ' '.join(str(i) for i in media_item["writers"])
    producers = ' '.join(str(i) for i in media_item["producers"])
    exec_producers = ' '.join(str(i) for i in media_item["exec_producers"])
    credits = [directors, writers, producers, exec_producers]
    media_item["credits"] = ' '.join(i for i in credits if i)
    del media_item["directors"]
    del media_item["writers"]
    del media_item["producers"]
    del media_item["exec_producers"]
    csv_writer.writerow(media_item.values())
 
data_file.close()

