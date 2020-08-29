from tkinter import*

#--------------------------Setting-----------------------#
root = Tk()
root.geometry('800x500')
root.title('Slick Mail')
color = 'white'
root.configure(bg = 'green')
root.resizable(width = False, height = False)

#------------------------Functions-------------------------#
def clear_from():
    f.delete(0, END)

def clear_to():
    t.delete(0, END)

def clear_all():
    clear_from()
    clear_to()

def clear_text():
    message.delete('1.0', END)

def send_email():
     print(f.get())
     print(t.get())
     print(message.get('1.0', END))





#------------------------Frames-------------------------#
top = Frame(root, width = 800, height = 50, bg = 'orange')
top.pack(side = TOP)

bottom = Frame(root, width = 800, height = 50, bg = 'blue')
bottom.pack(side = BOTTOM)

left = Frame(root, width = 800, height = 400, bg = 'white')
left.pack(side = LEFT)

right = Frame(root, width = 200, height = 400, bg = 'green')
right.pack(side = RIGHT)

#------------------------Button-------------------------#
btn_clear_from = Button(right, text = 'Clear From',
                    font = ('arial', 10, 'bold'), bg = color, command = lambda : clear_from())
btn_clear_from.place(x = 1, y = 20)

btn_clear_to = Button(right, text = 'Clear To',
                    font = ('arial', 10, 'bold'), bg = color, command = lambda : clear_to())
btn_clear_to.place(x = 130, y = 20)

btn_clear_text = Button(right, text = 'Clear Text',
                    font = ('arial', 10, 'bold'), bg = color, command = lambda : clear_text())
btn_clear_text.place(x = 120, y = 70)

btn_clear_all = Button(right, text = 'Clear All',
                    font = ('arial', 10, 'bold'), bg = color, command = lambda : clear_all())
btn_clear_all.place(x = 1, y = 70)

send = Button(right, text = 'Send',
                    font = ('arial', 10, 'bold'), bg = color, command = lambda : send_email())
send.place(x = 80, y = 120)


#------------------------Entries-------------------------#
from_label = Label (top, font = ('arial', 12, 'bold'), text = 'From :', bg = 'orange')
from_label.place(x=10, y =10)

f = Entry(top, font = ('arial', 12, 'bold'), width = 25, bd = 3)
f.place(x = 70, y = 10)

from_label2 = Label (top, font = ('arial', 12, 'bold'), text = 'To :', bg = 'orange')
from_label2.place(x= 310, y =10)

t = Entry(top, font = ('arial', 12, 'bold'), width = 25, bd = 3)
t.place(x = 355, y = 10)


#------------------------MessageBox-------------------------#
message = Text(left, font = ('arial', 12, 'bold'), width = 65)
message.pack(side = LEFT) 


root.mainloop()