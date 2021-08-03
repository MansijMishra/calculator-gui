from tkinter import *

window = Tk()

# 0-9

b0 = Button(
    text='7')
b0.grid(row=1,column=0,ipadx=50,ipady=50,padx=10,pady=10)

b1 = Button(
    text='8')
b1.grid(row=1,column=1,ipadx=50,ipady=50,padx=10,pady=10)

b2= Button(
    text='9')
b2.grid(row=1,column=2,ipadx=50,ipady=50,padx=10,pady=10)

b3= Button(
    text='4')
b3.grid(row=2,column=0,ipadx=50,ipady=50,padx=10,pady=10)

b4 = Button(
    text='5')
b4.grid(row=2,column=1,ipadx=50,ipady=50,padx=10,pady=10)

b5 = Button(
    text='6')
b5.grid(row=2,column=2,ipadx=50,ipady=50,padx=10,pady=10)

b6= Button(
    text='1')
b6.grid(row=3,column=0,ipadx=50,ipady=50,padx=10,pady=10)

b7= Button(
    text='2')
b7.grid(row=3,column=1,ipadx=50,ipady=50,padx=10,pady=10)

b8 = Button(
    text='3')
b8.grid(row=3,column=2,ipadx=50,ipady=50,padx=10,pady=10)

b9 = Button(
    text='0')
b9.grid(row=4,column=0,ipadx=50,ipady=50,padx=10,pady=10)

b_decimal = Button(
    text='.')
b_decimal.grid(row=4,column=1,ipadx=50,ipady=50,padx=10,pady=10)

# commands

b_equal = Button(
    text='=')
b_equal.grid(row=4,column=2,columnspan=2,sticky=E+W,ipadx=50,ipady=50,padx=10,pady=10)

b_add = Button(
    text='+')
b_add.grid(row=0,column=3,ipadx=50,ipady=50,padx=10,pady=10)

b_subtract= Button(
    text='-')
b_subtract.grid(row=3,column=3,ipadx=50,ipady=50,padx=10,pady=10)

b_multiply= Button(
    text='*')
b_multiply.grid(row=2,column=3,ipadx=50,ipady=50,padx=10,pady=10)

b_divide= Button(
    text='/')
b_divide.grid(row=1,column=3,ipadx=50,ipady=50,padx=10,pady=10)

b_del = Button(
    text='DEL')
b_del.grid(row=0,column=0,columnspan=2,sticky=E+W,ipadx=50,ipady=50,padx=10,pady=10)

b_percent = Button(
    text='%')
b_percent.grid(row=0,column=2,ipadx=50,ipady=50,padx=10,pady=10)

window.mainloop()