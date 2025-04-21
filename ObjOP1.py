class Vault:
    def __init__(self, gold=0,silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    def __str__(self):
        return f"Vault: {self.gold} gold, {self.silver} silver, {self.bronze} bronze"
    
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        bronze = self.bronze + other.bronze
        return Vault(gold, silver, bronze)
    
    def __sub__(self, other):
        gold = self.gold - other.gold
        silver = self.silver - other.silver
        bronze = self.bronze - other.bronze
        return Vault(gold, silver, bronze)
    
    def __mul__(self, other):
        gold = self.gold * other.gold
        silver = self.silver * other.silver
        bronze = self.bronze * other.bronze
        return Vault(gold, silver, bronze)
    
    def __truediv__(self, other):
        if other == 0:
            raise ValueError("Cannot divide by zero")
        gold = self.gold / other.gold
        silver = self.silver / other.silver
        bronze = self.bronze / other.bronze
        return Vault(gold, silver, bronze)
    
    def __floordiv__(self, other):
        if other == 0:
            raise ValueError("Cannot divide by zero")
        gold = self.gold // other.gold
        silver = self.silver // other.silver
        bronze = self.bronze // other.bronze
        return Vault(gold, silver, bronze)
    
    def __mod__(self, other):
        gold = self.gold % other
        silver = self.silver % other
        bronze = self.bronze % other
        return Vault(gold, silver, bronze)
    
    def __pow__(self, other):
        gold = self.gold ** other               #just other if other is a number
        silver = self.silver ** other
        bronze = self.bronze ** other
        return Vault(gold, silver, bronze)
    

def main():
    ken = Vault(100, 200, 300)
    print(ken)
    eiji = Vault(50, 100, 150)
    print(eiji)
    vault = ken + eiji - Vault(10, 20, 30) % 2
    print(vault)

if __name__=="__main__":
    main()