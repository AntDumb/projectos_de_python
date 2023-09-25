import tkinter
from tkinter import Tk, font
import math
from datetime import datetime
now=datetime.now()
if len(str(now.minute)) == 2 :
    x = f"{now.hour}:{now.minute}"
else : x = f"{now.hour}:0{now.minute}"

ven = tkinter.Tk()
ven.configure(bg='gray17')
#icono = tkinter.PhotoImage(file="logo__.png")    no se poner iconos yo todo imbecil 
#ven.iconphoto(True, icono)
ven.title("Calculadora - v1.1")
ven.geometry("475x410")

t = tkinter.Label(text=f"Abierto a las {x}", bg="white")
t.place(x=375, y=390)

text = tkinter.Entry(ven, font="Calibri 23", bg="gray89")
sub_text = tkinter.Entry(ven, font="Calibri 9", bg="gray89")

def input_button(value) : 
    
    text.insert(40, value)
    sub_text.delete(0, "end") 
def delete_input() :
    x = text.get()
    y = len(x)
    y = y-1
    text.delete(y, tkinter.END)   
def calculate() :
    band = True
    band2 = True
    true_text = text.get()
    if true_text == "codigosecreto" : text.delete(0, "end"); sub_text.insert(40, "Lo descubriste"); band2=False
    
    if band2 == True :
        try : text.delete(0, "end"); true_true_text = eval(true_text)
        except : sub_text.insert(40, "Syntax Error"); band=False
        if band == True :
            text.delete(0, "end")
            text.insert(40, true_true_text)
        
button1 = tkinter.Button(ven, text="1", width=10, height=5, command=lambda:input_button(1), bg="gray99")
button2 = tkinter.Button(ven, text="2", width=10, height=5, command=lambda:input_button(2), bg="gray99")
button3 = tkinter.Button(ven, text="3", width=10, height=5, command=lambda:input_button(3), bg="gray99")
button4 = tkinter.Button(ven, text="4", width=10, height=5, command=lambda:input_button(4), bg="gray99")
button5 = tkinter.Button(ven, text="5", width=10, height=5, command=lambda:input_button(5), bg="gray99")
button6 = tkinter.Button(ven, text="6", width=10, height=5, command=lambda:input_button(6), bg="gray99")
button7 = tkinter.Button(ven, text="7", width=10, height=5, command=lambda:input_button(7), bg="gray99")
button8 = tkinter.Button(ven, text="8", width=10, height=5, command=lambda:input_button(8), bg="gray99")
button9 = tkinter.Button(ven, text="9", width=10, height=5, command=lambda:input_button(9), bg="gray99")
button10 = tkinter.Button(ven, text="Borrar", width=10, height=5, command=lambda: delete_input(), bg="maroon")
button11 = tkinter.Button(ven, text="0", width=10, height=5, command=lambda:input_button(0), bg="gray99")
button12 = tkinter.Button(ven, text="=", width=10, height=5, command=lambda:calculate(), bg="green")
button13 = tkinter.Button(ven, text="x", width=10, height=5, command=lambda:input_button("*"), bg="gray99")
button14 = tkinter.Button(ven, text="/", width=10, height=5, command=lambda:input_button("/"), bg="gray99")
button15 = tkinter.Button(ven, text="-", width=10, height=5, command=lambda:input_button("-"), bg="gray99")
button16 = tkinter.Button(ven, text="+", width=10, height=5, command=lambda:input_button("+"), bg="gray99")

button17 = tkinter.Button(ven, text=".", width=10, height=5, command=lambda:input_button("."), bg="gray99")
button18 = tkinter.Button(ven, text="π", width=10, height=5, command=lambda:input_button(str(math.pi)), bg="gray99")                                                                                                                                                                                                                


text.grid(row=0, column=0, columnspan=4, padx=6, pady=7)
sub_text.place(x=340, y=14)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button10.grid(row=4, column=0)
button11.grid(row=4, column=1)
button12.grid(row=4, column=2)

button13.grid(row=1, column=3)
button14.grid(row=2, column=3)
button15.grid(row=3, column=3)
button16.grid(row=4, column=3)

button17.grid(row=1, column=4)
button18.grid(row=2, column=4)


