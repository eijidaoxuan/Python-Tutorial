import csv
ages = {"John Doe":"None", "Chen Daoxuan":"199,000 Years", "Ken":"30 Years", "Eiji":"20 Years"}

def main():
    with open("FileIO1.csv") as file, open ("FileIO3.csv", "w", newline="") as file2:
        reader = csv.reader(file)
        writer = csv.DictWriter(file2, fieldnames = ["Name", "Location", "Age"])        #or fieldnames = ["Name", "Location", "Age"]
        writer.writeheader()                                                            #write fieldnames in FileIO3.csv
        next(reader)                                                        #skip header in FileIO1.csv     
        for row in reader:                                                              #row = line
            writer.writerow(
                {"Name":row[0], "Location":row[1], "Age":ages.get(row[0])}              #.get() is used to avoid KeyError if the key is not found in the dictionary
            )
    
    with open("FileIO1.csv") as file, open ("FileIO3.csv", "w", newline="") as file2:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(file2, fieldnames = reader.fieldnames + ["Age"])        #or fieldnames = ["Name", "Location", "Age"]
        writer.writeheader()                                                            #write fieldnames in FileIO3.csv
        for row in reader:                                                              #row = line
            writer.writerow(
                {"Name":row["Name"], "Location":row["Location"], "Age":ages[row["Name"]]} 
            )
        for row in reader:
            row["Age"] = ages[row["Name"]]
            writer.writerow(row)                                                        #Same result
            
main()
