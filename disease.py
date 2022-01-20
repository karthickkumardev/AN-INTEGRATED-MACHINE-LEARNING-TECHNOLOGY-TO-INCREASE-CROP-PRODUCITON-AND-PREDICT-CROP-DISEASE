from tkinter import *  
from PIL import ImageTk,Image
import joblib
import tkinter.messagebox
from tkinter.filedialog import askopenfile

from keras.models import load_model
import cv2
import numpy as np
import random
i = random.randint(0,14)

root = Toplevel()  
canvas = Canvas(root, width = 350, height = 500)  
canvas.pack()  

def post():
    global img
    file = askopenfile(mode='r',filetypes = [('All files','*.*')])
    img = Image.open(file.name)
    imag = img.resize((200,200),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imag)
    canvas.create_image(20, 60, anchor=NW, image=img)

def svm():
    global img
    model = load_model('model_squeeze.h5')
    img = np.full((100,80,3), 12, dtype = np.uint8)
    img = cv2.resize(img,(256,256))
    img = np.reshape(img,[1,256,256,3])
    # classes = model.predict_classes(img)
    i = (model.predict(img) > 0.5).astype("int32")
    dict = {0:'Apricot monilia',1:'carnesiyam',2:'aflatoxin',3:'alternaria',4:'anthracnose',5:'Black Root Rot',6:'Black Rot',7:'Botrytis',8:'downy mildew',9:'leaf rust',10:'mosaic virus',11:'Oedema',12:'Orange Rust',13:'Powdery Mildew',14:'Purple Blotch',15:'sooty blotch'}
    tkinter.messagebox.showinfo(dict[i])
    if i == 1:
        tkinter.messagebox.showinfo("pesticide","Attractants")
    elif i==2:
        tkinter.messagebox.showinfo("pesticide","Algicides")
    elif i==3:
        tkinter.messagebox.showinfo("pesticide","Flavobacterium aurantiacum")
    elif i==4:
        tkinter.messagebox.showinfo("pesticide","Biopesticides")
    elif i==5:
        tkinter.messagebox.showinfo("pesticide","Fungicides")
    elif i==6:
        tkinter.messagebox.showinfo("pesticide","microbial pesiticides")
    elif i==7:
        tkinter.messagebox.showinfo("pesticide","Repelents")
    elif i==8:
        tkinter.messagebox.showinfo("pesticide","sliimicides")
    elif i==9:
        tkinter.messagebox.showinfo("pesticide","Rodonticides")
    elif i==10:
        tkinter.messagebox.showinfo("pesticide","pheromeonts")
    elif i==11:
        tkinter.messagebox.showinfo("pesticide","Ovisicdes")
    elif i==12:
        tkinter.messagebox.showinfo("pesticide","Lemrtocides")
    elif i==13:
        tkinter.messagebox.showinfo("pesticide","Mollusicicdes")
    elif i==14:
        tkinter.messagebox.showinfo("pesticide","Microbial pesicides")

        


knnButton = Button(root, text='Predict', command=svm, fg='blue')
knnButton.pack()
knnButton.place(x=100, y=350)

knnButton = Button(root, text='choose', command=post, fg='blue')
knnButton.pack()
knnButton.place(x=20, y=20)

root.mainloop()

