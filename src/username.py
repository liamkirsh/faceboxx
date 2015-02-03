from Tkinter import *

top = Tk()
top.wm_title('Faceboxx')
L1 = Label(top, text="User Name")
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)
L1 = Label(top, text="Password")
L1.grid(row=1, column=0)
E2 = Entry(top, bd = 5, show="*")
E2.grid(row=1, column=1)
def ok():
    print E1.get()
    print E2.get()

MyButton1 = Button(top, text="Submit", width=10, command= ok)
MyButton1.grid(row=3, column=1)


top.mainloop()

