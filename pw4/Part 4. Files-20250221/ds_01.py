import re
# Provide full path for file name
datne = input('Enter file name: ')
# hand = open('mbox-short.txt')
hand = open(datne)
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))