import csv
import time

x, y = [], []

with open('TEK0000.CSV') as file:
    reader_file = csv.reader(file)
    for row in reader_file:
        x.append(float(row[3]))
        y.append(float(row[4]))

# with open('test.txt', 'r') as file:
#     data = file.readlines()
#     for line in data:
#         x.append(float(line.split()[0]))
#         y.append(float(line.split()[1]))


def trapezoid(data_x, data_y):
    answer = 0.0
    for i in range(len(data_x) - 2):
        area = 0.5 * (data_x[i + 1] - data_x[i]) * (data_y[i + 1] + data_y[i])
        answer += abs(area)
    return answer


def simpsons(data_x, data_y):
    answer = 0.0
    dx = (data_x[-1] - data_x[0]) / (len(data_x) - 1)
    for i in range(1, len(data_x) - 2):
        if i % 2 == 0:
            area = 2 * data_y[i]
        else:
            area = 4 * data_y[i]
        answer += abs(area)
    answer += data_y[0] + data_y[-1]
    answer = dx * answer / 3
    return answer


start_time = time.time()
trap = trapezoid(x, y)
end_time = time.time()
print('Trapezoid %f\t times %.10f seconds' % (trap, end_time - start_time))

start_time = time.time()
simps = simpsons(x, y)
end_time = time.time()
print('Simpson %f\t times %.10f seconds' % (simps, end_time - start_time))
