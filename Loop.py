def main():
    print_square(int(input("Size: ")))
    print_simple_triangle1(int(input("Size: ")))
    print_simple_triangle2(int(input("Size: ")))
    print_triangle(int(input("Top: ")), int(input("Bottom: ")), int(input("Interval: ")))

def print_square(x):
    for _ in range(x):
        print("#"*x)

def print_simple_triangle1(x):
    for _ in range(x):
        print("#"*x)
        x -= 1
        
def print_simple_triangle2(x):
    for _ in range(x):
        print("#"*(_+1))

def print_triangle(x, y, z):
    if x != y and z != 0:
        while x < y and z != 0:
            print("#"*x)
            x += z
        while x > y and z != 0:
            print("#"*x)
            x -= z
    elif x == y:
        print("#"*x)
    else:
        print("Invalid input")

        
main()

#Prints rectangle
x = input("What to print: ")
y = int(input("Vertical: "))
z = int(input("Horizontal: "))
for _ in range(y):
    print(x*z)

for _ in range(-10, 11): 
    print(_)