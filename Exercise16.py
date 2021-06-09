'''
16. Write a Python program to retrieve the HTML code of the title,
its text, and the HTML code of its parent.
 
'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url).text
soup = BeautifulSoup(reqs, 'html.parser')



print(soup.title)
print(soup.title.text)
print(soup.title.parent)