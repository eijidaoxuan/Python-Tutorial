class Character:
    def __init__(self, name, level):
        if not name:
            raise ValueError("Missing name")        #Check if name is not empty only at creating object
        if level < 1:
            raise ValueError("Level must be at least 1")    #Check if level is not less than 1 only at creating object
        self.name = name
        self.level = level
        print(f"Character {self.name} successfully created at level {self.level}")

class Player(Character):                            #Player is a child class of Character so must have same or more constructor as parent class
    def __init__(self, name, location, level=1):
        super().__init__(name, level)               #Call the constructor of the parent(Character class)
        self.location = location  
    def __str__(self):
        return f"Player '{self.name}' spawned at level {self.level} in {self.location}"
    def cooldown(self, duration_per_level):
        return self.level * duration_per_level      #Cooldown time based on the player's level
    
class Enemy(Character):                             #Enemy is a child class of Character so must have same or more constructor as parent class
    def __init__(self, name, location, level=1):
        super().__init__(name, level)               #Call the constructor of the parent(Character class)
        self.location = location
    def __str__(self):
        return f"Enemy '{self.name}' spawned at level {self.level} in {self.location}"

class Demonking():
    base_level = 3                       
    def __init__(self, name):                       
        self.name = name                  
        self.level = Demonking.kill() 
    def __str__(self):
        return f"Demonking '{self.name}' spawned at level {self.level}"

    @classmethod
    def kill(cls, players=None):
        level = cls.base_level
        if not players:
            pass
        else:
            for player in players:
                if "Hero" in player.name:
                    level += player.level*2
                else:
                    level += player.level
        return level
    
    @classmethod
    def kill_nothing(cls,level):
        demonking=Demonking("Demon King of Darkness")
        demonking.level = level
        return demonking


def main():
    player1 = Player("Hero", "Forest", 5)           #Eror if  Player("","Forest", 5) or Player(None,"Forest",0)
    print(player1)
    player2 = Player(name="Warrior", level=3, location="Castle")    #Same result
    print(player2)
    enemy = Enemy("Goblin", "Cave")                 #Create an enemy with default level 1
    print(enemy)
    character = Character("Villager", 1)            #Create a character if you want to test the Character class
    
    players = [player1, player2, Player("Mage", "Tower", 2), Player(name="Thief", location="Dungeon", level=4)]
    for player in players:
        print(f"Player name: {player.name}, location: {player.location}, level: {player.level}")
    for player in players:
        print(f"{player.cooldown(10)} minutes left until {player}")   
    
    demonking = Demonking(name="Demon King of Madness")  
    print(demonking)
    print(f"Demon King of Madness level: {demonking.kill([player1, player2])}")

    print(f"{Demonking.kill_nothing(10)}")

if __name__=="__main__":
    main()