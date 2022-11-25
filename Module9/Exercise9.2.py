# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

dates = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    getword = line.split()
    if len(getword) < 3 or getword[0] != 'From':
        continue
    else:
        if getword[2] not in dates:
            dates[getword[2]] = 1
        else:
            dates[getword[2]] += 1

print(dates)


