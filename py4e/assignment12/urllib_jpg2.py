# In order to avoid running out of memory,
# we retrieve the data in blocks (or buffers) and then write each block to your disk before retrieving the next block.
# This way the program can read any size file without using up all of the memory you have in your computer.

import urllib.request

picture = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3_urllib_jpg2.jpg', 'wb')
size = 0
while True:
    info = picture.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)
print(size, '...')
fhand.close()
