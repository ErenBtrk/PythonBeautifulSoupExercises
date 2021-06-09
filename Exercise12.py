'''
12. Write a Python program to extract all the text from a given web page. 

'''

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

print(soup.get_text().strip())