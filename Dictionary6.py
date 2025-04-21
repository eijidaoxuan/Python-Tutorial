names = [
    {"name": "John Doe", "location": "Main", "age": None},
    {"name": "Chen Daoxuan", "location": "Eastern", "age": "199,000 Years"},
    {"name": "Ken", "location": "Western", "age": 30},
    {"name": "Eiji", "location": "Eastern", "age": 20},
]       
worlds = []
for name in names:
    worlds.append({"name": name["name"], "location": name["location"]}) 
print(worlds)                        

worlds1 = [{"name":name["name"], "location":name["location"]} for name in names]
print(worlds1)                                                                      #Same result

world2 = {name["name"]:name["location"] for name in names}
print(world2)                                                                

for i, name in enumerate(names, start=1):         
    print(i, name)                                                     
for i in range(len(names)):                                
    print(i+1, names[i])                    #Same result