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


#Function to claculate top X customers
def topXSimpleLTVCustomers(top_Customer,dict):
	cust_ltv={} #dictionary to hold customer id and LTV value for top X customer
	t=10 
	ltv=0
	
	for c in dict.keys(): #going through the dictionary which has all the details loaded
		
		no_of_visit=0
		total_amount=0
		#total amount spent by customer
		order=dict[c].get('ORDER',None)
		if order is not None:
			for o in order:
				total_amount=total_amount+float(o.total_amount.split(' ')[0].strip())
	
		#total number of visits
		
		visit=dict[c].get('SITE_VISIT',None)
		if visit is not None:
			no_of_visit=len(visit)
		
		#Logic to get the number of weeks
		curr=dict[c].get('CUSTOMER')[0].event_time
		curr = datetime.strptime(curr, '%Y-%m-%dT%H:%M:%S.%fZ').date()
		first_week =curr - timedelta(days=curr.weekday())#Assuming the given date in the file as start week and taking the starting week of the customer 
		this_week=datetime.now().date()-timedelta(days=datetime.now().date().weekday())#Current week 
		total_weeks=int(abs((first_week-this_week).days))/7 
		if total_weeks==0: #check if visit is current week
			total_weeks=1
 

		#calculating the avaerage part 'a'
		if no_of_visit>0: #checking this inorder to avoid divide by zero error caused by no_of_visit
			avg_cust_amount=total_amount/no_of_visit
			site_visit_per_week=no_of_visit/total_weeks
			a=avg_cust_amount*site_visit_per_week
			ltv=52*a*t
		else:
			ltv=0
		
		cust_ltv[c]=ltv
	
	#sorting the dictionary and printing the top X customers
	result=[]
	if top_Customer >  len(dict):
		print ('X is greater than number of customers in the input file,however printing all the customers in the file')
		top_Customer=len(dict)
	for i in  sorted(cust_ltv,key=cust_ltv.get,reverse=True):
		result.append((i,cust_ltv.get(i)))
	print ('Customer ID     LTV')
	for k in range(0,top_Customer):
		print (str(result[k][0])+'                '+ str(result[k][1]))
		
				
	
