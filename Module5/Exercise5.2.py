largest = None
smallest = None
num = input("Enter a number: ")

try:
    num = int(num)
    smallest = num
    largest = num
except ValueError:
    print("Invalid input")

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest < num:
            largest = num
        if smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")
        pass

print("Maximum is", largest)
print("Minimum is", smallest)