import tkinter as tk 
width=206
height=324
root=tk.Tk()
px=5
py=12
screen=tk.StringVar()
screen.set("0")
def press_num(tx):
    screen.set(value=tx)

root.title("Calculator")
root.geometry("{}x{}+900+200".format(width,height))
root.resizable(False,False)

entry=tk.Entry(width=13,bd=16,font="Arial 17",justify="right",textvariable=screen)
entry.grid(row=0,column=0,columnspan=4,ipady=4)

butonC=tk.Button(text="C",font="Verdana 10",width=px)
butonC.grid(row=1,column=0,ipady=py)

butonSqrt=tk.Button(text="√",font="Verdana 10",width=px)
butonSqrt.grid(row=1,column=1,ipady=py)

butonPow=tk.Button(text="X^Y",font="Verdana 10",width=px)
butonPow.grid(row=1,column=2,ipady=py)

butonPerc=tk.Button(text="%",font="Verdana 10",width=px)
butonPerc.grid(row=1,column=3,ipady=py) 
sayi=1
for i in range(3):
    for j in range(3):
        buttonNum=tk.Button(text=sayi,font="Verdana 10",width=px)
        sayi+=1
        buttonNum.grid(row=i+2,column=j,ipady=py)


butonPlus=tk.Button(text="+",font="Verdana 10",width=px,command= lambda: press_num("+"))
butonPlus.grid(row=2,column=3,ipady=py)

butonMinus=tk.Button(text="-",font="Verdana 10",width=px,command= lambda: press_num("-"))
butonMinus.grid(row=3,column=3,ipady=py)

butonMult=tk.Button(text="*",font="Verdana 10",width=px)
butonMult.grid(row=4,column=3,ipady=py)

butonDiv=tk.Button(text="/",font="Verdana 10",width=px)
butonDiv.grid(row=5,column=3,ipady=py)

butonZero=tk.Button(text="0",font="Verdana 10",width=px)
butonZero.grid(row=5,column=1,ipady=py)

butonDot=tk.Button(text=".",font="Verdana 10",width=px)
butonDot.grid(row=5,column=0,ipady=py)

butonEqual=tk.Button(text="=",font="Verdana 10",width=px)
butonEqual.grid(row=5,column=2,ipady=py)













root.mainloop()