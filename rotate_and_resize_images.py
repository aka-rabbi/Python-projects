#!/usr/bin/env python3
import sys
import os
from os.path import expanduser
from PIL import Image

def rotate_and_resize(root,filenames):
    for file in filenames:
        path =os.path.join(root,file)
        im = Image.open(path).convert('RGB')
        im.resize((640,480)).rotate(90).save(path,'JPEG')
    

def check_jpg(folder):
    _,_,files = next(os.walk(expanduser(folder)))
    images = []
    for name in files:
        if os.path.splitext(name)[1] =='.jpg': 
            images.append(name)
    return images

filenames = check_jpg(sys.argv[1])
rotate_and_resize(sys.argv[1],filenames)



