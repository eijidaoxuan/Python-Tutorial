names = input("Name: ").title().split()

name = " ".join(names)
if name:
    print(name)
else:
    print("Invalid name")

if name := " ".join(names):       #Same result (Walrus operator {:=})
    print(name)
else:
    print("Invalid name")


first_name, last_name = input("Name: ").title().split()

if first_name.startswith("Abs") and last_name.endswith("der"):
    print(f"Welcome {first_name} {last_name}")
elif first_name and last_name:
    print(first_name, last_name)
else:
    print("Invalid name")