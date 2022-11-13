# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# By Jonathan Weld

def chop():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list1[1:-1])

def middle():
    list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    newList = list2[1:-1]
    return newList


chop()
Returned = middle()
print(Returned)
