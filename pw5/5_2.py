# open
file_name = input("Enter a file name:")
try:
    file = open(file_name, "r")
except:
    print("ERRORE: incorrect file name was recieved!")
    exit()

# data:   
manuf_descr = {"A" : "American Home Food Products", "G" : "General Mills", "K" : "Kelloggs", 
               "N" : "Nabisco", "P" : "Post", "Q" : "Quaker Oats", "R" : "Ralston Purina"}
mnf_cups_calories = list()

# get mnf, cups and caloris into tuple

file.readline()
for line in file:
    line_list = line.split(",")
    if len(line_list) == 16:
        mnf = line_list[1]
        if len(mnf) == 1:
            mnf = manuf_descr[mnf]
        cups = float(line_list[14])
        calories = int(line_list[3])
        mnf_cups_calories.append((mnf, cups, calories))
file.close()
print(mnf_cups_calories)

# sorting
mnf_cups_calories_sorted = sorted(mnf_cups_calories, key=lambda x: x[2])

# printing
# print(mnf_cups_calories_sorted)
print("SORTED:")
print("{:<30} {:<10} {:<10}".format("Manufacturer:", "Cups:", "Calories:"))
for tuple in mnf_cups_calories_sorted:
    manufacturer = tuple[0]
    cups = tuple[1]
    calories = tuple[2]
    print("{:<30} {:<10} {:<10}".format(manufacturer + ":", cups, calories))