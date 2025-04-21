#Make a list
names = [
        "John Doe",
        "Chen Daoxuan",
        "Ken",
        "Eiji",
]
print(", ".join(names).lower())
name_lower = [name.lower() for name in names if len(name) > 3]
print (name_lower)
counts = {name: name_lower.count(name) for name in name_lower}
print(counts)

import random
number = [random.randint(0, 10) for i in range(3)]
print(f"Numbers: {number}")


#Get name (Perfect)
def main():
    print(input("Name: ").title().strip())      #Name input (1 word)
    x = get_name("Name: ")                      #Name input (1 or more words)
    print(x)

def get_name(x):
    names = input(x).split()
    return " ".join(name.capitalize() for name in names)        #name.title() if any number before name

if __name__ == "__main__":
    main()
