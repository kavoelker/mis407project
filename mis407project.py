import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show, plot
import json
import urllib2
import csv

url = "clist2.csv"
results = pd.read_csv(url)
#removes rows with missing values
results = results.dropna(how='any')
#removes '$' on price data
results['price'] = results['price'].map(lambda x: str(x)[1:])
#changes prices to integers
results['price'] = results['price'].astype(int)


def loadCraigslistData():
     #load csv data from api created in kimonolabs that grabs craigslist data
     print("Collecting Craigslist Data For Electronics in Ames, Iowa")
     request = urllib2.Request("https://www.kimonolabs.com/api/csv/b0c7flky?apikey=qvdiZcoVwcx9TlWbDGcqdWMtSamsK7AB", headers={"authorization" : "Bearer mi6aboJU5bcLWzPDuGevrseP5mkMQ9Wt"})
     
     
#     with open("clist2.csv", "w") as newfile:
#          with open("clist1.csv") as oldfile:
#               oldfile = oldfile.readlines()
#               newfile.write(oldfile[0])
#               for line in oldfile[1:]:
#                    line = line.split(",")
#                    line[0] = line[0].upper()
#                    newfile.write(",".join(line))

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
          chooseAction()
          

def secondaryMenu(search):
    #menu that user is brought to after search
    search = search
    print("Select a corresponding number that matches the action you would like to take.")
    print("1: Find the average price")
    print("2: Find the range of prices in your search")
    print("3: Plot out the data in your search")
    print("4: See how many "+search+"'S there are compared to all electronics")
    print("")
    print("Press S to perform another search")
    print("Press Q to quit")
    menuSelection = raw_input()
    if menuSelection == "1":
        avgData(search)
    elif menuSelection == "2":
        priceRangeData(search)
    elif menuSelection == "3":
        pricingHist(search)
    elif menuSelection == "4":
        ratio(search)
    elif menuSelection == "q":
        print("Thank You")
    elif menuSelection == "s":
        searchData()
    else:
        print("Please choose an action that is on the menu.")
        secondaryMenu(search)
        
        
def advance(search):
    #helper function that asks if the user would like to do more with the search
    print("Would you like to do more with your search? (y/n)")
    advance = raw_input()
    if advance == "y":
        secondaryMenu(search)
    else:
        print("Thank you")
        

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
     print("would you like more information about results matching "+search+"? (y/n)")
     moreInfo = raw_input()
     if moreInfo == "y":
         secondaryMenu(search)
     else:
         print("Thank you")
     

def pricingHist(search):
    #creates histogram that takes various items and lays them out by price.
    dataSet = results[results['description'].str.contains(search)]
    dataSet['price'].diff().hist()
    dataSet.plot()
    show()
    advance(search)
    
    #dataSet['price'].plot(kind='hist')


def priceRangeData(search):
    #looks at max and min data to see the price range for a search
    dataSet = results[results['description'].str.contains(search)]
    
    maximum = dataSet.price.max()
    minimum = dataSet.price.min()
    print("Pricing varies from $"+str(minimum)+" to $"+str(maximum))
    advance(search)
   
         
def avgData(search): 
    #finds the average price of a set of items
    dataSet = results[results['description'].str.contains(search)]
    
    avg = dataSet.price.mean()
    
    print("The average cost of a "+search+" is $%.2f" % avg)
    advance(search)
    
def ratio(search):
    #calculates percentage of search results compared to total items
    dataSet = results[results['description'].str.contains(search)]
    
    numSearchResults = len(dataSet)
    totalItems = float(len(results))
    searchRatio = numSearchResults/totalItems
    searchRatio = searchRatio*100
    print ("Your search for "+search+" makes up %.2f percent of total items." % searchRatio)
    
    advance(search)
    
    
  
loadCraigslistData()


