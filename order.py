import os
import ingest
import json

class order:
	def __init__(self, rec):
		if(rec['verb'] =="NEW" or rec['verb'] =='UPDATE'):
			self.data = rec
			self.write_new_order()
		else:
			print("Invalid order record verb type")
			exit(1)
	def write_new_order(self):
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