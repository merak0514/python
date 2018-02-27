import urllib.request

picture = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()

new = open('stuff_urllib.jpeg', 'wb')
new.write(picture)
new.close()
