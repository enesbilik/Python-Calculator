import tkinter as tk 
width=260
height=370
root=tk.Tk()

value=tk.StringVar()
value.set("")


px=5
py=12


def checkState():
    global butonMult,butonSqrt,butonPow,butonDot
    if len(entry.get())==0:
        butonPow["state"]=tk.DISABLED
        butonMult["state"]=tk.DISABLED
        butonSqrt["state"]=tk.DISABLED
        butonDot["state"]=tk.DISABLED
        butonDiv["state"]=tk.DISABLED
    
    elif entry.get()=="-":
        butonPow["state"]=tk.DISABLED
        butonMult["state"]=tk.DISABLED
        butonSqrt["state"]=tk.DISABLED
        butonDot["state"]=tk.DISABLED
        butonDiv["state"]=tk.DISABLED

        

    else:
        butonPow["state"]=tk.NORMAL
        butonMult["state"]=tk.NORMAL
        butonSqrt["state"]=tk.NORMAL
        butonDot["state"]=tk.NORMAL
        butonDiv["state"]=tk.NORMAL
        
def pow():
    press_num("^")


def sqrt():
    valuen=entry.get()
    valuen=eval(valuen)
    value.set(round(valuen**0.5,4))


def clearLast():
    global value
    value.set(entry.get()[:-1])
    checkState()

def clearAll():
    global value
    value.set("")
    checkState()

def press_num(tx):
    leng=len(entry.get())
    entry.insert(leng,tx)
    checkState()

def calculate():
    islem=str(entry.get()).replace("^","**")
    sonuc=eval(islem)
    value.set(sonuc)




root.title("Calculator")
root.geometry("{}x{}+900+200".format(width,height))
root.resizable(False,False)

entry=tk.Entry(width=13,bd=16,font="Arial 17",justify="right",textvariable=value,takefocus=True)
entry.grid(row=0,column=0,columnspan=4,ipady=4)


butonC=tk.Button(text="C",font="Verdana 10",width=px,command=lambda:clearAll())
butonC.grid(row=1,column=0,ipady=py)

butonSqrt=tk.Button(text="√",font="Verdana 10",width=px,command=lambda:sqrt())
butonSqrt.grid(row=1,column=1,ipady=py)

butonPow=tk.Button(text="X^Y",font="Verdana 10",width=px,command=lambda:pow())
butonPow.grid(row=1,column=2,ipady=py)

butonPerc=tk.Button(text="<-",font="Verdana 10",width=px,command=lambda:clearLast())
butonPerc.grid(row=1,column=3,ipady=py) 

b=[]

for i in range(1,10):
    b.append(tk.Button(text=str(i),font="Verdana 10",width=px,command= lambda x=i: press_num(x)))

sayi=0

for i in range(3):
    for j in range(3):
        
        b[sayi].grid(row=i+2,column=j,ipady=py)
        sayi+=1
        
        


butonPlus=tk.Button(text="+",font="Verdana 10",width=px,command= lambda: press_num("+"))
butonPlus.grid(row=2,column=3,ipady=py)

butonMinus=tk.Button(text="-",font="Verdana 10",width=px,command= lambda: press_num("-"))
butonMinus.grid(row=3,column=3,ipady=py)

butonMult=tk.Button(text="*",font="Verdana 10",width=px,command= lambda: press_num("*"))
butonMult.grid(row=4,column=3,ipady=py)

butonDiv=tk.Button(text="/",font="Verdana 10",width=px,command= lambda: press_num("/"))
butonDiv.grid(row=5,column=3,ipady=py)

butonZero=tk.Button(text="0",font="Verdana 10",width=px,command= lambda: press_num("0"))
butonZero.grid(row=5,column=1,ipady=py)

butonDot=tk.Button(text=".",font="Verdana 10",width=px,command= lambda: press_num("."))
butonDot.grid(row=5,column=0,ipady=py)

butonEqual=tk.Button(text="=",font="Verdana 10",width=px,command= lambda: calculate())
butonEqual.grid(row=5,column=2,ipady=py)


checkState()












root.mainloop()
