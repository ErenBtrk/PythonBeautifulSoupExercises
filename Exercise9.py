'''
9. Write a Python program to find all the h2 tags and list the first four from the webpage python.org.

'''

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

result = soup.find_all("h2")#[0:4])

for index in range(4):
    print(result[index])
