import os
import ingest
import json
from dateutil import rrule
from datetime import datetime, timedelta, date
import numpy as np

class stats:
	def __init__(self, rec):		
		with open('input.txt') as feedsjson:
			feeds = json.load(feedsjson)
		self.data={}
		self.data['num_visits']=0
		for input_rec in feeds:
			if input_rec['type'] == "CUSTOMER" and input_rec['key']==rec['customer_id'] and rec['type']=='SITE_VISIT':
				self.data['key'] = rec['customer_id']
				self.data['type']="STATS"
				self.data['first_visit']=input_rec['first_visit']
				self.data['last_visit']=rec['event_time'][:4]+rec['event_time'][5:7]+rec['event_time'][8:10]
				self.data['avg_revenue_per_visit']=input_rec['avg_revenue_per_visit']
				self.data['cltv']=input_rec['cltv']
				self.data['num_visits']=input_rec['num_visits']+1
				if self.weeks_between(self.data['first_visit'], self.data['last_visit'])!=0:
					self.data['avg_visits_per_week']=self.data['num_visits']/self.weeks_between(self.data['first_visit'], self.data['last_visit'])
				self.write_customer_stats()

			if input_rec['type'] == "CUSTOMER" and input_rec['key']==rec['customer_id'] and rec['type']=='ORDER':
				self.data['key'] = rec['customer_id']
				self.data['type']="STATS"
				self.data['first_visit']=input_rec['first_visit']
				self.data['last_visit']=rec['event_time'][:4]+rec['event_time'][5:7]+rec['event_time'][8:10]
				self.data['avg_revenue_per_visit']=input_rec['avg_revenue_per_visit']
				self.data['cltv']=input_rec['cltv']
				self.data['num_visits']=input_rec['num_visits']
				self.data['avg_visits_per_week']=input_rec['avg_visits_per_week']
				self.data['total_revenue_from_customer']=input_rec['total_revenue_from_customer']+float(rec['total_amount'][:-4])
				if self.data['num_visits']!=0:
					self.data['avg_revenue_per_visit']=self.data['total_revenue_from_customer']/self.data['num_visits']
				self.data['cltv']=self.data['avg_revenue_per_visit']*self.data['avg_visits_per_week']*52*10
				self.write_customer_stats()

	def write_customer_stats(self):
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

	def weeks_between(self,d1, d2):
		# weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
		# return weeks.count()
		d1_new=date(int(d1[:4]),int(d1[4:6]),int(d1[6:8]))
		d2_new=date(int(d2[:4]),int(d2[4:6]),int(d2[6:8]))
		monday1 = (d1_new - timedelta(days=d1_new.weekday()))
		monday2 = (d2_new - timedelta(days=d2_new.weekday()))
		return (monday2 - monday1).days / 7
		#return (d2-d1).apply(lambda x: x/np.timedelta64(1,'W'))


