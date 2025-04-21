name = input("Name: ")

with open("FileIO.txt", "w") as file:       #Write (reset) FileIO.txt
    file.write(f"{name}\n")

with open("FileIO.txt", "a") as file:       #Append FileIO.txt
    file.write(f"{name}\n")


with open("FileIO.txt", "r") as file:       #Read FileIO.txt    or  open("FileIO.txt")
    lines = file.readlines()                #each line being a list     lines[0] = first line, lines[3:10] = lines 3 to 10
for line in lines:                          #then file.writelines(lines)   #Write all lines at once to another file
    print(f"Welcome, {line.rstrip()}")

with open("FileIO.txt", "r") as file:       #Same result 
    for line in file:
        print(f"Welcome, {line.rstrip()}")
