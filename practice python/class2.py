"(1)Flow charts"
"(2)algorithms"
"(3)pseudocode"
"(4)time & space complexity"

# airthametic operators
a=3
b=3
c=(a+b)
print(c)

a=10
b=7
c=(a-b)
print(c)

a=10
b=2
print(a*b)


a=10
b=2
print(a/b)

# flore devision
a=10
b=3
c=(a // b)
print(c)

# reminder
a=10
b=3
print(a%b)

# exponentiation
a=2
b=3
print(a**b)


# assissment operator

from tkinter import*
from tkinter.ttk import*
sc=0; mn=0; hr=0; stp=0

def Start():
    global sc,mn,hr
    sc = sc+1
    if (sc == 60):
        mn = mn+1
        sc =0
    if mn == 60:
        hr = hr+1
        mn=0
    if stp== 0:
        lbl = Label(rt,text='%i:%i:%i'%(hr,mn,sc),font=('arial',30,'bold'),foreground='red',background='black',width=6)
        lbl.after(300,Start)
        lbl.place(x=170,y=80)
def Stop():
    global stp  
    stp = 1             
rt= Tk(); style=Style()
rt.title("stopwatch")
rt.configure(bg="black")

style.configure('TButton',font=('arial',20,'bold'),borderwidth='5')

start_button =Button(rt,text='Start',command=Start).place(x=10,y=10)
stop_button =Button(rt,text='Stop',command=Stop).place(x=300,y=10)
rt.mainloop()













































































