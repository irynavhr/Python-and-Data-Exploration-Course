# !!! correct code to comprehance part 
# of code in try statement                --- done!

h = input("Enter Hours:")
r = input("Enter Rate:")

c = 0

try:
    h = float(h)
    r = float(r)
    c = 1
except:
    print("Error, please enter numeric input")

if c==1:
    if h>40:
        p = 40*r + (h-40)*r*1.75
    else:
        p = h*r
    print("Pay:", p)