from tkinter import *

root = Tk()
root.geometry('300x300')


frame = Frame(root, width= 100, height = 90, bg = 'red')
frame.pack(side=LEFT)

frame2 = Frame(root, width= 100, height = 90, bg = 'blue')
frame2.pack(side=RIGHT)

frame3 = Frame(root, width= 150, height = 90, bg = 'orange')
frame3.pack(side=TOP)

frame4 = Frame(root, width= 150, height = 90, bg = 'green')
frame4.pack(side=BOTTOM)


root.mainloop()