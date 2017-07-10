import os
import ingest
import json

class image:
	def __init__(self, rec):
		if(rec['verb'] =='UPLOAD'):
			self.data = rec
			self.write_new_image()
		else:
			print("Invalid image record verb type")
			exit(1)
	def write_new_image(self):
		a = []
		if not os.path.isfile('input.txt'):
			a.append(self.data)
			with open('input.txt', mode='w') as f:
				f.write(json.dumps(a, indent=2))
		else:
			with open('input.txt') as feedsjson:
				feeds = json.load(feedsjson)
			feeds.append(self.data)
			with open('input.txt', mode='w') as f:
				f.write(json.dumps(feeds, indent=2))