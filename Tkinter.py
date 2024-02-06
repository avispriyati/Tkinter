from tkinter import *
from tkinter import ttk
window=Tk()
window.title("Assigment Tkinter")
window.geometry('325x250')
window.configure(background="white")
a=Label(window,text="Nama:").grid(row=0,column=0)
Label( 
    text="Hai, My name is Avis Priyati",
    bg='#CCCCCC',
    ).grid(row=2, column=0)
a1=Entry(window).grid(row=0,column=1)

btn=ttk.Button(window,text="Submit").grid(row=1,column=1)


window.mainloop()
