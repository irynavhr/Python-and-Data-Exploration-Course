size_of_rhombus = 11
M2 = [[0 for _ in range(size_of_rhombus)] for _ in range(size_of_rhombus)]
# print(M2)

# ***************THOUGHTS**************************
# col [0] and [col-1] : col//2-----id of 1st "1"
# col-=2
#
# num_of_iter = col//2 +1-----=item = 9//2 +1
#iteration from 1 to  num_of_iter=5  
# how many "1"? ---- item*2-1
# what id to start? 
# ************************

num_of_iter = size_of_rhombus//2 + 1
for case in range(num_of_iter):
    num_of_ones = (case + 1)*2 - 1
    id_to_start = num_of_iter - case - 1
    for each in range(num_of_ones):
        M2[case][id_to_start + each] = 1
        M2[size_of_rhombus - 1 - case][id_to_start + each] = 1
# print(M2)

# M = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 0, 1, 1, 1, 1, 1, 0, 0],
#      [0, 1, 1, 1, 1, 1, 1, 1, 0],
#      [1, 1, 1, 1, 1, 1, 1, 1, 1],
#      [0, 1, 1, 1, 1, 1, 1, 1, 0],
#      [0, 0, 1, 1, 1, 1, 1, 0, 0],
#      [0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0, 0, 0]]

for r in M2:
    for i in r:
        if i == True:
            print("^", end = "")
        else:
            print(" ", end = "")
    print("")