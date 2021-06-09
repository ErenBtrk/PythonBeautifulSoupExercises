'''
19. Write a Python program to print the element(s) that has a specified id of a given web page.

'''

import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nelement(s) that has #python-network id:\n")
print(soup.select_one("#python-network"))