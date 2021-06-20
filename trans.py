from google_trans_new import google_translator
import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
# print(googletrans.LANGUAGES)

#GUI
root = Tk()
 
root.title("Translate By Bê")
root.geometry("420x630")
root.iconbitmap('logo.ico')
load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x=0,y=0)
 

name = Label(root,text="Translator",fg ="#F0350D",bg="#46444F")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box = Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    t = google_translator()
    a = t.translate(INPUT,lang_src='vi',lang_tgt='en')
    box1.insert(END,a)
clear_button = Button(button_frame,text="Clear Text",font=(("Arial"),10,'bold'),bg='#303030',fg="#F0350D",command=clear)
clear_button.place(x=120,y=310)
trans_button = Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg='#303030',fg="#F0350D",command=translate)
trans_button.place(x=250,y=310)
box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=70)


root.mainloop()