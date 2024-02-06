from tkinter import *


ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')


right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Nama : ", 
    bg='#CCCCCC',
    ).grid(row=0, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="Hai, My name is Avis", 
    bg='#CCCCCC',
    ).grid(row=1, column=0, sticky=W, pady=10)

register_name = Entry(
    right_frame, 
    )

register_btn = Button(
    right_frame, 
    width=15, 
    text='Submit', 
    relief=SOLID,
    cursor='hand2',
    command=None
)





register_name.grid(row=0, column=1, pady=10, padx=20)

register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()





ws.mainloop()
