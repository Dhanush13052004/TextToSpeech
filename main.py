from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(speed=='Fast'):
        engine.setProperty('rate',250)
        setvoice()
    elif(speed=='Normal'):
        engine.setProperty('rate', 150)
        setvoice()
    else:
        engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()

    if (speed == 'Fast'):
        engine.setProperty('rate', 250)
        setvoice()
    elif (speed == 'Normal'):
        engine.setProperty('rate', 150)
        setvoice()
    else:
        engine.setProperty('rate', 60)
        setvoice()

window=Tk()
window.title("Text To Speech")
icon = PhotoImage(file='img.png')
window.iconphoto(True,icon)
window.geometry("1100x500+130+130")
window.resizable(False,False)
window.configure(bg="black")
l1= Label(text="TEXT TO SPEECH",font=("cascadia code extralight",30,"bold"),fg="#E75480",bg="black")
l1.place(x=350,y=0)
text_area = Text(window,font=("cascadia code",20),wrap=WORD,bg="#FAAFBA",fg="Black")
text_area.place(x=10,y=90,width=750,height=300)
gender_combobox = Combobox(window,values=['Male','Female'],font=("arial",14),state='r',width=8)
gender_combobox.place(x=780,y=200)
gender_combobox.set('Male')
Label(text="VOICE",font=("cascadia code extralight",20),fg="#E75480",bg="black").place(x=790,y=150)
speed_combobox = Combobox(window,values=['Fast','Normal','Slow'],font=("arial",14),state='r',width=8)
speed_combobox.place(x=940,y=200)
speed_combobox.set('Normal')
Label(text="SPEED",font=("cascadia code extralight",20),fg="#E75480",bg="black").place(x=940,y=150)
btn1 = Button(window,text="Speak",width=9,font="arial 14 bold",fg="black",bg="#E75480",command=speaknow)
btn1.place(x=780,y=280)
btn2 = Button(window,text="Save",width=9,font="arial 14 bold",fg="black",bg="#E75480",command=download)
btn2.place(x=940,y=280)
window.mainloop()
