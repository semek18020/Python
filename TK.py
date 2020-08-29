from tkinter import *

root = Tk()
root.title('Semek')

label = Label(root, text='M')
label.place(x=0, y=0)

label3 = Label(root, text='M')
label3.place(x=180, y=0)

label = Label(root, text='M')
label.place(x=90, y=90)

label4 = Label(root, text='M')
label4.place(x=180, y=180)

label2 = Label(root, text='M')
label2.place(x=0, y=180)



root.mainloop()