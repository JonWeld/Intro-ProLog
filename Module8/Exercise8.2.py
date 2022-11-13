# Exercise 2: Figure out which line of the below program is still not properly guarded. 
# See if you can construct a text file which causes the program to fail 
# and then modify the program so that the line is properly guarded 
# and test it to make sure it handles your new text file.


fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()

    if len(words) < 4:
        continue
    if words[0] != 'From':
        continue
    print(words[2])