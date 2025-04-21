def main():             #To test function, function must return a value
    x = input("Name: ")
    print(greeting(x))

def greeting(x = "Master"):
    return f"Welcome, {x}"

if __name__ == "__main__":
    main()