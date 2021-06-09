'''
14. Write a Python program to retrieve children of the html tag from a given web page. 

'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
print("\nNames of all HTML tags (https://www.python.org):\n")

for tag in soup.html:
    if(tag.name != None):
        print(tag.name)
    
        
