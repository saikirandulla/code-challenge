import sys
import json
import ingest

#command line arguments
#First argument takes X customers as input and second argument takes the file name of the events file
def main():
	if len(sys.argv)!=3:
		print ('Only three arguments allowed. Enter the value of X for top X Customers and the sample event file name')
		exit(1)
	input_file=sys.argv[2]
	top_X_customers=int(sys.argv[1])

	if top_X_customers <0:
		print ('Invalid input X for top X Customers. You have to input an integer greater than 0')
		exit(1)

	#Opening the file with events and parsing the JSON file 
	try:	
		with open (input_file) as f:
			event_data=json.load(f)
	except:
		print("Invalid input file name")
		exit(1)

	#calling the Ingest method in calculate 
	data=ingest.Ingest(event_data)
	#calling Analytical Method in calculate
	#calculate.topXSimpleLTVCustomers(top_Customer,dict)
if __name__ == "__main__":
	main()