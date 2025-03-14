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
Label(root,text="Enter Journey Details",bg='green',fg='white',padx=10).grid(row=4,column=2,columnspan=6)#.pack()
Label(root,text=" ").grid(row=5,column=0)#.pack()
a=Entry(root)
a.grid(row=7,column=2)
b=Entry(root)
b.grid(row=7,column=4)#pack()
c=Entry(root)
c.grid(row=7,column=6)#pack()
Label(root,text="To:").grid(row=7,column=1)#.pack()
Label(root,text="From:").grid(row=7,column=3)#.pack()
Label(root,text="Journey Date:").grid(row=7,column=5)#.pack()

Button(root,text='Show Bus',bg='green').grid(row=7,column=7)
Button(root,text='Home',bg='green').grid(row=7,column=8)

Label(root,text=" ").grid(row=8,column=6)#.pack()

Label(root,text="Select Bus",fg='green').grid(row=9,column=1)#.pack()
Label(root,text="Operator",fg='green').grid(row=9,column=2)#.pack()
Label(root,text="Bus Type",fg='green').grid(row=9,column=3)#.pack()
Label(root,text="Available Capacity",fg='green').grid(row=9,column=4)#.pack()
Label(root,text="Fare",fg='green').grid(row=9,column=5)#.pack()

Button(root,text='Proceed To Buy',bg='green').grid(row=10,column=7)

Button(root,text="Bus 1").grid(row=10,column=1)#.pack()
Label(root,text="Kamla ",font="arial 10 italic",fg='blue').grid(row=10,column=2)#.pack()
Label(root,text="AC 2x2",fg='blue').grid(row=10,column=3)#.pack()
Label(root,text="25:30",fg='blue').grid(row=10,column=4)#.pack()
Label(root,text="1000",fg='blue').grid(row=10,column=5)#.pack()

Label(root,text="Fill Passenger Details To Book The Bus Ticket",font='arial 15 bold',bg='bisque',fg='red',padx=40).grid(row=12,column=2,columnspan=6)#.pack()
Label(root,text='Name').grid(row=13,column=0)
n=Entry(root)
n.grid(row=13,column=1)
Label(root,text='Gender').grid(row=13,column=2)
Label(root,text='No. of seats').grid(row=13,column=3)
ns=Entry(root)
ns.grid(row=13,column=4)
Label(root,text='Mobile No.').grid(row=13,column=5)
mn=Entry(root)
mn.grid(row=13,column=6)
Label(root,text='Age').grid(row=13,column=7)
mn=Entry(root)
mn.grid(row=13,column=8)

def amount():
    askquestion("Info","Total amount to be paid is .....")
Button(root,text='Book Seat',command=amount,bg='green').grid(row=13,column=9)
#Label(root,text="For Admin Only",font='arial 8 ').grid(row=7,column=6)#.pack()
root.mainloop()


