import pandas as pd
import json
import urllib2
import csv

results = ''



def loadCraigslistData():
	#load csv data from api created in kimonolabs that grabs craigslist data
	print("Collecting Craigslist Data For Electronics in Ames, Iowa")
	request = urllib2.Request("https://www.kimonolabs.com/api/csv/b0c7flky?apikey=qvdiZcoVwcx9TlWbDGcqdWMtSamsK7AB", headers={"authorization" : "Bearer mi6aboJU5bcLWzPDuGevrseP5mkMQ9Wt"})
	contents = urllib2.urlopen(request).read()
	
	url = "clist.csv"
	results = pd.read_csv(url)
	print results

#def chooseAction():
	#ask user what action they would like to perform, search/sort

#def sortData():
	#will sort craigslist data by price increasing/decreasing depending on user choice

#def searchData():
	#search csv for items based on keywords provided by user
	#store list temporarily to give user choice to sort by price
	#show user what percentage of items match their keyword
	queryResult = results.query('property3 == "$50"')
	print(queryResult)

loadCraigslistData()
