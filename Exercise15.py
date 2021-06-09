'''
15. Write a Python program to retrieve all descendants of the body tag from a given web page.

'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url).text
soup = BeautifulSoup(reqs, 'html.parser')
print("\nNames of all HTML tags (https://www.python.org):\n")


for tag in soup.html.descendants:
    if(tag.name != None):
        print(tag.name)

    