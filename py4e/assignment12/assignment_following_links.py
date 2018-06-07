# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.# noqa
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list,# noqa
# follow that link and repeat the process a number of times and report the last name you find.# noqa

# We provide two files for this assignment.
# One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment# noqa

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jenna.html
# Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load:D

from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input the needed imformation
url = input('Enter url-')
count = int(input('Enter count-'))
position = int(input('Enter position-'))
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

for x in range(0, count):
    print('retrieving: ', url)
    page = urlopen(url, context=ctx).read()
    html = BeautifulSoup(page, 'html.parser')
    tags = html('a')    # All the a tag in this page
    tag = tags[position - 1]    # The a tag at the asked position
    url = tag.get('href', None)
    print(tag)
    # print(x)
print(url)
print('Answer: ', tag.contents[0])
