# 7.2
# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# Use the file name mbox-short.txt as the file name


fname = input('Enter a file name: ')
total = 0
count = 0
try:
    xfile = open(fname)
except:
    print('Wrong name')
    quit()
position = 'X-DSPAM-Confidence:'.find(':')
for line in xfile:
    if line.startswith('X-DSPAM-Confidence:'):
        number = line[position + 1:]
        try:
            number = float(number)
        except:
            print('Wrong File')
            quit()
        total = total + number
        count = count + 1
average = total / count
print('Average spam confidence:', average)
