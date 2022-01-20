from tkinter import *
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter.messagebox


root = Tk()
root.geometry('850x800')
root.title("crop selector")

pH = DoubleVar()
temp = IntVar()
var = IntVar()
c = StringVar()
c1 = StringVar()
var1 = IntVar()
value1=0
name1="noname"


def doNothing() :

    canvas= Canvas(root,width = 2000,height = 1000)
    canvas.pack()

    label_0 = Label(root, text="CROP SELECTOR", width=20, font=("bold", 20))
    label_0.place(x=310, y=53)

    csv.register_dialect('myDialect',delimiter=',',skipinitialspace=True)
    count=0
    posi=0
    t=0
    maxx=0
    with open('crops.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            t=0
            if((row[1]<entry_2.get()) and (row[2]>entry_2.get())):
                t=t+1
            if((var1.get()==1 and row[5]=='food')or(var2.get()==1 and row[5]=='cash')or(var3.get()==1 and row[5]=='plantation')):
                t=t+1
            if((var.get()==1 and row[6]=='summer')or(var.get()==2 and row[6]=='rainy')or(var.get()==3 and row[6]=='winter')):
                t=t+1
            if((row[3]<entry_1.get()) and (row[4]>entry_1.get())):
                t=t+1
            if(row[8]==droplist1):
                t=t+1
            if((row[7]<entry_9.get()) and (row[8]>entry_9.get())):
                t=t+1
            if(t>maxx):
                if((var1.get()==1 and row[5]=='food')or(var2.get()==1 and row[5]=='cash')or(var3.get()==1 and row[5]=='plantation')):
                    maxx=t
                    posi=count
            print(t)
            count=count+1
    k=0
    with open('crops.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            if(k==posi):
                name1=row[0]
                value1=maxx*100/6
            k=k+1
    csvFile.close()
    canvas.destroy()
    root.destroy()
    import extra
    extra.fun(value1,name1)
    return
def Check():
    if(var.get()==0 or ((var1.get()==var2.get()==var3.get()) and (not(var1.get()==1 or var2.get()==1 or var3.get()==1)))):
        import popup
        popup.popUp()
    else:
        doNothing()
    return

label_0 = Label(root, text="CROP SELECTOR", width=20, font=("bold", 20))
label_0.place(x=310, y=53)

label_1 = Label(root, text="pH", width=20, font=("bold", 10))
label_1.place(x=250, y=180)

entry_1 = Entry(root)
entry_1.place(x=440, y=180)

label_9 = Label(root, text="rainfall", width=20, font=("bold", 10))
label_9.place(x=250, y=440)

entry_9 = Entry(root)
entry_9.place(x=440, y=440)

label_2 = Label(root, text="temperature", width=20, font=("bold", 10))
label_2.place(x=250, y=130)

entry_2 = Entry(root)
entry_2.place(x=440, y=130)

label_3 = Label(root, text="weather", width=20, font=("bold", 10))
label_3.place(x=250, y=230)

radioButt_1 = Radiobutton(root, text="summer", padx=5, variable=var, value=1)
radioButt_1.place(x=430, y=230)
radioButt_2 = Radiobutton(root, text="rainy", padx=20, variable=var, value=2)
radioButt_2.place(x=505, y=230)
radioButt_3 = Radiobutton(root, text="winter", padx=35, variable=var, value=3)
radioButt_3.place(x=580, y=230)

label_4 = Label(root, text="state", width=20, font=("bold", 10))
label_4.place(x=250, y=280)

list1 = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh'
    ,'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
    'Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telengana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('select your state')
droplist.place(x=440, y=280)

label_8 = Label(root, text="type of soil", width=20, font=("bold", 10))
label_8.place(x=250, y=330)

list2 = ['Alluvial','Black','Loamy','Sandy']

droplist1 = OptionMenu(root, c1, *list2)
droplist1.config(width=15)
c1.set('select your soil')
droplist1.place(x=440, y=330)


var2 = IntVar()
var3 = IntVar()

label_5 = Label(root, text="type of crop", width=20, font=("bold", 10))
label_5.place(x=250, y=380)

check_1 = Checkbutton(root, text="food", variable=var1)
check_1.place(x=430, y=380)

check_2 = Checkbutton(root, text="cash", variable=var2)
check_2.place(x=505, y=380)

check_3 = Checkbutton(root, text="plantation", variable=var3)
check_3.place(x=580, y=380)

label_9 = Label(root, text="Average rainfall for year", width=20, font=("bold", 10))
label_9.place(x=250, y=500)
entry_9 = Entry(root)
entry_9.place(x=440, y=500)

button1=Button(root, text='Submit', width=20, bg='brown', fg='white',command=Check)
button1.place(x=650, y=600)
root.mainloop()
