def is_even(x):
    return x % 2 == 0
x = int(input("Enter a number: "))
if is_even(x):
    print("Even")
else:
    print("Odd")

def is_odd(x):
    if x % 2 != 0:
        print ("Odd")
    else:
        print ("Even")
is_odd(int(input("Enter a number: ")))

name = input("Name: ").title().strip()
match name:
    case "John Doe" | "Ken" | "Absolute Grinder":
        print("Western")
    case "Chen Daoxuan" | "Eiji":
        print("Eastern")
    case _:
        print("Not registered")