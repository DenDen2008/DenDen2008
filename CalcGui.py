from tkinter import *
Form1 = Tk()
Form1.geometry('500x600')
Form1.resizable(False, False)
def Button1_Do():
    Edit1.insert(0, '1')
def Button2_Do():
    Edit1.insert(1, '2')
    
Edit1 = Entry(Form1, width='26', borderwidth=3).place(x=10, y=15)
Button1 = Button(Form1, text='1', command=Button1_Do, padx=20, pady=5).place(x=10, y=40)#.grid(row=3, column=0)
Button2 = Button(Form1, text='2', command=Button2_Do, padx=20, pady=5).place(x=65, y=40)#.grid(row=3, column=2)
Button3 = Button(Form1, text='3', command=Button2_Do, padx=20, pady=5).place(x=120, y=40)#.grid(row=3, column=3)
Button3 = Button(Form1, text='3', command=Button2_Do, padx=20, pady=5).place(x=120, y=40)

Form1.mainloop()



