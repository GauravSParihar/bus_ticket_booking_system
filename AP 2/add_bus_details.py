from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry('1000x800')
Label(root,text=" ").grid(row=0,column=0)#.pack()

img=PhotoImage(file='starbus.png')
Label(root,image=img).grid(row=0,column=2,columnspan=8)#.pack()

Label(root,text="Online Bus Booking System",font='arial 30 bold ',bg='bisque').grid(row=1,column=2,columnspan=8)#.pack()#.grid(row=0,column=0,columnspan=3)
Label(root,text=" ").grid(row=2,column=0)#.pack()
Label(root,text=" ").grid(row=3,column=0)#.pack()
Label(root,text="Add New Details To Database",bg='grey88',fg='green',padx=10).grid(row=4,column=2,columnspan=7)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()

def fun(e=0):
    import abd_op

def fun1(e=0):
    import abd_bus

def fun2(e=0):
    import abd_route

def fun3(e=0):
    import abd_newrun
    
Button(root,text='New Operator',command=fun,bg='green').grid(row=7,column=2)
Button(root,text='New Bus',command=fun1,bg='orange').grid(row=7,column=4)
Button(root,text='New Route',command=fun2,bg='sky blue').grid(row=7,column=6)
Button(root,text='New Run',command=fun3,bg='pink').grid(row=7,column=8)

root.mainloop()
