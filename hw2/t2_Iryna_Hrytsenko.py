h = 21
w = 25

#  loop throgh imag matrix:
for i in range(h):
    for j in range(w):
        # Def conds for "*":
        if (
            (i in {0, 1, 2, 18, 19, 20} and j == 12) or  
            (i in {3, 5, 6, 9, 10, 11, 14, 15, 17} and 9 <= j <= 15) or  
            (i in {7, 8, 12, 13} and j in {5, 7, 8, 9, 10, 14, 15, 16, 17, 19}) or  
            (i in {4, 16} and j in {0, 8, 16, 24}) or
            (i in {6, 9, 11, 14} and j in {6, 8, 16, 18}) or
            (i in {5, 15} and j in {3, 7, 17, 21}) or
            (i in {10} and j in {7, 17})
        ):
            print("*", end="")
        else: 
            print(" ", end="")
    print() # next line
