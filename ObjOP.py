import random

class Name:                                         #Name = self(place) = something on the left side of the dot
    def __init__(self,name,region,age):             #or region=None being optional     or age=0 being optional
        #Here the sign error raised if without getter(property) and setter
        self.name = name
        self.region = region                        #self.region go to setter
        self.age = age
    
    def __str__(self):                              #for print(name) to work
        return f"{self.name} was in {self.region} region for {self.age} years"
    
    def condition(self):                            #for print(name.condition()) to work
        return f"How the condition in {self.region} region?"

    @classmethod
    def new_region(cls,name):
        return f"{name} new location will be in {random.choice(["Western", "Main", "Eastern"])} region"
    
    @classmethod
    def get(cls):                                   #cls = only class = something on the left side of the dot
        name = input("Name: ").capitalize()
        region = input("Region: ").capitalize()
        age = int(input("Age: "))
        return cls(name, region, age)               #if cls(name,region,age) = Name(name,region,age)    being class Name

    @property                                       #getter (gate for setter) or print(name.region)
    def region(self): 
        return self._region
    
    @region.setter                                  #All name.region go to setter and become self._region for checking
    def region(self, region):
        if region not in ["Western", "Main", "Eastern"]:
            raise ValueError("Unvalid region")      #sign if error, repair with try and except in main()
        self._region = region
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

def main():
    name = Name.get()                               #name = Name(name,region,age)
    print(name)
    print(name.condition()) 
    print(Name.new_region("Eiji"))                  #take a function from class Name without creating an object
    name._region = "..."                            #if name.region = "..." go to setter, will be error
    print(name)                             
    print("Main function executed")


if __name__=="__main__":
    main()