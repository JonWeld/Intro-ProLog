def computepay(h, r):
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input ("Enter Rate:")
    r = float(rate)
    if h > 40 :
        reg = (40.0 * r)
        otp = (h - 40.0) * (r * 1.5)
        pay = (reg + otp)
    else: 
        pay = (h * r)
    return pay

p = computepay(10, 20)
print("Pay", p)