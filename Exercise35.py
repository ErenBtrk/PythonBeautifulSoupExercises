'''
35. Write a Python program to wrap an element in
 the specified tag and create the new wrapper. 

'''

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Python exercises.</p>", "lxml")
print("Original Markup:")
print(soup.p.string.wrap(soup.new_tag("i")))
print("\nNew Markup:")
print(soup.p.wrap(soup.new_tag("div")))