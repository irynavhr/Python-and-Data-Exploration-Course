# DEVELOPED BY IRYNA HRYTSENKO
# first version missed leters adding after procesing file
# secound version is with dict already filled with letters
# first version by defolt

import re

# opening files:
file_name_1 = input("Enter a lv file name:")
file_name_2 = input("Enter a en file name:")
try:
    file1 = open(file_name_1, "r")
    file2 = open(file_name_2, "r")
except:
    print("ERRORE: incorrect file names was recieved!")
    exit()

# data:
alf = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = dict()     # first ver
alphabet2 = dict()     # first ver
# alphabet1 = {i:0 for i in alf}    # secound ver
# alphabet2 = {i:0 for i in alf}    # secound ver
alf_list_1 = list() # (for first-main version only):
alf_list_2 = list() # (for first-main version only):
len_text_1_lv = 0
len_text_2_en = 0

# through file 1:
for line in file1:
    letters_of_line = re.findall(r"[a-z]", line.lower()[:-1])
    for leter in letters_of_line:
        len_text_1_lv += 1
        alphabet1[leter] = alphabet1.get(leter, 0) + 1   # first ver
        # alphabet1[leter] += 1    # secound ver
file1.close()
# through file 2:
for line in file2:
    letters_of_line = re.findall(r"[a-z]", line.lower()[:-1])
    for leter in letters_of_line:
        len_text_2_en += 1
        alphabet2[leter] = alphabet2.get(leter, 0) + 1    # first ver
        # alphabet2[leter] += 1     # secound ver

file2.close()

# add miss leters (for first-main version only)
for l in alf:
    alphabet1[l] = alphabet1.get(l, 0)
    alphabet2[l] = alphabet2.get(l, 0)
    
# convertint both alphabets from dict to list of tupl to make pos to sort:
for k, v in alphabet1.items():
    alf_list_1.append((k, v))
for k, v in alphabet2.items():
    alf_list_2.append((k, v))
# sorting:
alf_list_1.sort(key=lambda x: x[1], reverse=True)
alf_list_2.sort(key=lambda x: x[1], reverse=True)

# PRINTING
print("{:<25} {}".format("Latvian:", "English:"))
len_alf = len(alf)
for l in range(len_alf):
    print("{:<25} {}: {:.2f}%".format
         (str(alf_list_1[l][0]) +": "+ str(round((alf_list_1[l][1]/len_text_1_lv)*100, 2))+"%", 
                                    alf_list_2[l][0], (alf_list_2[l][1]/len_text_2_en)*100))
    