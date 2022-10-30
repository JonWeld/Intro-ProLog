# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
# printing each letter on a separate line, except backwards.

fruit = 'banana'
i = len(fruit)

while (i - 1) >= 0 :
    print(fruit[i - 1])
    i -= 1
    
