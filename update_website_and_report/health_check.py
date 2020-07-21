#!/usr/bin/env python3
import os
from psutil import cpu_percent,virtual_memory
from shutil import disk_usage
from emails import generate_no_attachment,send

du = disk_usage('/')
free_percent = du.free/du.total*100
cpu = cpu_percent(1)
mem = virtual_memory()
mem_limit = 500*1024*1024
body = 'Please check your system and resolve the issue as soon as possible.'
if mem.available<mem_limit:
    message = generate_no_attachment('automation@example.com','<user>@example.com','Error - Available memory is less than 500MB',body)
    send(message)
if free_percent<20:
    message = generate_no_attachment('automation@example.com','<user>@example.com','Error - Available disk space is less than 20%',body)
    send(message)
if cpu>80:
    message = generate_no_attachment('automation@example.com','<user>@example.com','Error - CPU usage is over 80%',body)
    send(message)
response = os.system("ping -c 1 "+'localhost')
if response !=0:
    message = generate_no_attachment('automation@example.com','<user>@example.com','Error - localhost cannot be resolved to 127.0.0.1',body)
    send(message)