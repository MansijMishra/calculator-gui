from tkinter import *

class Calculator:

    def __init__(self):
        
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title('Calculator')

    # def buttons_frame(self):
    #     self.frame = Frame(self.window, height=150)
    #     self.frame.pack(expand=True,fill='both')
    #     return self.frame
        self.b0 = Button(
            text = '7',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b0.grid(row=1,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b1 = Button(
            text = '8',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b1.grid(row=1,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b2 = Button(
            text = '9',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b2.grid(row=1,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b3 = Button(
            text =' 4',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b3.grid(row=2,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b4 = Button(
            text =' 5',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b4.grid(row=2,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b5 = Button(
            text = '6',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b5.grid(row=2,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b6 = Button(
            text = '1',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b6.grid(row=3,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b7 = Button(
            text = '2',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b7.grid(row=3,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b8 = Button(
            text = '3',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b8.grid(row=3,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b9 = Button(
            text = '0',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b9.grid(row=4,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b_decimal = Button(
            text = '.',
            bg = '#A4A4A4',
            font = ('Arial', 16))
        self.b_decimal.grid(row=4,column=1,ipadx=15,ipady=15,sticky=NSEW)

        # commands

        self.b_equal = Button(
            text = '=',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_equal.grid(row=4,column=2,columnspan=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b_add = Button(
            text = '+',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_add.grid(row=0,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_subtract= Button(
            text = '-',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_subtract.grid(row=3,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_multiply= Button(
            text = '*',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_multiply.grid(row=2,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_divide= Button(
            text = '/',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_divide.grid(row=1,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_del = Button(
            text = 'DEL',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_del.grid(row=0,column=0,columnspan=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b_percent = Button(
            text = '%',
            bg = '#DF7401',
            font = ('Arial', 16))
        self.b_percent.grid(row=0,column=2,ipadx=15,ipady=15,sticky=NSEW)


    def run_calc(self):
        self.window.mainloop()
        


if __name__ == '__main__':
    calc = Calculator()
    calc.run_calc()