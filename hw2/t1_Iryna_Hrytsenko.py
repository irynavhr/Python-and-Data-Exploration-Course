def compute_wage(hours, rate):
    if h>40:
        p = 40*r + (h-40)*r*1.75
    else:
        p = h*r
    print("Pay:", p)

# take vals from kb
h = input("Enter Hours:")
r = input("Enter Rate:")

# check vals and if it's ok --> call compute_wage 
try:
    h = float(h)
    r = float(r)
    compute_wage(h, r)
except:
    print("Error, please enter numeric input")