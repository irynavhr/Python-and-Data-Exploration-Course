#  designed by iryna Hrytsenko
import re

dict = {"A":"American Home Food Products", "G":"General Mills", "K":"Kelloggs", 
        "N":"Nabisco", "P":"Post", "Q":"Quaker Oats", "R":"Ralston Purina"}

# x = "jnsnv"
# y = "A"
# print(len(x), len(y))
# print(dict[y])


with open("cereals.csv", "r") as data:
    for line in data:
        cereal_name_id = line.find(",")
        manufacturer_id = line.find(",", cereal_name_id + 1)
        name = line[:cereal_name_id]
        mnf = line[cereal_name_id+1:manufacturer_id].strip()
        if len(mnf)<2:
            print(f"{dict[mnf]}:{name}")
        else:
            print(f"{mnf}:{name}")
    