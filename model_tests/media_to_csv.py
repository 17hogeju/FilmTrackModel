import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('../generate_data/data/media.json') as json_file:
    data = json.load(json_file)
    
# now we will open a file for writing
data_file = open('media_test.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file, quoting=csv.QUOTE_NONE, delimiter='|',escapechar='\\')

csv_writer.writerow(['id', 'overview', 'genre_ids', 'media_type', 'title', 'credits'])
 
for media_item in data:
    temp_row = []
    temp_row.append(media_item["id"])
    temp_row.append(media_item["overview"])
    temp_row.append(' '.join(str(i) for i in media_item["genre_ids"]))
    temp_row.append(media_item['media_type'])
    temp_row.append(media_item['title'])
    temp_row.append(' '.join(str(i) for i in media_item["credits"]))
    csv_writer.writerow(temp_row)
 
data_file.close()