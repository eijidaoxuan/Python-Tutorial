
print("Hello", "John", "Doe", end="<>")         #variable.rstrip() = variable, end=""
print("Hello", "Vivy\nVlorite", 'Eye\'s')       #\n = new line    \" = "    \\ = \    \r = line start
print("Hello", "Chen", "Daoxuan", sep="...")

a = input("Greeting: ").capitalize()
if "Hello" in a:
    print("Hi")
print(len(a))

name = input("Name: ").capitalize()
print(name)
name_2 = input("Who? ").title().strip() #Input 2 words
print(name_2)

a,b = name_2.split()    #Split being a list     or      a = ... .split("...")   being   a[0] and a[1]
print(a)
print(b)

#Input cant decimal
a = int(input("Enter a number: "))
print (a)
#Input can decimal (. )
a = float(input("Enter a number: "))
print (a)

#input 100-300
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(round(a/b, 3))     #round to 3 decimal places
print(f"{a/b:.3f}")      #round to 3 decimal places
print(f"{a/b:.2%}")      #round to 2 decimal places and convert to percentage
print(f"{a/b:.2e}")      #round to 2 decimal places and convert to scientific notation
print(a//b)              #divide and round down to integer
c = a**b
print(f"{a**b:,}")
print(bin(c)[2:])           #number to binary   [2:] = remove 0b
print(int(bin(c)[2:],2))    #binary to number
print(hex(id(1)))           # 0x7f8c4c0a2b50

#Another Function
print(int(pow(2,3))) #2^3=8

#Another Function
while True:
    try:
        score = int(input("Enter score: "))
        if score < 0 or score > 100:
            print("Please enter a valid score")
        else:
            break
    except ValueError:
        print("Please enter a score")


if score >= 90: 
    print("Grade: A")
elif score >= 80:
    print(f"Grade: B")
elif score >= 70:
    print(f"Grade: C")
elif score >= 60:
    print(f"Grade: D")
else:
    print(f"Grade: E")


#Make function
def main():
    while True:
        try:
            score = int(input("Enter score: "))
            if score < 0 or score > 100:
                print("Please enter a valid score")
            else:
                print (f"Grade: {gradding(score)}")
                global name         #Input name from outside main function, then change it inside main function
                student(name)
                name = "John"
                student(name)
                break
        except ValueError:
            print("Please enter a score")

def gradding(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"
    
def student(name):
    print(name + "\'s grade")

if __name__ == "__main__":
    main()

