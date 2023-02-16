from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-do list')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)
ws.mainloop()

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]


for item in task_list:
    lb.insert(END, item)

