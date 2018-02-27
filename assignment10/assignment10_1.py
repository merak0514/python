# 10.1
# Revise a previous program as follows:
# Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.


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
mails = sorted([(v, k) for k, v in emails.items()], reverse=True)
print(mails)
# for k,v in emails.items():
# 	mails.append(v,k)
# mails.sort(reverse=True)
# print((v, k) for (k, v) in mails[0])    # Error
print([(v, k) for (k, v) in mails][0])
