# 9.4
# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
emails = {}
largest = [None, None]
if len(name) < 1:
    name = "mbox-short.txt"
try:
    fhand = open(name)
except:
    print('Error')
    quit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1
for email_address in emails:
    if largest[0] == None:
        largest[0] = email_address
        largest[1] = emails[email_address]
    else:
        if emails[email_address] > largest[1]:
            largest[0] = email_address
            largest[1] = emails[email_address]
print(largest[0], largest[1])
