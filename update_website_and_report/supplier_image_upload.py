#!/usr/bin/env python3
import os
import json
import requests

image_path = 'supplier-data/images/' #enter your desired folder here
files = os.listdir(image_path)
def check_extension(files):
    images = []
    for name in files:
        if os.path.splitext(name)[1] =='.jpeg':
            images.append(name)
    return images
images = check_extension(files)

url = 'http://localhost/upload/'
for f in images:
    #img_dict = {}
    with open(image_path+f,'rb') as img:
        #print(image_path+f)
        response = requests.post(url, files = {'file':img})
        print(response.ok,response.status_code)