from tkinter import *

root = Tk()
root.title('Semek')
root.geometry('300x300')
root.resizable(width=False, height= False)

name = StringVar()

def print_name():
    name.set('Onyekachukwu Joshua')

btn = Button(root, text= 'Click Me', command= lambda :print_name() )
btn.place(x=0, y=0)

label = Label(root, textvariable = name) 
label.place(x=0, y=120)

name1 = StringVar()

def print_name1():
    name1.set('Onyekachukwu Joshua')

btn1 = Button(root, text= 'Click Me', command= lambda :print_name1() )
btn1.place(x=150, y=0)

label = Label(root, textvariable = name1) 
label.place(x=150, y=150)


root.mainloop()