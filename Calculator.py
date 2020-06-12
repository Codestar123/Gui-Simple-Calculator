from tkinter import *
import time
class Calc:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Simple Calculator')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.tk.configure(background = 'red')
        self.equation = StringVar()
        self.expression_field = Entry(self.tk, textvariable=self.equation) 
        self.expression_field.grid(columnspan=4, ipadx=70) 
        self.equation.set('Enter your question') 
        self.question = ''
        self.questionlist = []
        self.displayquestionlist = []
        self.ans = 0
        self.one = Button(text=1,command=lambda :self.oper_per('1','1'),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.one.grid(row=1,column=0)
        self.two = Button(text=2,command=lambda :self.oper_per('2','2'),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.two.grid(row=1,column=1)
        self.three = Button(text=3, command=lambda :self.oper_per('3','3'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.three.grid(row=1, column=2)
        self.four = Button(text=4, command=lambda :self.oper_per('4','4'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.four.grid(row=2, column=0)
        self.five = Button(text=5, command=lambda :self.oper_per('5','5'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.five.grid(row=2, column=1)
        self.six = Button(text=6, command=lambda :self.oper_per('6','6'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.six.grid(row=2, column=2)
        self.seven = Button(text=7, command=lambda :self.oper_per('7','7'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.seven.grid(row=3, column=0)
        self.eight = Button(text=8, command=lambda :self.oper_per('8','8'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.eight.grid(row=3, column=1)
        self.nine = Button(text=9, command=lambda :self.oper_per('9','9'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.nine.grid(row=3, column=2)
        self.zero = Button(text=0, command=lambda :self.oper_per('0','0'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.zero.grid(row=4, column=1)
        self.equalto = Button(text='=',command=lambda :self.equal(),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.equalto.grid(row=6,column=0)
        self.delete = Button(text='Cut',command=lambda :self.cut(),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.delete.grid(row=4,column=2)
        self.div = Button(text='/',command=lambda :self.oper_per('/',' / '),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.div.grid(row=1,column=3)
        self.mul = Button(text='x',command=lambda :self.oper_per('*',' x '),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.mul.grid(row=2,column=3)
        self.add = Button(text='+', command=lambda :self.oper_per('+',' + '), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.add.grid(row=3, column=3)
        self.sub = Button(text='-', command=lambda :self.oper_per('-',' - '), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.sub.grid(row=4, column=3)
        self.power = Button(text='^',command=lambda :self.oper_per('**',' ^ '),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.power.grid(row=5,column=0)
        self.remainder = Button(text='%',command=lambda :self.oper_per('%',' % '),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.remainder.grid(row=5,column=1)
        self.open_bra = Button(text='(', command=lambda :self.oper_per('(','( '), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.open_bra.grid(row=5, column=2)
        self.close_bra = Button(text=')', command=lambda : self.oper_per(')',' )'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.close_bra.grid(row=5, column=3)
        self.point = Button(text='.', command=lambda : self.oper_per('.','.'), width=6, height=3,fg = 'yellow',bg = 'blue')
        self.point.grid(row=4, column=0)
        self.clear = Button(text='Clear',command=lambda :self.clea(),width=6,height=3,fg = 'yellow',bg = 'blue')
        self.clear.grid(row=6,column=1)
        



    def oper_per(self,num,display_num):
        self.questionlist.append(num)
        self.displayquestionlist.append(display_num)
        self.question = ''.join(self.questionlist)
        self.displayquestion = ''.join(self.displayquestionlist)
        self.equation.set(self.displayquestion)
    def equal(self):
        try:
            
            self.ans = eval(self.question)
            self.equation.set(str(self.ans))
            self.question = ''
        except:
            self.equation.set('Error')
    def cut(self):
        numofcharacterslist = len(self.questionlist)
        if numofcharacterslist != 0:
            del self.questionlist[numofcharacterslist - 1]
            self.question = ''.join(self.questionlist)
            del self.displayquestionlist[numofcharacterslist - 1]
            self.displayquestion = ''.join(self.displayquestionlist)
            self.equation.set(self.displayquestion)
    def clea(self):
        self.question = ''
        self.ans = ''
        self.questionlist = []
        self.displayquestionlist = []
        self.equation.set('')
        


c = Calc()
c.tk.mainloop()
