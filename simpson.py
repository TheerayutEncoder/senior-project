import csv

x, y = [], []
with open('TEK0000.CSV') as file:
    reader_file = csv.reader(file)
    for row in reader_file:
        print(row)
        x.append(float(row[3]))
        y.append(float(row[4]))


