'''
29. Write a Python program to insert tags or strings immediately before specified tags or strings.

'''

from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>", "lxml")
print("Original Markup:")
print(soup.b)
tag = soup.new_tag("i")
tag.string = "Python"
print("\nNew Markup, before inserting the text:")
soup.b.string.insert_before(tag)
print(soup.b)