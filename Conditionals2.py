def total_coins(gold, silver, bronze):
    return (gold*10 + silver)*10 + bronze

coins = [5,10,20]
print(*coins)                               #[5, 10, 20] being (5, 10, 20)      >> unpacking
print(total_coins(*coins))                  

coins2 = {"gold": 5, "bronze": 20, "silver": 10}
print(total_coins(**coins2))                #unpacking dictionary as required function      (Same result)

def main():
    username("John")
    username("John", "Doe", "Something")
    username("John", "Doe", "Something", "More", "And", "More")
    username2("John", "Doe", "Something", "More", "And", "More")
    username3("John", "Doe", "Something", "More", "And", "More")


def username(*names):                               #Unpacking tuple arguments or list arguments, **... for dictionary arguments
    uppercased = []
    for name in names:
        uppercased.append(name.upper())
    print(*uppercased)

def username2(*names):
    uppercased = map(str.upper, names)              #Using map function to apply str.upper to each name in names
    print(*uppercased)                              #Same result

def username3(*names):
    uppercased = [name.upper() for name in names]   #Using list comprehension to create a new list with uppercased names
    print(*uppercased)                              #Same result

main()