from tkinter import *
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter.messagebox


root = Tk()
root.geometry('400x400')
root.title("crop selector")


def choose1():
    import ndsemi
    
def choose2():
    import disease
    
label_0 = Label(root, text="Agriculture", width=20, font=("bold", 20))
label_0.place(x=10, y=53)

button1=Button(root, text='Crop prediction', width=20, bg='brown', fg='white',command=choose1)
button1.place(x=100, y=200)

button1=Button(root, text='Disease prediction', width=20, bg='brown', fg='white',command=choose2)
button1.place(x=100, y=300)
root.mainloop()
