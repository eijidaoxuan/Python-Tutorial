names = []
with open("FileIO.txt", "r") as file:       #Can change list from file
    for line in file:
        names.append(line.rstrip())
for name in sorted(names, reverse=True):    #Sorting a-z, delete reverse or reverse=False
    print(f"Welcome, {name}")

with open("FileIO.txt") as file:            #Same result, but cant change list from file
    for line in sorted(file, reverse=True):
        print(f"Welcome, {line.rstrip()}")
