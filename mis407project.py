import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import urllib2
import csv

url = "clist2.csv"
results = pd.read_csv(url)
#removes rows with missing values
results = results.dropna(how='any')
results['price'] = results['price'].map(lambda x: str(x)[1:])
results['price'] = results['price'].astype(int)


def loadCraigslistData():
     #load csv data from api created in kimonolabs that grabs craigslist data
     print("Collecting Craigslist Data For Electronics in Ames, Iowa")
     request = urllib2.Request("https://www.kimonolabs.com/api/csv/b0c7flky?apikey=qvdiZcoVwcx9TlWbDGcqdWMtSamsK7AB", headers={"authorization" : "Bearer mi6aboJU5bcLWzPDuGevrseP5mkMQ9Wt"})
     contents = urllib2.urlopen(request).read()
     
     
     with open("clist2.csv", "w") as newfile:
          with open("clist1.csv") as oldfile:
               oldfile = oldfile.readlines()
               newfile.write(oldfile[0])
               for line in oldfile[1:]:
                    line = line.split(",")
                    line[0] = line[0].upper()
                    newfile.write(",".join(line))

     url = "clist2.csv"
     results = pd.read_csv(url)

     print("Craigslist data loaded")
     chooseAction()
     

def chooseAction():
     #ask user what action they would like to perform, search/sort
     print("Would you like to search or sort the data")
     choice = raw_input()
     choice = choice.lower()
     if choice == "search":
          searchData()
     elif choice == "sort":
          sortData()
     else:
          print("Enter either search or sort")

def sortData():
     #will sort craigslist data by price increasing/decreasing depending on user choice
     print("")

def searchData():
     #search csv for items based on keywords provided by user
     #store list temporarily to give user choice to sort by price
     #show user what percentage of items match their keyword
     print("What item would you like to find?")
     search = raw_input()
     search = search.upper()
         
     searchData = results[results['description'].str.contains(search)]
     print(searchData)
     print("would you like more information about results matching "+search+"?")
     moreInfo = raw_input()
     if moreInfo == "yes":
         avgData(search)
     else:
         print("")
     

     
def avgData(search):
    
    #finds the average price of a set of items
    dataSet = results[results['description'].str.contains(search)]
    
    #removes '$' on price data
    value = dataSet['price']
    
    print dataSet.price.mean() 
    print value
    print len(value)
#    x = 0
#    while (len(value)-1) >= x:
#        tempValue = value[x]
#        if tempValue is None:
#            x += 1
#        else:
#            print value[x]
#            x += 1
    
searchData()
loadCraigslistData()


