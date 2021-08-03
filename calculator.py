from tkinter import *

class Calculator:

    def __init__(self):
    
        # 0-9
        self.b0 = Button(
            text='7')
        self.b0.grid(row=1,column=0,ipadx=50,ipady=50,padx=10,pady=10)

        self.b1 = Button(
            text='8')
        self.b1.grid(row=1,column=1,ipadx=50,ipady=50,padx=10,pady=10)

        self.b2= Button(
            text='9')
        self.b2.grid(row=1,column=2,ipadx=50,ipady=50,padx=10,pady=10)

        self.b3= Button(
            text='4')
        self.b3.grid(row=2,column=0,ipadx=50,ipady=50,padx=10,pady=10)

        self.b4 = Button(
            text='5')
        self.b4.grid(row=2,column=1,ipadx=50,ipady=50,padx=10,pady=10)

        self.b5 = Button(
            text='6')
        self.b5.grid(row=2,column=2,ipadx=50,ipady=50,padx=10,pady=10)

        self.b6= Button(
            text='1')
        self.b6.grid(row=3,column=0,ipadx=50,ipady=50,padx=10,pady=10)

        self.b7= Button(
            text='2')
        self.b7.grid(row=3,column=1,ipadx=50,ipady=50,padx=10,pady=10)

        self.b8 = Button(
            text='3')
        self.b8.grid(row=3,column=2,ipadx=50,ipady=50,padx=10,pady=10)

        self.b9 = Button(
            text='0')
        self.b9.grid(row=4,column=0,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_decimal = Button(
            text='.')
        self.b_decimal.grid(row=4,column=1,ipadx=50,ipady=50,padx=10,pady=10)

        # commands

        self.b_equal = Button(
            text='=')
        self.b_equal.grid(row=4,column=2,columnspan=2,sticky=E+W,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_add = Button(
            text='+')
        self.b_add.grid(row=0,column=3,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_subtract= Button(
            text='-')
        self.b_subtract.grid(row=3,column=3,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_multiply= Button(
            text='*')
        self.b_multiply.grid(row=2,column=3,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_divide= Button(
            text='/')
        self.b_divide.grid(row=1,column=3,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_del = Button(
            text='DEL')
        self.b_del.grid(row=0,column=0,columnspan=2,sticky=E+W,ipadx=50,ipady=50,padx=10,pady=10)

        self.b_percent = Button(
            text='%')
        self.b_percent.grid(row=0,column=2,ipadx=50,ipady=50,padx=10,pady=10)

def main(): 
    window = Tk()
    Calculator()
    window.mainloop()

if __name__ == '__main__':
    main()