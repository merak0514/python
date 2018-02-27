# Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come from each email address,
# and print the dictionary.


fname = input('File name: ')
emails = {}
try:
    fhand = open(fname)
except:
    print('Error')
    quit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1
print(emails)
