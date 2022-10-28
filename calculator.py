from tkinter import *

from pyparsing import col
from traitlets import Undefined
class Calculator(Frame):
    def __init__(self, parent) -> None:
        self.parent = parent
        self.__initUI()
        self.firstNum = 0
        self.secondNum = 0
        self.symbol = ''
    def __initUI(self):
        self.parent.title("Calculator")
        # Two Main Frames
        self.inputFrame = Frame(self.parent,padx=5, pady=5)
        self.inputFrame.grid(row=0, column=0)
        self.btnFrame = Frame(self.parent,padx=5, pady=5)
        self.btnFrame.grid(row=1, column=0)
        #entry box
        
        self.entry = Entry(self.inputFrame)
        self.entry.grid()
        #buttons
        self.btnC = Button(self.btnFrame, text="C", command= lambda: self.clear())
        self.btnC.grid(row=0,column=0)

        self.btnNegative = Button(self.btnFrame, text="+/-",command= lambda: self.neg())
        self.btnNegative.grid(row=0,column=1)

        self.btnPercent = Button(self.btnFrame, text="%",command= lambda: self.percent())
        self.btnPercent.grid(row=0,column=2)

        self.btnDevide = Button(self.btnFrame, text="/",command= lambda: self.operator('/'))
        self.btnDevide.grid(row=0,column=3)

        self.btn7 = Button(self.btnFrame, text="7",command= lambda: self.addNum(7))
        self.btn7.grid(row=1,column=0)

        self.btn8 = Button(self.btnFrame, text="8",command= lambda: self.addNum(8))
        self.btn8.grid(row=1,column=1)

        self.btn9 = Button(self.btnFrame, text="9",command= lambda: self.addNum(9))
        self.btn9.grid(row=1,column=2)

        self.btnX = Button(self.btnFrame, text="x",command= lambda: self.operator('x'))
        self.btnX.grid(row=1,column=3)

        self.btn4 = Button(self.btnFrame, text="4",command= lambda: self.addNum(4))
        self.btn4.grid(row=2,column=0)

        self.btn5 = Button(self.btnFrame, text="5",command= lambda: self.addNum(5))
        self.btn5.grid(row=2,column=1)
        
        self.btn6 = Button(self.btnFrame, text="6",command= lambda: self.addNum(6))
        self.btn6.grid(row=2,column=2)

        self.btnMinus = Button(self.btnFrame, text="-",command= lambda: self.operator('-'))
        self.btnMinus.grid(row=2,column=3)

        self.btn1 = Button(self.btnFrame, text="1",command= lambda: self.addNum(1))
        self.btn1.grid(row=3,column=0)

        self.btn2 = Button(self.btnFrame, text="2",command= lambda: self.addNum(2))
        self.btn2.grid(row=3,column=1)

        self.btn3 = Button(self.btnFrame, text="3",command= lambda: self.addNum(3))
        self.btn3.grid(row=3,column=2)
        self.btnPlus = Button(self.btnFrame, text="+",command= lambda: self.operator('+'))
        self.btnPlus.grid(row=3,column=3)

        self.btn0 = Button(self.btnFrame, text="0", width=7,command= lambda: self.addNum(1))
        self.btn0.grid(row=4,columnspan=2, column=0)

        self.btnDot = Button(self.btnFrame, text=".",command= lambda: self.addNum('.'))
        self.btnDot.grid(row=4,column=2)

        self.btnEq = Button(self.btnFrame, text="=",command= lambda: self.eq())
        self.btnEq.grid(row=4,column=3)
    
    # Helper Functions

    def addNum(self, num):
        if num =='.' and '.' in self.entry.get():
            return
        current = self.entry.get()
        self.entry.delete(0,END)
        self.entry.insert(0,(str(current)+ str(num)))  
    def percent(self):
        current = self.entry.get()
        self.entry.delete(0,END)
        per = int(current)/100
        self.entry.insert(0,str(per))
    def clear(self):
        current = self.entry.get()
        if current is None or current is Undefined or len(current) == 0:
            self.firstNum = ''
            self.secondNum = ''
            self.symbol = ''
            self.entry.delete(0,END)
        else:
            self.entry.delete(0,END)

    def operator(self,s):
        self.firstNum = self.entry.get()
        self.clear()
        self.symbol = s
    def eq(self):
        self.secondNum = self.entry.get()
        self.clear()
        if '.' in self.firstNum or '.' in self.secondNum:
            first, second = float(self.firstNum), float(self.secondNum)
        else:
            first, second =  int(self.firstNum), int(self.secondNum)
        if self.symbol == '+':
            result = first + second
        elif self.symbol == 'x':
            result = first * second
        elif self.symbol == '-':
            result = first - second
        elif self.symbol == '/':
            result = first / second
        self.entry.insert(0,str(result))
        self.firstNum = str(result)
    
    def neg(self):
        current = self.entry.get()
        if '.' in current:
            result = float(current)
        else:
            result = int(current)
        result = result * -1
        self.clear()
        self.entry.insert(0,str(result))
root = Tk()
Calculator(root)
root.mainloop()