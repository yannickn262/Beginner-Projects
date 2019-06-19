import requests
import re
from bs4 import BeautifulSoup

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("https://www.realtor.com/realestateandhomes-search/Jacksonville_FL", headers = headers)
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "detail-wrap"})

for item in all:
    #finds price
    print (item.find("span", {"class": "data-price"}).text.replace("\n", "").replace(" ", ""), end = " ")
    #finds # beds and prevents print from auto creating a newline
    print (item.find("span", {"class": "data-value meta-beds"}).text.replace(" ", "") + " bed ", end = " ")
    try:
        #attempting to get the number of bathrooms
        print(item.find("ul", {"class": "prop-meta ellipsis"}).find_all("li")[1].find("span",{"class":"data-value"}).text.replace(" ", "") + " bath ", end = " ")
        #gets square footage
        print(item.find("ul", {"class": "prop-meta ellipsis"}).find_all("li")[2].find("span",{"class":"data-value"}).text.replace(" ", "") + " sqft ")
    except:
        pass

    str = item.find("div", {"class" : "address ellipsis "}).text.replace("\n", "").replace(" ", "")
    #need to fix: add space to first part of pr
    " ".join(str.split())
    print(str)
    print()
