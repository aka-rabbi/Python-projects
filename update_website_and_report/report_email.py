#!/usr/bin/env python3
import datetime
import os
import locale
from reports import generate_report
from emails import generate,send

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
fruit_description_path= 'supplier-data/descriptions/'
files = os.listdir(fruit_description_path)
def check_extension(files):
    images = []
    for name in files:
        if os.path.splitext(name)[1] =='.txt':
            images.append(name)
    return images
txt_files = check_extension(files)
fruits_list = []
for f in txt_files:
    with open(fruit_description_path+f) as fruit_description:
        fruit_info = list(iter(fruit_description))
        fruits_list.append(' ')
        fruits_list.append('name: {}'.format(fruit_info[0].strip()))
        fruits_list.append('weight: {}'.format(fruit_info[1].strip()))
        fruits_list.append(' ')

if __name__ == "__main__":
    today = datetime.date.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
    #date = 'Processed Update on {}'.format(datetime.date.today())
    generate_report('processed.pdf',title,('<br/>').join(fruits_list))
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = generate('automation@example.com','student-01-2f5a3940372d@example.com','Upload Completed - Online Fruit Store',body,'processed.pdf')
    send(message)