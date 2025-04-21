names = []
with open("FileIO.csv") as file:
    for line in file:
        name , location = line.rstrip().split(",")
        names.append({"name":name, "location":location})

def get_name(name):
    return name["name"]
for name in sorted(names, key=get_name):
    print(f"{name['name']} is in {name['location']}")

for name in sorted(names, key=lambda name:name["name"]):        #Same result, Lambda = Unnamed function (only 1 use)
    print(f"{name['name']} is in {name['location']}")

