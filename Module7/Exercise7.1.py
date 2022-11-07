# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fhand = open('mbox-short.txt')
inp = fhand.read()
print (str.upper(inp))
