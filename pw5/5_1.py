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
manufactors_serials = dict()

# count how many sereals each mnf has:
file.readline()
for line in file:
    mnf = line.split(",")[1]
    manufactors_serials[mnf] = manufactors_serials.get(mnf, 0 ) + 1
file.close()
print(manufactors_serials)

# sorting
mnf_amount_srls_list = list()
for k, v in manufactors_serials.items():
    mnf_amount_srls_list.append((k, v))
mnf_amount_srls_list = sorted(mnf_amount_srls_list)

# printing
print("SORTED:")
for k, v in mnf_amount_srls_list:
    if len(k)==1:
        print(manuf_descr[k], ":", v)
    else:
        print(k, ":", v)