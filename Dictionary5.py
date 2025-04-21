names = [
    {"name": "John Doe", "location": "Main", "age": None},
    {"name": "Chen Daoxuan", "location": "Eastern", "age": "199,000 Years"},
    {"name": "Ken", "location": "Western", "age": 30},
    {"name": "Eiji", "location": "Eastern", "age": 20},
]          

locations = []
for name in names:
    if name["location"] not in locations:
        locations.append(name["location"])
for location in sorted(locations):
    print (location)

locations = set()                               #Listing the unlisted from the list, not listing if there is same as listed
for name in names:
    locations.add(name["location"])             #set() use .add() and .remove(), not .append() or .extend()
for location in sorted(locations):
    print (location)                            #Same result

name = [name["name"] for name in names if name["location"] == "Eastern"]    #List comprehension, same as the for loop above
for n in sorted(name):
    print (n)                                  

def location(n):
    return n["location"] == "Eastern"               #Function to filter names by location
name = filter(location, names)                      #Filter names with function location(n), being a new list
for name1 in sorted(name,key=lambda n: n["name"]):  #Sort name by name["name"]
    print(name1)              
