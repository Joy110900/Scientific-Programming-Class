from tkinter import *
from math import *

r = Tk()
r.title('Scientific Calculator')
r.geometry("1100x500")
frame = Frame(r)
Grid.rowconfigure(r, 0, weight=1)
Grid.columnconfigure(r, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)


exp = ""

#appending pressed input to the expression string
def on(n):
    global exp
    exp += str(n)
    l.config(text=exp)

#function to print the answer using the eval() function
def ans():
    global exp
    #If invalid syntax, the output will be cleared and no error will be given
    try:
        exp = str(eval(exp))
    except:
        exp = ""

    l.config(text=exp)

#function to clear either the whole string or the last element
def clr(i):
    global exp
    if i == 0:
        exp = ""
        l.config(text=exp)

    elif i == 1:
        exp = exp[:-1]
        l.config(text=exp)


#Lablel to show text
l = Label(frame, text="", font=("Aria", 40))
l.grid(rowspan=1, columnspan=6, ipadx=70, sticky=N+S+E+W)

fo = StringVar()
fo = ("Purisa", 40, "bold")

#Buttons

button1 = Button(frame, text='1', height=1, width=7, fg="white", bg="black", command=lambda: on(1), font=("Aria", 30)) 
button1.grid(row=4, column=0, sticky=N+S+E+W)

button2 = Button(frame, text='2', height=1, width=7, fg="white", bg="black", command=lambda: on(2), font=("Aria", 30)) 
button2.grid(row=4, column=1, sticky=N+S+E+W)

button3 = Button(frame, text='3', height=1, width=7, fg="white", bg="black", command=lambda: on(3), font=("Aria", 30)) 
button3.grid(row=4, column=2, sticky=N+S+E+W)

button4 = Button(frame, text='4', height=1, width=7, fg="white", bg="black", command=lambda: on(4), font=("Aria", 30)) 
button4.grid(row=3, column=0, sticky=N+S+E+W)

button5 = Button(frame, text='5', height=1, width=7, fg="white", bg="black", command=lambda: on(5), font=("Aria", 30)) 
button5.grid(row=3, column=1, sticky=N+S+E+W)

button6 = Button(frame, text='6', height=1, width=7, fg="white", bg="black", command=lambda: on(6), font=("Aria", 30)) 
button6.grid(row=3, column=2, sticky=N+S+E+W)

button7 = Button(frame, text='7', height=1, width=7, fg="white", bg="black", command=lambda: on(7), font=("Aria", 30)) 
button7.grid(row=2, column=0, sticky=N+S+E+W)

button8 = Button(frame, text='8', height=1, width=7, fg="white", bg="black", command=lambda: on(8), font=("Aria", 30)) 
button8.grid(row=2, column=1, sticky=N+S+E+W)

button9 = Button(frame, text='9', height=1, width=7, fg="white", bg="black", command=lambda: on(9), font=("Aria", 30)) 
button9.grid(row=2, column=2, sticky=N+S+E+W)

button0 = Button(frame, text='0', height=1, width=7, fg="white", bg="black", command=lambda: on(0), font=("Aria", 30)) 
button0.grid(row=5, column=0, sticky=N+S+E+W)

plus = Button(frame, text='+', height=1, width=7, fg="white", bg="black", command=lambda: on("+"), font=("Aria", 30)) 
plus.grid(row=5, column=3, sticky=N+S+E+W)

decimal = Button(frame, text='.', height=1, width=7, fg="white", bg="black", command=lambda: on("."), font=("Aria", 30)) 
decimal.grid(row=5, column=1, sticky=N+S+E+W)

modulus = Button(frame, text='%', height=1, width=7, fg="white", bg="black", command=lambda: on("%"), font=("Aria", 30)) 
modulus.grid(row=5, column=2, sticky=N+S+E+W)

minus = Button(frame, text='-', height=1, width=7, fg="white", bg="black", command=lambda: on("-"), font=("Aria", 30)) 
minus.grid(row=4, column=3, sticky=N+S+E+W)

mul = Button(frame, text='x', height=1, width=7, fg="white", bg="black", command=lambda: on("*"), font=("Aria", 30)) 
mul.grid(row=3, column=3, sticky=N+S+E+W)

div = Button(frame, text='÷', height=1, width=7, fg="white", bg="black", command=lambda: on("/"), font=("Aria", 30)) 
div.grid(row=2, column=3, sticky=N+S+E+W)

