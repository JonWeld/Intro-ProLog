# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

mail = list()
fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    if not line.startswith('From:' ):
        continue
    line = line.split()
    mail.append(line[1])

email = dict()
for word in mail:
    email[word] = email.get(word, 0) + 1
 
ecount = None
eword = None

for word, count in email.items():
    if ecount is None or count > ecount:
        ecount = count
        eword = word

print(eword, ecount)