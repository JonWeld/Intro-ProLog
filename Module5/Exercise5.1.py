num = 0
total = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    num = num + 1
    total = total + fval
print("All done")
print("Total:",total, "\nNumber of numbers entered:", num, "\nAverage:", total/num)
