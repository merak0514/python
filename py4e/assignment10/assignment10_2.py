# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour,
# print out the counts, one per line, sorted by hour as shown below.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

fname = input('Enter file name: ')
hours = {}
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('Error')
    quit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1
hours_list = sorted(hours.items())
for k, v in hours_list:
    print(k, v)
