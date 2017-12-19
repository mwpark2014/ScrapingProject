from bs4 import BeautifulSoup
import requests
import re

url = "http://plan.safeway.com/Circular/Mclean-1688-Anderson-Rd/713374771/Weekly"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
#soup = BeautifulSoup('html.parser')

for item in soup.find_all(id=re.compile('CircularItem-\d+')):
    #TODO: Filter out the gift card, which has None for itemTitle and itemPrice
    print(item.find("p", {"class": "itemTitle"}))
    print(item.find("p", { "class" : "itemPrice" }))
    print("\n")