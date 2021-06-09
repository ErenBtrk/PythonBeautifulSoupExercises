'''
26. Write a Python program to change the tag's contents and replace with the given string.

'''

from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>example.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
tag = soup.a
print("\nOriginal Markup:")
print(tag)
print("\nOriginal Markup with new text:")
tag.string = "CSS"
print(tag)