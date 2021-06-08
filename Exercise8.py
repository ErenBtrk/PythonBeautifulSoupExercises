'''
8. Write a Python program to extract all the URLs from 
the webpage python.org that are nested within <li> tags from . 

'''
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

result = soup.find_all("li")

for li in result:
    extractURL = li.find("a").get("href")
    print(extractURL) 