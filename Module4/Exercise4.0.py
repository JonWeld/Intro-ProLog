def max(x, y, z) :
    if (x >= y) and (x >= z) :
        biggest = x
    elif (y >= x) and (y >= z) :
        biggest = y
    else:
        biggest = z
    return biggest

x = 4
y = 8
z = 2
print(max(x, y, z))
