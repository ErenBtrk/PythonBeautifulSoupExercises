'''
11. Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org.

'''

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

result = soup.find_all(["h1","h2","h3"])

for h in result:
    print(h.name + '-' + h.text.strip())

