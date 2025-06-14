# DEVELOPED BY IRYNA HRYTSENKO
# open
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

domains = dict()
for line in file:
    if line.startswith("From "):
        email = line.split()[1]
        domain_name = email.split("@")[1]
        domains[domain_name] = domains.get(domain_name, 0) + 1
file.close()

# print dict as it is:
print(domains)

# sorting:
domains_list = list()
for k, v in domains.items():
    domains_list.append((k, v))
# print(sorted(domains_list))

# sorted printing
print("SORTED:")
for tuple in sorted(domains_list):
    print("{:>20} {:<1} {}".format(tuple[0], tuple[1], "*"*tuple[1]))