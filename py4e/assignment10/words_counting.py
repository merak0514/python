# count words
import string
fname = input('File name: ')
try:
    fhand = open(fname)
except:
    print('Error')
    quit()
wordlist = {}
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        wordlist[word] = wordlist.get(word, 0) + 1
if 'i' in wordlist.keys():
    wordlist['I'] = wordlist.pop('i')  # HIGH LIGHT
new_wordlist = sorted(
    [(k, v) for (v, k) in wordlist.items()], reverse=True)  # HIGH LIGHT
print('Most used words: ')
for k, v in new_wordlist[0:9]:
    print(v, k)
