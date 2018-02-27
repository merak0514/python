# 12.3
# Use urllib to replicate the previous exercise of
# (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters,
# (3) counting the overall number of characters in the document.
# Don't worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.

import urllib.request
import string

# function to format input string to a set of lower words with no punctuation


def format_word(origin_string):
    words = origin_string.rstrip()
    words = words.translate(words.maketrans(
        '', '', string.punctuation)).lower().split()
    return words


count = {}
url = input('Enter the url: ')
try:
    fhand = urllib.request.urlopen('http://' + url)
except:
    print('Fuck')
    quit()
passage = fhand.read(300).decode()
print(passage)

whole_words = format_word(passage)
while True:
    info = fhand.read(3000).decode()
    if len(info) < 1:
        break
    words = format_word(info)
    whole_words = whole_words + words
# whole_words is a set of all the word  of the passage with lowercase.
for word in whole_words:
    count[word] = count.get(word, 0) + 1
if 'i' in count:
    count['I'] = count.pop('i')   # make i upper
new_count = sorted([(k, v) for (v, k) in count.items()], reverse=True)
for v, k in new_count[:20]:
    print(k, v)
