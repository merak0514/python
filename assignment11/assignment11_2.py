# 11.2
# Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average.
# Enter file:mbox.txt: 38549.7949721
# Enter file:mbox-short.txt: 39756.9259259


import re
fname = input('File name: ')
count = 0
sum = 0
if len(fname) < 1:
    fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print('Error')
    quit()
for line in fhand:
    numbers = re.findall('New Revision: ([0-9]+)', line)
    for number in numbers:
        sum = sum + float(number)
        # print(sum)
        count = count + 1
        # print(count)
average = sum / count
print(average)
