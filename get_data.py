from bs4 import BeautifulSoup
import requests
import re
from models import loadSession, addItem, closeSession

#get items of specific page for Safeway ads
def getSafeway(url:str):
    r = requests.get(url)
    data = r.text
    data_html_parsed = BeautifulSoup(data, 'html.parser')
    for item in data_html_parsed.find_all(id=re.compile('CircularItem-\d+')):
        title = item.find("p", {"class": "itemTitle"})
        price = item.find("p", { "class" : "itemPrice" })
        if(title != None and price != None):
            print(title.get_text())
            print(price.get_text())
            addItem(db, title=title.get_text(), priceDesc=price.get_text())
        print("\n")

#Find how many pages are in the Safeway local ads
#Connect to database and store session in db
db = loadSession()
#This is the URL of the first page
url = "http://plan.safeway.com/Circular/Mclean-1688-Anderson-Rd/713374771/Weekly/3"
r = requests.get(url)
data = r.text
data_html_parsed = BeautifulSoup(data, 'html.parser')
getSafeway(url)
for item in data_html_parsed.find("div", {"class":"paging"}).find_all("a", title=re.compile('of')):
    getSafeway("http://plan.safeway.com" + item.get("href"))
closeSession(db)