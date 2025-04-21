names = [
        "john doe",
        " Chen daoxuan",
        "ken   ",
        "  Eiji  ",
]

for name in names:
    print(name.title().strip())
print(', '.join(names))

for n in range(len(names)):
    print (n + 1, names[n].title().strip())

names = {
        "John Doe" : "Western",
        "Chen Daoxuan" : "Eastern",
        "Ken" : "Western",
        "Eiji" : "Eastern",
}
for name in names:
    print(name, names[name])
for name in range(len(names)):
    print(name + 1, list(names.keys())[name], list(names.values())[name])

names = [
    {"name": "John Doe", "location": "Western", "age": None},
    {"name": "Chen Daoxuan", "location": "Eastern", "age": "199,000 Years"},
    {"name": "Ken", "location": "Western", "age": 30},
    {"name": "Eiji", "location": "Eastern", "age": 20},
]
for identity in names:
    print(identity["name"], identity["location"], identity["age"], sep=", ")
for identity in range(len(names)):
    print(identity + 1, names[identity]["name"], names[identity]["location"], names[identity]["age"], sep=", ")

