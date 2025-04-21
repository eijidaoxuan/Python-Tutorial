names1 = [
        "John Doe",
        "Chen Daoxuan",
        "Ken",
        "Eiji",
]                               #Can change with names[0]= "..."  or names[1]= "..."   or names[0:2] = ["...","..."]   
print(names1)
names1.sort()                    #or sorted(names) or or sorted(names, reverse=True)
print(names1)
names1.append("Mr. Zombie")
print(names1)
names1.remove("Ken")
print(names1)
names1.pop()
print(names1)
names1.extend(["Ken", "AG"])
print(names1)
names1.insert(0, "Absolute God")
print(names1)
names1.reverse()
print(names1)

names2 = {
        "John Doe" : "Western",
        "Chen Daoxuan" : "Eastern",
        "Ken" : "Western",
        "Eiji" : "Eastern",
}                                       #Can change with names["John Doe"]= "..."  or names["Chen Daoxuan"]= "..."   or names["Ken"]= "..."   or names["Eiji"]= "..."
print(names2)
names2.update ({"Ken" : "Main"})
print(names2)
names2.update ({"Mr. Zombie": "Main"})
print(names2)

names = [
    {"name": "John Doe", "location": "Western", "age": None},
    {"name": "Chen Daoxuan", "location": "Eastern", "age": "199,000 Years"},
    {"name": "Ken", "location": "Western", "age": 30},
    {"name": "Eiji", "location": "Eastern", "age": 20},
]                               #Can change with names[0]["name"]= "..."  or names[1]["location"]= "..."   or names[2]["age"]= "..."   or names[3]["name"]= "..."
print(names)
names[0].update({"location": "Main"})
names[2].update({"age": "200,000 Years"})
print(names)
