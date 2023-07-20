import csv

answer = input("What you want to write down?\n")

with open("file1.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")

    w.writerow(answer)


with open("file1.csv", "r") as f:
    r = csv.reader(f, delimiter=",")

    for row in r:
        print(" ".join(row))
        