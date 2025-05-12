#code for creating a window
from tkinter import*
 # type: ignore
from customtkinter import *
import math as m
 
root = CTk()

#window setting
root.geometry("300x445")
root.title("Calculator")
root.attributes("-alpha",0.9)
root.maxsize(1366,768)
root.minsize(300,445)


#setting for the 
border= Frame(root,bg="gray",borderwidth=2)
border.grid(column=1,columnspan=3,sticky=N)
a=Label (border,text="This is a sample code by @kr.anmol1234",bg="gray")
a.grid(row=0,column=1)

photo= PhotoImage(file="logo.png")
b=Label (image=photo)
b.grid(row=0,column=3,sticky=NE)


#creating writing area
entry =CTkEntry(root, placeholder_text="enter the numbers")
entry.grid(row=1,column=1,columnspan=3)

def add_to_entry(char):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(char))


def calculate():
    try:
        result = eval(entry.get().replace('X', '*').replace('%', '/').replace('-', '-').replace('+', '+'))
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")



#creting buttons


class numbers:
    def __init__(alpha,root):
        pass
#buttons
buttons = [
    ("1", 3, 1), ("2", 3, 2), ("3", 3, 3),
    ("4", 5, 1), ("5", 5, 2), ("6", 5, 3),
    ("7", 7, 1), ("8", 7, 2), ("9", 7, 3),
    ("0", 9, 2), ("+", 9, 1), ("-", 9, 3),
    ("X", 11, 1), ("/", 11, 2), ("=", 11, 3)
]


for (text, row, col) in buttons:
    if text == "=":
        btn = CTkButton(root, text=text, width=4, command=calculate)
    else:
        btn = CTkButton(root, text=text, width=4, command=lambda t=text: add_to_entry(t))
    btn.grid(row=row, column=col, padx=20, pady=10)




root.mainloop()

