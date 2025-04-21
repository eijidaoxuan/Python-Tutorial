import csv
names_0 = []
with open("FileIO0.csv") as file:
    reader = csv.reader(file)
    for name,location in reader:                            #Can without first line csv
        names_0.append({"name":name,"location":location})

for name in sorted(names_0, key=lambda name:name["name"]):
    print(f"{name["name"]} is in {name["location"]}")                       #Same result

names_1 = []
with open("FileIO1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:                                      #make dictionary from every line csv    (Need first line)
        names_1.append({"name":row["Name"], "location":row["Location"]})

for name in sorted(names_1, key=lambda name:name["name"]):
    print(f"{name["name"]} is in {name["location"]}")                       #Same result

names_2 = []
with open("FileIO1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:                                      #Each line was a dictionary             (Need first line)
        names_2.append(row)

for name in sorted(names_2, key=lambda name:name["Name"]):
    print(f"{name["Name"]} is in {name["Location"]}")                       #Same result
