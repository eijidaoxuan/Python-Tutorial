def main():             #To test function, function must return a value
    while True:
        try:
            x = float(input("Number: "))
            break
        except ValueError:
            print("Please enter a number")
    print(f"{x} squared is {square(x)}")

def square(x):
    if not isinstance(x, (int,float)):                          #function x == int or float
        raise TypeError ("Input must be an int or float")       #Error for square("String")     without float or int for input
    return x * x


if __name__ == "__main__":
    main()