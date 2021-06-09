'''

18. Write a Python program to print content of elements that contain a specified string of a given web page.

'''
import re
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url).text
soup = BeautifulSoup(reqs, 'html.parser')

print("\nContent of elements that contain 'Python' string:")
str1 = soup.find_all(string=re.compile('Python'))
for txt in str1:
    print(" ".join(txt.split()))