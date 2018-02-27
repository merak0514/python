# 11.3
# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Give out the sum


import re
fname = input('File name: ')
sum = 0
try:
    fhand = open(fname)
except:
    print('Error')
    quit()
for line in fhand:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + float(number)
print(sum)
