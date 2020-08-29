from tkinter import *

root = Tk()
root.title('FPA')
root.geometry('300x200')
root.resizable( width = False, height = False)
root.configure(bg = 'grey77')

v = IntVar()    
res = IntVar()

def cal_price():
    value = int(v.get())
    if value == 0:
        res.set(int(entry2.get())* 4)
    elif value == 1:
        res.set(int(entry2.get()) * 5)
    elif value == 2:
        res.set(int(entry2.get()) * 3)
    elif value == 3:
        res.set(int(entry2.get()) * 10)
    elif value == 4:
        res.set(int(entry2.get()) * 7)
    elif value == 5:
        res.set(int(entry2.get()) * 9)
    elif value == 6:
        res.set(int(entry2.get()) * 15)
    elif value == 7:
        res.set(int(entry2.get()) * 30)
    elif value == 8:
        res.set(int(entry2.get()) * 6)

label = Label(root, text = 'Choose an item')
label.place(x=100, y=5)
label.configure(bg = 'grey77')

r_btn = Radiobutton(root, text='Banana', bg = 'grey77', variable= v, value = 0)
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text='Apple', bg = 'grey77', variable= v, value = 1) 
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text='Eggs', bg = 'grey77', variable= v, value = 2)
r_btn3.place(x=5, y=90)

r_btn4 = Radiobutton(root, text='Mango', bg = 'grey77', variable= v, value = 3)
r_btn4.place(x=90, y=30)

r_btn5 = Radiobutton(root, text='Rice', bg = 'grey77', variable= v, value = 4) 
r_btn5.place(x=90, y=60)

r_btn6 = Radiobutton(root, text='Fish', bg = 'grey77', variable= v, value = 5)
r_btn6.place(x=90, y=90)

r_btn7 = Radiobutton(root, text='Maize', bg = 'grey77', variable= v, value = 6)
r_btn7.place(x=180, y=30)

r_btn8 = Radiobutton(root, text='Slik', bg = 'grey77', variable= v, value = 7) 
r_btn8.place(x=180, y=60)

r_btn9 = Radiobutton(root, text='Milk', bg = 'grey77', variable= v, value = 8)
r_btn9.place(x=180, y=90)


entry = Entry(root, width=25, textvariable= res)
entry.place(x=70, y=160)

label_res = Label(root, text = 'Results', bg = 'grey77')
label_res.place(x=8, y=160)

entry2 = Entry(root, width=25)
entry2.place(x=70, y=130)

btn = Button(root, text= 'Cal', bg = 'grey77', command = lambda: cal_price())
btn.place(x=5, y=130)

root.mainloop()