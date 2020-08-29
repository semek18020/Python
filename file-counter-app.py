from tkinter import *
from tkinter import filedialog 

root = Tk()
root.geometry('300x300')
root.title('File Countter')
color = 'grey77'
root.configure(bg = color)

count_result = dict()

def clear_text():
    word_list.delete(0, END)
    answer.delete('1.0',END)

def open_file():
    root.filename = filedialog.askopenfilename()

def count_text(file):
    file_open = open(str(file), 'r')
    full_text = file_open.readlines()
    file_open.close() 
    
    for word in word_list.get().split(', '):
        for text in full_text:
            if word in count_result:
                count_result[word] = count_result[word] + text.count(word)
            else:
                count_result[word] = text.count(word)

    answer.delete('1.0', END)

    for k, v in count_result.items():
        answer.insert('1.0','{0} {1} \n' .format(k, v))
    
    count_result.clear()



word_list = Entry(root, width= 50)
word_list.place (x=2, y=0)

file = Button(root, text = 'Select File', width = 15, command = lambda: open_file())
file.place(x=0, y=30)

Count = Button(root, text = 'Count Words', width = 15,  command = lambda: count_text(root.filename))
Count.place(x=180, y=30)

Clear= Button(root, text = 'Clear', width = 15, command = lambda: clear_text())
Clear.place(x=90, y=90)

answer = Text(root, height= 30, width= 500, bg = 'white' )
answer.place(x=0, y=120)

root.mainloop()