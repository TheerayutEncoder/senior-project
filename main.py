import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

window = tk.Tk()
window.title("TrackGraph")
window.attributes("-fullscreen", True)
# window.geometry("%dx%d" % (800, 600))

# draw:list[object] is a list that keep dot
draw = []
coordinate = []
axis_x = []
axis_y = []
co_real_x = []
co_real_y = []


def set_x():
    axis_x.append(float(x_min.get()))
    axis_x.append(float(x_max.get()))
    clear()
    frame1.destroy()
    print(axis_x)


def set_axisx():
    global frame1
    frame1 = tk.Tk()
    frame1.title("Set x axis")
    frame1.geometry("250x150")

    pixel_unit = Label(frame1, text="Pixel units")
    pixel_unit.grid(padx=15, pady=15, column=2, row=1)
    real_unit = Label(frame1, text="Times (s)")
    real_unit.grid(padx=15, pady=15, column=3, row=1)
    lbl1 = Label(frame1, text="x min :")
    lbl1.grid(column=1, row=2)
    lbl2 = Label(frame1, text="x max :")
    lbl2.grid(column=1, row=3)
    global x_min, x_max
    x_min = Entry(frame1, width=10)
    x_min.grid(column=3, row=2)
    x_max = Entry(frame1, width=10)
    x_max.grid(column=3, row=3)

    global coordinate, axis_x
    if len(coordinate) != 0:
        for item in coordinate:
            axis_x.append(item[0])
        axis_x.sort()
        lbx_min = Label(frame1, text=coordinate[0][0])
        lbx_min.grid(column=2, row=2)
        lbx_max = Label(frame1, text=coordinate[1][0])
        lbx_max.grid(column=2, row=3)

    ok_button = Button(frame1, text="Ok", width=10, command=set_x)
    ok_button.grid(pady=20, column=2, row=4)

    frame1.mainloop()


def set_y():
    axis_y.append(float(y_min.get()))
    axis_y.append(float(y_max.get()))
    clear()
    frame2.destroy()
    print(axis_y)


def set_axisy():
    global frame2
    frame2 = tk.Tk()
    frame2.title("Set y axis")
    frame2.geometry("250x150")

    pixel_unit = Label(frame2, text="Pixel units")
    pixel_unit.grid(padx=15, pady=15, column=2, row=1)
    real_unit = Label(frame2, text="emf (V)")
    real_unit.grid(padx=15, pady=15, column=3, row=1)
    lbl1 = Label(frame2, text="y min :")
    lbl1.grid(column=1, row=2)
    lbl2 = Label(frame2, text="y max :")
    lbl2.grid(column=1, row=3)
    global y_min, y_max
    y_min = Entry(frame2, width=10)
    y_min.grid(column=3, row=2)
    y_max = Entry(frame2, width=10)
    y_max.grid(column=3, row=3)

    global coordinate, axis_y
    if len(coordinate) != 0:
        for item in coordinate:
            axis_y.append(item[1])
        axis_y.sort(reverse=True)
        lbx_min = Label(frame2, text=axis_y[0])
        lbx_min.grid(column=2, row=2)
        lbx_max = Label(frame2, text=axis_y[1])
        lbx_max.grid(column=2, row=3)

    ok_button = Button(frame2, text="Ok", width=10, command=set_y)
    ok_button.grid(pady=20, column=2, row=4)

    frame2.mainloop()


def scaling():
    global co_real_x, co_real_y, axis_x, axis_y
    for item in coordinate:
        x = axis_x[2] + (item[0] - axis_x[0]) * ((axis_x[3] - axis_x[2]) / (axis_x[1] - axis_x[0]))
        y = axis_y[2] + (item[1] - axis_y[0]) * ((axis_y[3] - axis_y[2]) / (axis_y[1] - axis_y[0]))
        co_real_x.append(x)
        co_real_y.append(y)
    for i in range(len(co_real_x)):
        print("%f\t%f" % (co_real_x[i], co_real_y[i]))
    axis_x.clear()
    axis_y.clear()


def clear():
    for item in draw:
        canvas.delete(item)
    coordinate.clear()
    co_real_x.clear()
    co_real_y.clear()


def save_coor():
    files = [('All Files', '*.*'),
             ('Text Document', '*.txt')]

    file = asksaveasfile(filetypes=files, initialfile="Untitled", defaultextension=".txt")
    try:
        with open(file.name, 'w') as f:
            for i in range(len(co_real_x)):
                f.writelines(f"{co_real_x[i]}\t{co_real_y[i]}\n")

        """
        =====================================
        Use this code if you want to write CSV file instead of text file
        But trust need you dont need to try it
        =====================================
        
        with open('data.csv', 'w', encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            header = ['x', 'y']
            writer.writerow(header)
            for i in range(len(co_real_x)):
                data = (co_real_x[i], co_real_y[i])
                writer.writerow(data)
        """
    except AttributeError:
        return


