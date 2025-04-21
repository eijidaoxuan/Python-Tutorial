def meaw(x :int) -> None:                       #:int and -> None = hint (undetected from system)
    """Prints "meaw" x times."""                #Simple docstring
    for _ in range (x):
        print("meaw")

number :int = int(input("Enter a number: "))    #:int = hint
meaws :str = meaw(number)                       #:str = hint
print(meaws)  
print(meaw(number))                             #Same result

#Debugging meaw function
def meaw2(x :int) -> str:                       #:int and -> str = hint
    """
    Returns "meaw" x times.                                     #Docstring with description, parameters, return type, and example.                
    
    :param x: Number of times to print "meaw"
    :type x: int
    :raise ValueError: If x is not a positive integer.
    :return: String with "meaw" repeated x times.
    :rtype: str                                                 #return type = str
    :Example:
    >>> meaw(3)
    meaw
    meaw
    meaw
    """                
    return f"meaw\n" * x
print (meaw2(number).rstrip())
print (meaw2(number), end="")                   #Same result