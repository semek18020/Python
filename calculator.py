from tkinter import*
import tkinter.messagebox 

#--------------------------Settings-------------------------#
root = Tk()
root.title ('Calculator')
root.geometry('300x150')
color = 'grey77'
root.configure(bg = color)
root.resizable(width=False, height = False)

#-----------------------------Variables----------------------#
num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

#--------------------------Frames-------------------------#
top_first = Frame(root, width = 800, height = 40, bg = 'grey77' )
top_first.pack(side= TOP)

top_second = Frame(root, width = 800, height = 40, bg = color )
top_second.pack(side= TOP)

top_third = Frame(root, width = 800, height = 40, bg = color )
top_third.pack(side= TOP)

top_fourth = Frame(root, width = 800, height = 40, bg = color )
top_fourth.pack(side= TOP)

#--------------------------Buttons-------------------------#

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'Something went wrong! Please input am Integer')
    elif ms == 'divisionerror':
        tkinter.messagebox.showerror('Division Error', 'Cannot Divide by 0')

def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')

def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')

def times():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')

def div():
    if num2.get() == '0':
        errorMsg('divisionerror')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg('error')
def percent():
    if num2.get() == '0':
        errorMsg('divisionerror')
    elif num2.get() != '0':
        try:
            value = (float(num1.get()) *100) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg('error')


#--------------------------Buttons-------------------------#

btn_plus = Button(top_third, text= '+', width = 5, command = lambda : plus())
btn_plus.pack(side= LEFT, padx = 5, pady = 5)

btn_minus = Button(top_third, text= '-', width = 5, command = lambda : minus())
btn_minus.pack(side= LEFT, padx = 5, pady = 5)

btn_times = Button(top_third, text= 'x', width = 5, command = lambda : times())
btn_times.pack(side= LEFT, padx = 5, pady = 5)

btn_divide = Button(top_third, text= '/', width = 5, command = lambda : div())
btn_divide.pack(side= LEFT, padx = 5, pady = 5)

btn_per_cent = Button(top_third, text= '%', width = 5, command = lambda : percent())
btn_per_cent.pack(side= LEFT, padx = 5, pady = 5) 

#-------------------------------Label-----------------------#

label_first_num = Label(top_first, text = 'Input Number 1:', bg = 'grey77')
label_first_num.pack(side=LEFT, padx =5, pady =5)

first_num = Entry(top_first, bg = 'white', textvariable = num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text = 'Input Number 2:', bg = 'grey77')
label_second_num.pack(side=LEFT, padx =5, pady =5)

second_num = Entry(top_second, bg = 'white', textvariable = num2)
second_num.pack(side=LEFT)

res = Label(top_fourth, text = 'Results', bg = 'grey77')
res.pack(side=LEFT, padx =5, pady =5)

res_num = Entry(top_fourth, bg = 'white', textvariable = res_value)
res_num.pack(side=LEFT)

root.mainloop()