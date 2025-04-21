import random
x = random.choice(["Truth", "Dare", "Nothing"]) #Chance(50:50, 33:33:33, 25:25:25:25)
print(x)
from random import choice
x = choice(["Truth", "Dare", "Nothing"])
print(x)

a = random.randint(0, 10) #Random number (same chance)
print(a)

choices = ["Truth", "Dare", "Nothing"]
random.shuffle(choices) 
print (choices)

import statistics
b = statistics.mean([80,100,90]) 
print (b)

import sys
if len(sys.argv) < 2:
    print("Too few arguments")    #python Import.py "name"
elif sys.argv[1] == "Master":
    print("Welcome, Administrator") 
for arg in sys.argv[1:]:
    print(f"Welcome, {arg}")

