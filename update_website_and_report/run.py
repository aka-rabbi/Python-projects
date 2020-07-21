#!/usr/bin/env python3
import os
import json
import requests
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
fruit_description_path = 'supplier-data/descriptions/' #enter your desired folder here
files = os.listdir(fruit_description_path)
def check_extension(files):
    images = []
    for name in files:
        if os.path.splitext(name)[1] =='.txt':
            images.append(name)
    return images
txt_files = check_extension(files)
print(txt_files)
url = 'http://35.188.56.35/fruits/'
for f in txt_files:
    fruits_dict = {}
    with open(fruit_description_path+f) as fruit_description:
        fruit_info = list(iter(fruit_description))
        fruit_description = ' '.join([l.strip() for l in fruit_info[2:]])  #.encode('utf-8').strip()
        fruits_dict['name'] = fruit_info[0]
        fruits_dict['weight'] = int(fruit_info[1].split()[0])
        fruits_dict['description'] = fruit_description
        fruits_dict['image_name'] = os.path.splitext(f)[0]+'.jpeg'
        #fruits_json = json.dumps(fruits_dict)

        response = requests.post(url, fruits_dict)  #json doesn't work it seems
        print(response.ok,response.status_code)