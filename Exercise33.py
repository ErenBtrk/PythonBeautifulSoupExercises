'''
33. Write a Python program to remove a tag from a given
tree of html document and destroy it and its contents. 

'''

from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
a_tag = soup.a
print(a_tag)
new_tag = soup.a.decompose()
print("After decomposing:")
print(new_tag)