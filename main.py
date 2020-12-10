import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math
import time
import sys


def graph_func():
    text = e1.get()
    string = bytes([ord(i) for i in text])
    if 'x' not in str(string):
        r1.grid_forget()
        r2.grid_forget()
        ran1.grid_forget()
        ran2.grid_forget()
        graph1.grid_forget()
        rez.config(text=f"{eval(string)}", bg='gray', fg='white')
        rez.grid(row=3, column=1)
    else:
        if rez != "":
            rez.grid_forget()
        r1.grid(row=2, column=0)
        r2.grid(row=2, column=2)
        graph1.grid(row=5, column=0)
        ran1.grid(row=1, column=0)
        ran2.grid(row=1, column=2)


def graph():
    text = e1.get()
    string = bytes([ord(i) for i in text])
    if 'x' in str(string):
        v1 = float(eval(bytes([ord(i) for i in r1.get()])))
        v2 = float(eval(bytes([ord(i) for i in r2.get()])))
        x1 = np.arange(v1, v2, 0.0001)
        if "tan" in str(string) and "arctan" not in str(string):
            y1 = [0]*len(x1)
            for el in range(len(x1)):
                if abs(np.cos(x1[el])) > 0.01:
                    y1[el] = np.tan(x1[el])
                else:
                    y1[el] = np.nan
        elif '/' in str(string):
            y1 = [0] * len(x1)
            for el in range(len(x1)):
                x = x1[el]
                t1 = eval(string)
                if abs(t1) < 10001:
                    y1[el] = t1
                else:
                    y1[el] = np.nan

        elif "tan" in str(string) and "arctan" in str(string):
            y1 = [0] * len(x1)
            for el in range(len(x1)):
                x = x1[el]
                t1 = eval(string)
                if abs(t1) < 2000:
                    y1[el] = t1
                else:
                    y1[el] = np.nan
        else:
            y1 = [eval(string) for x in x1]

        plt.plot(x1, y1, linewidth=3)
        plt.grid()
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.plot(0, 0, marker="o", markersize=5, color="k")
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.show()
    else:
        print("Invalid input")


def quit1():
    sys.exit(0)


window = tk.Tk()
p1 = tk.PhotoImage(file="img_1.png")
window.title("Graph Your Function!")
window.iconphoto(False, p1)
write_function = tk.Label(text="Write your function/math expression below:", bg='gray', fg='white')
math_expr = ""
x_values = []
y_values = []
e1 = tk.Entry(window)
r1 = tk.Entry(window)
r2 = tk.Entry(window)
ran1 = tk.Label(text="Range 1", bg='gray', fg='white')
ran2 = tk.Label(text="Range 2", bg='gray', fg='white')
rez = tk.Label(text="", bg='gray', fg='white')
graph1 = tk.Button(window, text="Graph it!", command=graph)
graph_it = tk.Button(window, text="Solve it!", command=graph_func)
quit_it = tk.Button(window, text="Quit", command=quit1)
write_function.grid(row=0, column=1)
e1.grid(row=1, column=1)
graph_it.grid(row=5, column=1)
quit_it.grid(row=5, column=2)
window.mainloop()
