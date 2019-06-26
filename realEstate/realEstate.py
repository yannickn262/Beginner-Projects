import requests, pandas
import re
from bs4 import BeautifulSoup

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("https://www.realtor.com/realestateandhomes-search/Jacksonville_FL", headers = headers)
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "detail-wrap"})


l = []
for item in all:
    hash = {}
    #finds price
    try:
        hash["Price"] = item.find("span", {"class": "data-price"}).text.replace("\n", "").replace(" ", "")
        #print (hash["Price"])
    except:
        hash["Price"] = "None"
    #finds # beds and prevents print from auto creating a newline
    try:
        hash["Beds"] = item.find("span", {"class": "data-value meta-beds"}).text.replace(" ", "")
        #print (hash["Beds"] + " bed ", end = " ")
    except:
        hash["Beds"] = "None"
    try:
        #get number of bathrooms
        hash["Baths"] = item.find("ul", {"class": "prop-meta ellipsis"}).find_all("li")[1].find("span",{"class":"data-value"}).text.replace(" ", "")
        #print(hash["Baths"] + " bath ", end = " ")
    except:
        hash["Baths"] = "None"
        pass
    try:
        #gets square footage
        hash["Sqft"] = item.find("ul", {"class": "prop-meta ellipsis"}).find_all("li")[2].find("span",{"class":"data-value"}).text.replace(" ", "")
        #print(hash["Sqft"] + " sqft ")
    except:
        hash["Sqft"] = "None"
        pass
    try:
        #gets address
        str = item.find("div", {"class" : "address ellipsis "}).text.replace("\n", "").replace(" ", "")
        hash["Address"] = str
        #need to fix: add space to first part of address and last (can solve via more detailed scrape or use regex commands)
        #print(hash["Address"])
    except:
        hash["Address"] = "none"
    l.append(hash)
    #print()

df = pandas.DataFrame(l)
df.to_csv("Output.csv")
