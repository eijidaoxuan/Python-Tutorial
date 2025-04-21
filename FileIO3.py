import csv

name = input("Name: ")
location = input("Location: ")

with open("FileIO2.csv", "a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,location])

with open("FileIO2.csv", "a",newline="") as file:
    writer = csv.DictWriter(file, fieldnames = ["Name","Location"])     #Output position depends on fieldnames
    writer.writerow({"Name": name, "Location": location})               #Same output