# def plot_graph():
#     data = {}
#     if len(co_real_x) != 0:
#         data['Times(ms)'] = co_real_x
#         data['emf(V)'] = co_real_y
#
#         df = pd.DataFrame(data, columns=['Times(ms)', 'emf(V)'])
#         print(df)
#         frame3 = Tk()
#         frame3.title("Graph from tracking")
#
#         figure = plt.Figure(figsize=(6, 5), dpi=100)
#         ax = figure.add_subplot(111)
#         line = FigureCanvasTkAgg(figure, frame3)
#         line.get_tk_widget().pack()
#         df = df[['Times(ms)', 'emf(V)']].groupby('Times(ms)').sum()
#         df.plot(kind='line', legend=True, ax=ax, color='r', marker='', fontsize=10, grid=True)
#         ax.set_title('emf vs times')
#
#         frame3.mainloop()


def calculate_area():
    global co_real_x, co_real_y
    answer = 0.0
    for i in range(len(co_real_x) - 2):
        area = 0.5 * (co_real_x[i + 1] - co_real_x[i]) * (co_real_y[i + 1] + co_real_y[i])
        answer += area

    answer = abs(answer)

    frame4 = Tk()
    frame4.geometry("450x300")
    result = Label(frame4, text="Area under curve (Vs) = %.6f" % answer, font=('Arial', 20))
    result.pack(pady=25)

    lb1 = Label(frame4, text="Enter the number of coil turn", font=('Arial', 16))
    lb1.pack()

    n_coils = Entry(frame4, width=10)
    n_coils.pack()

    flux_lb = Label(frame4, text="Magnetic flux : 0 Wb")
    flux_lb.pack()

    def cal_flux():
        try:
            n = int(n_coils.get())
        except ValueError:
            n = 0
        if n != 0:
            flux_lb.config(text="Magnetic flux : %.6f Wb" % (answer / n))

    button_cal = Button(frame4, text='Calculate magnetic flux', command=cal_flux)
    button_cal.pack()

    frame4.mainloop()


def about():
    frame_about = Tk()
    frame_about.geometry("400x250")
    frame_about.title("About me")

    name_lb = Label(frame_about, text="Hi, I'm Top Theerayut.\nThis is TrackGraph program.\n"
                                      "For magnetic flux determination from EMF graph.")
    name_lb.pack(pady=50)

    contact = Label(frame_about, text="Contact me: Theerayutattajak@gmail.com")
    contact.pack()


menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar)
# plot_menu = Menu(menubar)
help_menu = Menu(menubar)
edit_menu = Menu(menubar)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
# menubar.add_cascade(label="Plot", menu=plot_menu)
menubar.add_cascade(label="Help", menu=help_menu)

file_menu.add_command(label='Save', command=save_coor)
file_menu.add_command(label='Exit', command=window.destroy)

edit_menu.add_command(label="set axis x", command=set_axisx)
edit_menu.add_command(label="set axis y", command=set_axisy)
edit_menu.add_command(label="scaling", command=scaling)
edit_menu.add_command(label="calculate magnetic flux", command=calculate_area)
edit_menu.add_command(label="clear", command=clear)
help_menu.add_command(label="About me", command=about)

# plot_menu.add_command(label="Plot graph", command=plot_graph)

img2 = (Image.open("data/img/background.jpg"))
resize_img2 = img2.resize((1920, 1080), Image.ANTIALIAS)
new_img2 = ImageTk.PhotoImage(resize_img2)


def file_name():
    filetypes = (
        ('text files', '*.jpg'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    if filename != "":
        select_label.config(text=filename)
        global img2, resize_img2, new_img2
        img2 = (Image.open(filename))
        # resize_img2 = img2.resize((1069, 700), Image.ANTIALIAS)
        # new_img2 = ImageTk.PhotoImage(resize_img2)
        new_img2 = ImageTk.PhotoImage(img2)

    canvas.bind('<Button-1>', draw_dot)


def insert_image():
    canvas.itemconfig(work_space, image=new_img2)


def draw_dot(event):
    x1 = event.x
    y1 = event.y
    x2 = event.x
    y2 = event.y
    global draw
    draw.append(canvas.create_oval(x1, y1, x2, y2, width=5))
    xy = (x1, y1)
    global coordinate
    coordinate.append(xy)


select_button = tk.Button(text='Select img file', font=25, command=file_name)
select_button.pack(pady=10)

select_label = Label(text="Not select any file.")
select_label.pack()

insert_button = tk.Button(text='insert image (only JPG)', font=25, command=insert_image)
insert_button.pack(pady=10)

canvas = Canvas(width=1920, height=1080, bg="white")
img = ImageTk.PhotoImage(Image.open("background.jpg"))
work_space = canvas.create_image(760, 350, image=img)
canvas.pack()

window.mainloop()
