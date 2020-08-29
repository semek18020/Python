from tkinter import*
import tkinter.messagebox
from io import StringIO

root = Tk()
root.geometry('500x300')
root.title('Python IDE')
color= 'grey'
root.configure(bg = color)
root.resizable(width = False, height= False)

def clear_python():
    python_code.delete('1.0', END)

def run():
    #Run Python Code
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(python_code.get('1.0', END))
    sys.stdout = old_stdout
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())

    #Show Python Code to User


top = Frame(root, width = 800, height = 50, bg = color)
top.pack(side = TOP)

bottom = Frame(root, width = 800, height= 500, bg ='red')
bottom.pack(side=BOTTOM)

btn_clear = Button(top, text= 'Clear', bg ='grey77', font = ('arial', 10, 'bold'), command = lambda :clear_python())
btn_clear.pack(side = TOP)

btn_run = Button(top, text= 'Run', bg ='grey77', font = ('arial', 10, 'bold'), command = lambda: run())
btn_run.pack(side = TOP)

python_code = Text(bottom, font = ('arial', 7, 'bold'), bg = 'grey88')
python_code.pack(side=TOP)

root.mainloop()



