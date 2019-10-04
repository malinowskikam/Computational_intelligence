import csv
import statistics
import random

#b
with open("osoby.csv") as f:
    reader = csv.reader(f, "excel", delimiter=",")
    for row in reader:
        print(" | ".join(row))

#c
with open("osoby.csv") as f:
    print()
    reader = csv.reader(f, "excel", delimiter=",")
    next(reader)
    for row in reader:
        print(row[1])

#d
with open("osoby.csv") as f:
    print()
    reader = csv.reader(f, "excel", delimiter=",")
    next(reader)

    for row in reader:
        if row[2] == "k":
            print(" | ".join(row))

#e
with open("osoby.csv") as f1, open("osoby2.csv", "w") as f2 :
    print()

    writer = csv.writer(f2, "excel", delimiter=",")
    reader = csv.reader(f1, "excel", delimiter=",")
    next(reader)

    for row in reader:
        if row[2] == "m" and int(row[3]) > 50:
            print(" | ".join(row))
            writer.writerow(row)

#f
with open("osoby.csv") as f:
    print()
    reader = csv.reader(open("osoby.csv", newline=''), "excel", delimiter=",")
    ages = []
    next(reader)

    for row in reader:
        ages.append(int(row[3]))

    print("Avg age: " + str(statistics.mean(ages)))

#g/h
with open("osoby.csv") as f1, open("osoby3.csv", "w") as f2 :
    writer = csv.writer(f2, "excel", delimiter=",")
    reader = csv.reader(f1, "excel", delimiter=",")

    row = next(reader)
    row.append("wyplata")
    writer.writerow(row)

    for row in reader:
        row.append(random.randint(2000, 5000))
        writer.writerow(row)

    row = ["Jan", "Kowalski", "m", "30", "3000"]
    writer.writerow(row)

#i
with open("osoby3.csv") as f:
    print()
    reader = csv.reader(f, "excel", delimiter=",")
    for row in reader:
        print(" | ".join(row))
