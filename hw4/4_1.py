# DEVELOPED BY IRYNA HRYTSENKO
#  open
file_name = input("Enter a file name:")
try:
    file = open(file_name, "r")
except:
    print("ERRORE: incorrect file name was recieved!")
    exit()


# go throght file and get emals into list:

#   short-code:
# emails = [line.split()[1] for line in file if line.startswith("From ")]
# print(emails)

emails = list()
for line in file:
    if line.startswith("From "):
        emails.append(line.split()[1])
file.close()


# print(emails)
# print(len(emails))
# print(sorted(emails))

for email in sorted(emails): print(email)
print("There were " + str(len(emails)) + " lines in the file with From as the first word")