names = {
        "John Doe" : "Western",
        "Chen Daoxuan" : "Eastern",
        "Ken" : "Western",
        "Eiji" : "Eastern",
}
print (names["John Doe"])
print (f"""
===============================
|  Name  |      Location      |
John Doe is {names['John Doe']}
Chen Daoxuan is {names.get("Chen Daoxuan", "Not registered")}
Mr. Zombie is {names.get("Mr. Zombie", "Not registered")}
===============================
""")

names.update ({"Mr. Zombie" : "Main"})
print (f"""
===============================
|  Name  |      Location      |
Mr. Zombie is {names.get("Mr. Zombie", "Not registered")}
===============================
""")

for name in names.keys():
    print(f"{name} is stay in {names[name]}")
for region in names.values():
    print (f"{region} world in upper realm")
for name, region in names.items():
    print (f"{name} is stay in {region} world")