import csv
import time

start_time = time.time()
x, y = [], []
# with open('TEK0000.CSV') as file:
#     reader_file = csv.reader(file)
#     for row in reader_file:
#         x.append(float(row[3]))
#         y.append(float(row[4]))

with open('test.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

answer = 0.0
dx = (x[-1]-x[0])/(len(x) - 1)
for i in range(1, len(x)-2):
    if i % 2 == 0:
        area = 2*y[i]
    else:
        area = 4*y[i]
    answer += abs(area)
answer += y[0] + y[-1]
answer = dx*answer/3

end_time = time.time() - start_time
print(answer)
print(answer/2)
print("%.10f second" % end_time)

