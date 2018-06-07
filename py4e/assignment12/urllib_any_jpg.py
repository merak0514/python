import urllib.request
# import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL: ')
picture = urllib.request.urlopen(url, context=ctx)
# picture_path = 'p'
# count = 0
# for line in picture:
#     picture_path = re.findall('<title>(.+?)\.', line)
#     print(count)
#     count = count + 1
#     if len(picture_path) > 2:
#         break
fhand = open('a.jpg', 'wb')
size = 0
while True:
    info = picture.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)
print('Size: ', size)
fhand.close()
