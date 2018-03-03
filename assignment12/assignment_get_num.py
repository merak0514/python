# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.# noqa
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_70008.html (Sum ends with 7)# noqa
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:# noqa
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

import ssl
from bs4 import BeautifulSoup
import urllib.request

sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the page
url = input('Enter the URL-')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
try:
    fhand = urllib.request.urlopen(url, context=ctx).read()
except:
    print("Error: can't open the  page")
    quit()

html = BeautifulSoup(fhand, 'html.parser')

spans = html('span')
for span in spans:
    sum = sum + int(span.contents[0])
print(sum)
