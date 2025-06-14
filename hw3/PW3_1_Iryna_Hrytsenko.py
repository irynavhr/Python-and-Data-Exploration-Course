# developed by Iryna Hrytsenko
import re

high = {}
low = {}
aver = {}

with open("cereals.csv", "r") as data:
    for line in data:
        # transform str into list of str:
        line_list = line.strip().split(",")
        
        # exclude wrong data:
        if len(line_list) != 16 or line_list[0]=="name":
            continue
        
        # define data needed for procesing:
        name = line_list[0]
        sereal_type = line_list[2]
        rate = (line_list[-1])
        # print(name, sereal_type, rate)

        # sort:
        if (sereal_type not in high) and (sereal_type not in low):
            high[sereal_type] = rate +","+ name
            low[sereal_type] = rate +","+ name
            aver[sereal_type] = rate +","+ str(1)
            # print("high: ",high)
            # print("low: ",low)
        else:
            # count sum and quant for aver
            aver[sereal_type] = str(float(aver[sereal_type].split(",")[0]) + float(rate)) + "," + str(float(aver[sereal_type].split(",")[1]) + 1)
            if float(rate) > float(high[sereal_type].split(",")[0]):
                high[sereal_type] = rate +","+ name
                # print("high: ",high)
                # print("low: ",low)
            elif float(rate) < float(low[sereal_type].split(",")[0]):
                low[sereal_type] = rate +","+ name
                # print("high: ",high)
                # print("low: ",low)
        
# print extract:
# print(high)
# print(low)

# printing res:
for v in high:
    print("Cereal type:", end=" ")
    if v == "H":
        print("Hot")
    else:
        print("Cold")
    print("The lowest cereals rating value: ", low[v].split(",")[0], "Cereals name: ", low[v].split(",")[1])
    print("The average cereals rating value: ", float(aver[v].split(",")[0])/float(aver[v].split(",")[1]))
    print("The highest cereals rating value: ", high[v].split(",")[0], "Cereals name: ", high[v].split(",")[1])