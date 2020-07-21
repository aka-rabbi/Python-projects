#!/usr/bin/env python3
import sys
import os
from os.path import expanduser
from PIL import Image

def rotate_and_resize(root,filenames):
    for file in filenames:
        path =os.path.join(root,file)
        new_path = os.path.join(root,os.path.splitext(file)[0])
        im = Image.open(path).convert('RGB')
        im.resize((600,400)).save(new_path+'.jpeg','JPEG')

def check_extension(folder):
    _,_,files = next(os.walk(expanduser(folder)))
    images = []
    for name in files:
        if os.path.splitext(name)[1] =='.tiff':
            images.append(name)
    return images

filenames = check_extension(sys.argv[1])
rotate_and_resize(sys.argv[1],filenames)