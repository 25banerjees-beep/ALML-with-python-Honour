import csv
print("1. Dispaly\n2. Write\n3. Search\n4. Quit")
a = input()
while(a!="4"):
    if a=="1":
        with open("data.txt","r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) ! = 0:
                    print(row)
        csvfile.cloase()
        a = input("Next Option")
    if a ="2":
       name = input("Enter name")
       surname = input("Enter surname")
       gender = input("Enter gender")
       s1 = input("Enter Score 1")
       s2 = input("Enter Score 2")
       s3 = input("Enter Score 3")
       with open("data.txt","a") as csvfile:
            reader = csv.reader(csvfile)
            reader.writerow([name, surname, gender, s1, s2, s3])
            csvfile.cloase()
            a = input("Next Option")
    if a ="3":
        with open("data.txt","r") as csvfile:
            searchitem = input("Enter item to be search\n")
            reader = csv.reader(csvfile)
                        for row in reader:
                            if len(row) ! = 0:
                                print(row)
                    csvfile.cloase()
                    a = input("Next Option")
