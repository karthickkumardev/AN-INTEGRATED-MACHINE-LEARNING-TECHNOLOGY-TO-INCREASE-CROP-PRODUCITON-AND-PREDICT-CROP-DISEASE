from tkinter import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
def goBack():
    import ndsemi
def fun(value1,name1):
    root = Tk()

    canvas1 = Canvas(root, width=1000, height=50)
    canvas1.pack()
    label_0 = Label(root, text=name1, width=20, font=("chiller", 20))
    label_0.place(x=350, y=00)

    def insert_number():
        x1 = value1
        x2 = 100-x1
        x3 = 0

        figure1 = Figure(figsize=(5, 4), dpi=100)
        subplot1 = figure1.add_subplot(111)
        xAxis = [float(x1), float(x2), float(x3)]
        yAxis = [float(x1), float(x2), float(x3)]
        subplot1.bar(xAxis, yAxis, color='g')
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=0)

        figure2 = Figure(figsize=(5, 4), dpi=100)
        subplot2 = figure2.add_subplot(111)
        labels2 = 'Matched', 'NotMatched', ' '
        pieSizes = [float(x1), float(x2), float(x3)]
        explode2 = (0, 0.1, 0)
        subplot2.pie(pieSizes, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
        subplot2.axis('equal')
        pie2 = FigureCanvasTkAgg(figure2, root)
        pie2.get_tk_widget().pack()

    insert_number()

    button1 = Button(root, text='Submit', width=20, bg='brown', fg='white', command=goBack)
    button1.place(x=650, y=500)
    root.mainloop()