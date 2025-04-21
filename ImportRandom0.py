import random
names = ["John Doe",
        "Chen Daoxuan",
        "Ken",
        "Eiji"
]
def main():
    print(random.choice(names))
    print(random.choices(names, k=4))       #Just choosing item
    print(random.sample(names, k=4))        #Taking item after choosing

    print(random.choices(names, weights=[5,25,50,100], k=4))     #Chance = 5:25:50:100

    random.seed(0)              #Random result without chance (Same seed = Same result)
    print(random.choices(names, k=4))
    print(random.sample(names, k=4))

if __name__ == "__main__":
    main()