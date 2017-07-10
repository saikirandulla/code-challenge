import os
import ingest
import json
from dateutil import rrule
import datetime

class customer:
	def __init__(self, rec):
		if(rec['verb'] =="NEW" or rec['verb'] =="UPDATE"):
			self.data=rec
			self.data['first_visit']=rec['event_time'][:4]+rec['event_time'][5:7]+rec['event_time'][8:10]
			self.data['last_visit']=rec['event_time'][:4]+rec['event_time'][5:7]+rec['event_time'][8:10]
			self.data['num_visits']=0
			self.data['total_revenue_from_customer']=0
			self.data['avg_revenue_per_visit']=0
			self.data['avg_visits_per_week']=0
			self.data['cltv']=0
			self.write_new_customer()
		else:
			print("Invalid customer record verb type")
			exit(1)
	def write_new_customer(self):
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