'''
13. Write a Python program to print the names of all HTML
tags of a given web page going through the document tree.
 
'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
print("\nNames of all HTML tags (https://www.python.org):\n")

for tag in soup.findAll():
    print(tag.name)

