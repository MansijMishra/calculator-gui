from tkinter import *

class Calculator:

    def __init__(self):
        
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title('Calculator')
        self.bind_keys()
        self.total = ''
        self.expression = ''
        self.result = ''

        self.tot_expr = Label(text=self.total, anchor=NE,font=('Arial',18), bg= '#D8D8D8', fg='#585858')
        self.tot_expr.grid(row=0,column=0,sticky=NSEW,columnspan=4)

        self.current_exp = Label(text=self.expression, anchor=E,font=('Arial',24), bg= '#D8D8D8', height=2)
        self.current_exp.grid(row=1,column=0,sticky=NSEW,columnspan=4)

        self.b0 = Button(
            text = '7',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 7: self.num_update(x))
        self.b0.grid(row=3,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b1 = Button(
            text = '8',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 8: self.num_update(x))
        self.b1.grid(row=3,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b2 = Button(
            text = '9',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 9: self.num_update(x))
        self.b2.grid(row=3,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b3 = Button(
            text =' 4',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 4: self.num_update(x))
        self.b3.grid(row=4,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b4 = Button(
            text =' 5',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 5: self.num_update(x))
        self.b4.grid(row=4,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b5 = Button(
            text = '6',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 6: self.num_update(x))
        self.b5.grid(row=4,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b6 = Button(
            text = '1',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 1: self.num_update(x))
        self.b6.grid(row=5,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b7 = Button(
            text = '2',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 2: self.num_update(x))
        self.b7.grid(row=5,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b8 = Button(
            text = '3',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 3: self.num_update(x))
        self.b8.grid(row=5,column=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b9 = Button(
            text = '0',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = 0: self.num_update(x))
        self.b9.grid(row=6,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b_decimal = Button(
            text = '.',
            bg = '#A4A4A4',
            font = ('Arial', 16),
            command=lambda x = '.': self.num_update(x))
        self.b_decimal.grid(row=6,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b_equal = Button(
            text = '=',
            bg = '#DF7401',
            font = ('Arial', 16),
            command= lambda : self.equate())
        self.b_equal.grid(row=6,column=2,columnspan=2,ipadx=15,ipady=15,sticky=NSEW)

        self.b_add = Button(
            text = '+',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=lambda x = '+': self.num_update(x))
        self.b_add.grid(row=2,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_subtract= Button(
            text = '-',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=lambda x = '-': self.num_update(x))
        self.b_subtract.grid(row=5,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_multiply= Button(
            text = '*',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=lambda x = '*': self.num_update(x))
        self.b_multiply.grid(row=4,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_divide= Button(
            text = '/',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=lambda x = '/': self.num_update(x))
        self.b_divide.grid(row=3,column=3,ipadx=15,ipady=15,sticky=NSEW)

        self.b_clear = Button(
            text = 'CE',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=self.num_clear)
        self.b_clear.grid(row=2,column=0,ipadx=15,ipady=15,sticky=NSEW)

        self.b_del = Button(
            text = 'DEL',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=self.num_del)
        self.b_del.grid(row=2,column=1,ipadx=15,ipady=15,sticky=NSEW)

        self.b_square = Button(
            text = '^',
            bg = '#DF7401',
            font = ('Arial', 16),
            command=lambda x = '**': self.num_update(x))
        self.b_square.grid(row=2,column=2,ipadx=15,ipady=15,sticky=NSEW)

    def num_update(self, value):
        self.expression += str(value) 
        self.current_exp.config(text=self.expression)

    def num_clear(self):
        self.total = ''
        self.expression = ''
        self.current_exp.config(text=self.expression)
        self.tot_expr.config(text=self.total)

    def num_del(self):
        self.expression = self.expression.rstrip(self.expression[-1])
        self.current_exp.config(text=self.expression)

    def equate(self):
        global expression
        self.result = str(eval(self.expression))
        self.current_exp.config(text=self.result)
        self.tot_expr.config(text=self.expression)
        self.expression = self.result
        self.current_exp.config(text=self.expression)
        
    def bind_keys(self):
        self.window.bind('<Return>', lambda event: self.equate())
        self.window.bind('<BackSpace>', lambda event: self.num_del())

        for i in range(0,10):
            self.window.bind(str(i), lambda event,value=i: self.num_update(value))    

        self.window.bind('.', lambda event, value='.': self.num_update('.'))
        self.window.bind('+', lambda event, value='+': self.num_update('+'))
        self.window.bind('-', lambda event, value='-': self.num_update('-'))
        self.window.bind('*', lambda event, value='*': self.num_update('*'))
        self.window.bind('/', lambda event, value='/': self.num_update('/'))    

    def run_calc(self):
        self.window.mainloop()
        

if __name__ == '__main__':
    calc = Calculator()
    calc.run_calc()