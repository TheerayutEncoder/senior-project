import csv
import time

x, y = [], []
"""
==============================
no need to use this CSV file anymore
==============================
"""
# with open('TEK0003.CSV') as file:
#     reader_file = csv.reader(file)
#     for row in reader_file:
#         x.append(float(row[3]))
#         y.append(float(row[4]))

"""
==============================
use only file .txt
==============================
"""
with open('TEK0000.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))


def open_txt_file(n=0):
    point_x, point_y = [], []
    with open('image_blue_550.txt', 'r') as f:
        data_point = f.readlines()
        step = len(data_point) // n
        for i in range(0, len(data_point), step):
            point_x.append(float(data_point[i].split()[0]))
            point_y.append(float(data_point[i].split()[1]))
    trap = trapezoid(point_x, point_y)
    simp = simpsons(point_x, point_y)
    print("%.6f\t%.6f" % (abs(trap), abs(simp)))


def trapezoid(data_x, data_y):
    answer = 0.0
    for i in range(len(data_x) - 1):
        area = 0.5 * (data_x[i + 1] - data_x[i]) * (data_y[i + 1] + data_y[i])
        answer += area
    return answer


def simpsons(data_x, data_y):
    answer = 0.0
    dx = (data_x[-1] - data_x[0]) / (len(data_x) - 1)
    for i in range(1, len(data_x) - 1):
        if i % 2 == 0:
            area = 2 * data_y[i]
        else:
            area = 4 * data_y[i]
        answer += area
    answer += data_y[0] + data_y[-1]
    answer = dx * answer / 3
    return answer


# start_time = time.time()
# trap = trapezoid(x, y)
# end_time = time.time()
# print('Trapezoid %f\t times %.10f seconds' % (trap, end_time - start_time))
#
# start_time = time.time()
# simp = simpsons(x, y)
# end_time = time.time()
# print('Simpson %f\t times %.10f seconds' % (simp, end_time - start_time))


i = 0
while i <= 40:
    i += 2
    open_txt_file(i)


