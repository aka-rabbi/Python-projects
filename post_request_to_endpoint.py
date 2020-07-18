#!/usr/bin/env python3
import os
import json
import requests

feedback_path = '<>' #enter your desired folder here
files = os.listdir(feedback_path)
for f in files:
	review_dict = {}
	with open(feedback_path+f) as feedback:
		user_info = list(iter(feedback))
		feedback_text = ' '.join([l.strip() for l in user_info[3:]])

		review_dict['title'] = user_info[0]
		review_dict['name'] = user_info[1]
		review_dict['date'] = user_info[2]
		review_dict['feedback'] = feedback_text

		feedback_json = json.dumps(review_dict)
		response = requests.post('<endpoint>', data = review_dict)  #json doesn't work it seems
		print(response.ok,response.status_code)