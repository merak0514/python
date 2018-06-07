# 8.4
# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fname = input('File name: ')
try:
    fhand = open(fname)
except:
    print('Error,What are you doing?')
    quit()
words_list = []
for line in fhand:
    words = line.split()
    for word in words:
        if word not in words_list:
            words_list.append(word)
words_list.sort()
print(words_list)
