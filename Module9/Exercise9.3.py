# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from each email address, 
# and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

mail = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    getmail = line.split()
    if len(getmail) < 2 or getmail[0] != 'From':
        continue
    else:
        if getmail[1] not in mail:
            mail[getmail[1]] = 1
        else:
            mail[getmail[1]] += 1

print(mail)