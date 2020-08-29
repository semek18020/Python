from tkinter import *

root = Tk()
root.title('Semek')
root.geometry('300x300')
root.resizable(width=False, height= False)

entry = Entry(root)
entry.place(x=50, y=0)

name = StringVar()

label = Label(root, text= 'Name: ')
label.place(x=0, y=0)

def print_name():
    name.set(entry.get())

label = Label(root, textvariable = name) 
label.place(x=0, y=120)

def get_name(name):
    print(entry.get())
    entry.insert(5, 'This is my name: ' )

btn = Button(root, text= 'Login', command = lambda: print_name())
btn.place(x=100, y=100)


root.mainloop()