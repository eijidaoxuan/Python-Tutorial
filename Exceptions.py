def main():
    if is_even() == True:
        print("Even")
    else:
        raise ValueError("Odd")                         #or raise Exception("Odd") > parent     or      raise BaseException("Odd") > grandparent

def is_even():
    while True:
        try:
            return int(input("Enter a number: ")) % 2 == 0
        except ValueError:
            print ("Invalid input. Please enter a number.")         #(pass) to continue with nothing
            
if __name__ == "__main__":
    main()