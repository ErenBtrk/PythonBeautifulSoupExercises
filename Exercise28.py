'''
28. Write a Python program to insert a new text within a url in a specified position.

'''

from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>w3resource.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
tag = soup.a
print("Original Markup:")
print(tag.contents)
print(soup.a)
tag.insert(2, "CSS") #2-> Position of the text (1, 2, 3…)
print("\nNew url after inserting the text:")
print(tag.contents)
print(soup.a)