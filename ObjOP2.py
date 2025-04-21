class Vault:
    def __init__(self):
        self._balance = 0           #If all using .balance, property cant change .balance to _balance
    def deposit(self, x):
        self._balance += x
    def withdraw(self, x):
        self._balance -= x
    @property                       #_balance to use property, but cant print(self.balance = ...) without setter
    def balance(self):
        return self._balance        #if return self.balance, it will looping

class Vault2:
    balance = 0
    def deposit(self, x):
        self.balance += x
    def withdraw(self, x):
        self.balance -= x
    def __str__(self):
        return f"{self.balance}"    #Cant return int
    
balance = 0

def main():
    deposit(100)
    withdraw(50)
    print(balance) 
    money = Vault()
    money.deposit(100)
    money.withdraw(50)
    print(money.balance)                            #Same result
    money2 = Vault2()
    money2.deposit(100)
    money2.withdraw(50)
    print(money2)                                   #Same result

def deposit(x):
    global balance
    balance += x

def withdraw(x):
    global balance
    balance -= x

main()