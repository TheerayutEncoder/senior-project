def open_txt_file(n=0):
    point_x, point_y = [], []
    with open('webplot_red_110.txt', 'r') as f:
        data_point = f.readlines()
        step = (len(data_point) // n) - 1
        for i in range(0, len(data_point), step):
            point_x.append(float(data_point[i].split()[0]))
            point_y.append(float(data_point[i].split()[1]))
    trap = trapezoid(point_x, point_y)
    simp = simp13(point_x, point_y)
    print("%.5f\t%.5f" % (abs(trap), abs(simp)))


def trapezoid(data_x, data_y):
    answer = 0.0
    for i in range(len(data_x) - 1):
        area = 0.5 * (data_x[i + 1] - data_x[i]) * (data_y[i + 1] + data_y[i])
        answer += area
    return answer


def simp13(data_x, data_y):
    answer = 0.0
    for i in range(0, len(data_x) - 2, 2):
        area = (data_x[i+2]-data_x[i]) * (data_y[i]+4*data_y[i+1]+data_y[i+2])/6
        answer += area

    return answer


# i = 0
# while i <= 40:
#     i += 2
#     open_txt_file(i)
open_txt_file(14)



