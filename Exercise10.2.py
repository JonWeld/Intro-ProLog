# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

fname = input("Enter file name:")
if len(fname) < 1 : fname = "mbox-short.txt"
lines = open(fname)
d1 = dict()
for line in lines:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d1[line]=d1.get(line,0)+1

lst=list()        
for value,count in d1.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)