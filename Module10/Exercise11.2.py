# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average as an integer.

import re

fname = input('Enter file:')
try:
    hand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
lt = list()
for line in hand:
    line = line.rstrip()
    num1 = re.findall('^New Revision:(\s[0-9.]+)',line)
    if len(num1) > 0:
        for number in num1:
            number = float(number)
        lt.append(number)
avg = sum(lt)/len(lt)
print(avg)