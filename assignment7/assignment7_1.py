# 7.1
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
# File: mbox-short.txt


fname = input('Enter a file name: ')
try:
    xfile = open(fname)
except:
    print('Input something wrong!')
    quit()

for line in xfile:
    print(line.upper())
