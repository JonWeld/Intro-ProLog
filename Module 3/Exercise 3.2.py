hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print ("Error, please enter numeric input")
    quit()

print(h, r)
if h > 40 :
    reg = (40.0 * r)
    otp = (h - 40.0) * (r * 1.5)
    pay = (reg + otp)
else: 
    pay = (h * r)
print ("Pay:",pay)