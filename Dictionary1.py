characters = {
        "John Doe" : "Western",
        "Chen Daoxuan" : "Eastern",
        "Ken" : "Western",
        "Eiji" : "Eastern",
}
print(f"Welcome in the upper realm!\nHere is your character list:\n")
for name, region in characters.items():
    print(f"{name} from {region} region")
print(" ")
while len(characters) > 0:
    character = input("Please choose your character!\n").title().strip()
    if character in characters.keys():
        region = characters.pop(character)
        print(f"Welcome, {character}!\n{region} region will be your start point.\n")
    else:
        print("Sorry, your character is not in the list\n")
print("All characters have been choosen\nThanks for playing!")