# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from
# (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fname = input('File name: ')
addresses = {}
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
        email = words[1]
        delimiter = '@'
        address = email.split(delimiter)[1]
        addresses[address] = addresses.get(address, 0) + 1
print(addresses)
