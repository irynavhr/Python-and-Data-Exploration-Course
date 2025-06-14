import re

data_count = {}
# print(type(data_count))

file_name = input("Enter a file name:")
try:
    file = open(file_name, "r")
except:
    print("ERRORE: incorrect file name was recieved!")
    exit()


for line in file:
    if len(line.split(",")) != 16:
        print("bla-bla")
        continue

    name_srl = re.findall(r'^[^,]+', line)[0]
    print(name_srl)
    data_count[name_srl] = data_count.get(name_srl,0) + 1
    print(data_count[name_srl])

file.close()