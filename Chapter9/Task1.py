import csv

with open("file1.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")

    w.writerow(['один', "два", "три"])
    w.writerow(["четыре", "пять", "шесть"])

with open("file1.csv", "r", newline="") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