ven.mainloop()import tkinter
from tkinter import Tk, font
import math
from datetime import datetime
now=datetime.now()
if len(str(now.minute)) == 2 :
    x = f"{now.hour}:{now.minute}"
else : x = f"{now.hour}:0{now.minute}"

ven = tkinter.Tk()
ven.configure(bg='gray17')
icono = tkinter.PhotoImage(file="logo__.png")
ven.iconphoto(True, icono)
ven.title("Calculadora - v1.1")
ven.geometry("475x410")

t = tkinter.Label(text=f"Abierto a las {x}", bg="white")
t.place(x=375, y=390)

text = tkinter.Entry(ven, font="Calibri 23", bg="gray89")
sub_text = tkinter.Entry(ven, font="Calibri 9", bg="gray89")

def input_button(value) : 
    
    text.insert(40, value)
    sub_text.delete(0, "end") 
def delete_input() :
    x = text.get()
    y = len(x)
    y = y-1
    text.delete(y, tkinter.END)   
def calculate() :
    band = True
    band2 = True
    true_text = text.get()
    if true_text == "codigosecreto" : text.delete(0, "end"); sub_text.insert(40, "Lo descubriste"); band2=False
    
    if band2 == True :
        try : text.delete(0, "end"); true_true_text = eval(true_text)
        except : sub_text.insert(40, "Syntax Error"); band=False
        if band == True :
            text.delete(0, "end")
            text.insert(40, true_true_text)
        
button1 = tkinter.Button(ven, text="1", width=10, height=5, command=lambda:input_button(1), bg="gray99")
button2 = tkinter.Button(ven, text="2", width=10, height=5, command=lambda:input_button(2), bg="gray99")
button3 = tkinter.Button(ven, text="3", width=10, height=5, command=lambda:input_button(3), bg="gray99")
button4 = tkinter.Button(ven, text="4", width=10, height=5, command=lambda:input_button(4), bg="gray99")
button5 = tkinter.Button(ven, text="5", width=10, height=5, command=lambda:input_button(5), bg="gray99")
button6 = tkinter.Button(ven, text="6", width=10, height=5, command=lambda:input_button(6), bg="gray99")
button7 = tkinter.Button(ven, text="7", width=10, height=5, command=lambda:input_button(7), bg="gray99")
button8 = tkinter.Button(ven, text="8", width=10, height=5, command=lambda:input_button(8), bg="gray99")
button9 = tkinter.Button(ven, text="9", width=10, height=5, command=lambda:input_button(9), bg="gray99")
button10 = tkinter.Button(ven, text="Borrar", width=10, height=5, command=lambda: delete_input(), bg="maroon")
button11 = tkinter.Button(ven, text="0", width=10, height=5, command=lambda:input_button(0), bg="gray99")
button12 = tkinter.Button(ven, text="=", width=10, height=5, command=lambda:calculate(), bg="green")
button13 = tkinter.Button(ven, text="x", width=10, height=5, command=lambda:input_button("*"), bg="gray99")
button14 = tkinter.Button(ven, text="/", width=10, height=5, command=lambda:input_button("/"), bg="gray99")
button15 = tkinter.Button(ven, text="-", width=10, height=5, command=lambda:input_button("-"), bg="gray99")
button16 = tkinter.Button(ven, text="+", width=10, height=5, command=lambda:input_button("+"), bg="gray99")

button17 = tkinter.Button(ven, text=".", width=10, height=5, command=lambda:input_button("."), bg="gray99")
button18 = tkinter.Button(ven, text="π", width=10, height=5, command=lambda:input_button(str(math.pi)), bg="gray99")                                                                                                                                                                                                                


text.grid(row=0, column=0, columnspan=4, padx=6, pady=7)
sub_text.place(x=340, y=14)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button10.grid(row=4, column=0)
button11.grid(row=4, column=1)
button12.grid(row=4, column=2)

button13.grid(row=1, column=3)
button14.grid(row=2, column=3)
button15.grid(row=3, column=3)
button16.grid(row=4, column=3)

button17.grid(row=1, column=4)
button18.grid(row=2, column=4)


ven.mainloop()
