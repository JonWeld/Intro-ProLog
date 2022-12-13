# Variables are assigned
total = 0
count = 0
numbers = [] # List variable

# Gets input and loops for every input except if the input is quit
while True:
    num = input('Enter a number: ')
    if num == 'quit':
        break
    else:
        num = float(num)            # Turns the variable num into a float
        numbers.append(num)
        total += num                
        count += 1

# Outputs the total, count, and the average
print('Total:', total)
print('Count:', count)
print('Average:', total/count)