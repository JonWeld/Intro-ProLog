# This program records the domain name (instead of the address) where the message was sent from 
# instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

file = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file, 'r')
    if line.startswith("From ")]

edict = {}

for line in lines:
    line = line.split()
    email = line[1]
    emain = email.split("@")[1]
    edict[emain] = edict.get(emain, 0) + 1

print (edict)