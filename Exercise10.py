'''
10. Write a Python program to find all the link tags and list the first ten from the webpage python.org.

'''

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

result = soup.find_all("a")#[0:4])

for index in range(10):
    print(result[index])