clrall = Button(frame, text='Clr', height=1, width=7, fg="white", bg="black", command=lambda: clr(0), font=("Aria", 30)) 
clrall.grid(row=2, column=5, sticky=N+S+E+W)

a = Button(frame, text='=', height=1, width=7, fg="white", bg="black", command=lambda: ans(), font=("Aria", 30)) 
a.grid(row=5, column=4, sticky=N+S+E+W)

backspace = Button(frame, text='<-', height=1, width=7, fg="white", bg="black", command=lambda: clr(1), font=("Aria", 30)) 
backspace.grid(row=2, column=4, sticky=N+S+E+W)

leftbrac = Button(frame, text='(', height=1, width=7, fg="white", bg="black", command=lambda: on("("), font=("Aria", 30)) 
leftbrac.grid(row=3, column=4, sticky=N+S+E+W)

rightbrac = Button(frame, text=')', height=1, width=7, fg="white", bg="black", command=lambda: on(")"), font=("Aria", 30)) 
rightbrac.grid(row=4, column=4, sticky=N+S+E+W)

pibutton = Button(frame, text='π', height=1, width=7, fg="white", bg="black", command=lambda: on("pi"), font=("Aria", 30)) 
pibutton.grid(row=5, column=5, sticky=N+S+E+W)

sqrtbutton = Button(frame, text='√', height=1, width=7, fg="white", bg="black", command=lambda: on("sqrt("), font=("Aria", 30)) 
sqrtbutton.grid(row=4, column=5, sticky=N+S+E+W)

sinbutton = Button(frame, text='sin()', height=1, width=7, fg="white", bg="black", command=lambda: on("sin("), font=("Aria", 30)) 
sinbutton.grid(row=2, column=6, sticky=N+S+E+W)

factbutton = Button(frame, text='!', height=1, width=7, fg="white", bg="black", command=lambda: on("factorial("), font=("Aria", 30)) 
factbutton.grid(row=3, column=5, sticky=N+S+E+W)

cosbutton = Button(frame, text='cos()', height=1, width=7, fg="white", bg="black", command=lambda: on("cos("), font=("Aria", 30)) 
cosbutton.grid(row=3, column=6, sticky=N+S+E+W)

tanbutton = Button(frame, text='tan()', height=1, width=7, fg="white", bg="black", command=lambda: on("tan("), font=("Aria", 30)) 
tanbutton.grid(row=4, column=6, sticky=N+S+E+W)

log10button = Button(frame, text='log10()', height=1, width=7, fg="white", bg="black", command=lambda: on("log10("), font=("Aria", 30)) 
log10button.grid(row=5, column=6, sticky=N+S+E+W)

sinhbutton = Button(frame, text='sinh()', height=1, width=7, fg="white", bg="black", command=lambda: on("sinh("), font=("Aria", 30)) 
sinhbutton.grid(row=1, column=0, sticky=N+S+E+W)

coshbutton = Button(frame, text='cosh()', height=1, width=7, fg="white", bg="black", command=lambda: on("cosh("), font=("Aria", 30)) 
coshbutton.grid(row=1, column=1, sticky=N+S+E+W)

tanhbutton = Button(frame, text='tanh()', height=1, width=7, fg="white", bg="black", command=lambda: on("tanh("), font=("Aria", 30)) 
tanhbutton.grid(row=1, column=2, sticky=N+S+E+W)

degbutton = Button(frame, text='deg', height=1, width=7, fg="white", bg="black", command=lambda: on("degrees("), font=("Aria", 30)) 
degbutton.grid(row=1, column=3, sticky=N+S+E+W)

radbutton = Button(frame, text='rad', height=1, width=7, fg="white", bg="black", command=lambda: on("radians("), font=("Aria", 30)) 
radbutton.grid(row=1, column=4, sticky=N+S+E+W)

powbutton = Button(frame, text='^', height=1, width=7, fg="white", bg="black", command=lambda: on("**"), font=("Aria", 30)) 
powbutton.grid(row=1, column=5, sticky=N+S+E+W)

ebutton = Button(frame, text='e', height=1, width=7, fg="white", bg="black", command=lambda: on("e"), font=("Aria", 30)) 
ebutton.grid(row=1, column=6, sticky=N+S+E+W)

for x in range(7):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(6):
  Grid.rowconfigure(frame, y, weight=1)

r.mainloop()