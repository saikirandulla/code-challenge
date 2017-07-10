import json
from customer import *
from order import *
from siteVisit import *
from image import *
from stats import *
from collections import defaultdict

from datetime import datetime, timedelta


def Ingest(data):

	for rec in data:
		if rec['type']=='CUSTOMER':
			data=customer(rec)

		elif rec['type']=='SITE_VISIT':
			data=siteVisit(rec)
			stat=stats(rec)
			
		elif rec['type']=='IMAGE':
			data=image(rec)

		elif rec['type']=='ORDER':
			data=order(rec)
			stat=stats(rec)
			
		else:
			print ('Invalid Record Type')
			exit(1)



def topXLTVCustomers(rec):
	print("Code in Progress")
		
				
	
