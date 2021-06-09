'''
17. Write a Python program to find and print all li tags of a given web page.

'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.w3resource.com/'
reqs = requests.get(url).text
soup = BeautifulSoup(reqs, 'html.parser')

result = soup.find_all("li")

for tag in result:
    print(tag.name,tag.text)