import urllib.request
import re

url_address = input('URL Address: ')
try:
    fhand = urllib.request.urlopen('http://' + url_address)
    print(fhand)
except:
    print('Error')
    quit()
for line in fhand:
    hrefs = re.findall('href="(http[s]*://.+?)"|href="(/\w+?)"', line.decode())
    for href in hrefs:
        print(href)
