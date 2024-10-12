#code for creating a window
from tkinter import*
 # type: ignore
from customtkinter import *
 
root = CTk()

#window setting
root.geometry("290x445")
root.title("Calculator")
root.attributes("-alpha",0.9)
root.maxsize(1366,768)
root.minsize(290,445)


#setting for the labels

#creating writing area
screen= IntVar()
scre=Entry(root,textvariable=screen)
scre.grid(column=2,pady=10,row=1)


#creting buttons



#buttons

b1=CTkButton(root,text="  1  ",width=4,)
b1.grid(row=2, column=1, padx=33, pady=20)
b2=CTkButton(root,text="  2  ",width=4)
b2.grid(row=2, column=2, padx=33, pady=20)
b3=CTkButton(root,text="  3  ",width=4)
b3.grid(row=2, column=3, padx=33, pady=20)
b4=CTkButton(root,text="  4  ",width=4)
b4.grid(row=3, column=1, padx=33, pady=20)
b5=CTkButton(root,text="  5  ",width=4)
b5.grid(row=3, column=2, padx=33, pady=20)
b6=CTkButton(root,text="  6  ",width=4)
b6.grid(row=3, column=3, padx=33, pady=20)
b7=CTkButton(root,text="  7  ",width=4)
b7.grid(row=4, column=1, padx=33, pady=20)
b8=CTkButton(root,text="  8  ",width=4)
b8.grid(row=4, column=2, padx=33, pady=20)
b9=CTkButton(root,text="  9  ",width=4)
b9.grid(row=4, column=3, padx=33, pady=20)
b0=CTkButton(root,text="  0  ",width=4)
b0.grid(row=5, column=2, padx=33, pady=20)

add=CTkButton(root,text="  +  ",width=4)
add.grid(row=5, column=1, padx=33, pady=20)

minus=CTkButton(root,text="  -  ",width=4)
minus.grid(row=5, column=3, padx=33, pady=20)

into=CTkButton(root,text="  X  ",width=4)
into.grid(row=6, column=1, padx=33, pady=20)

divide=CTkButton(root,text="  %  ",width=4)
divide.grid(row=6, column=2, padx=33, pady=20)
divide=CTkButton(root,text="  =  ",width=4)
divide.grid(row=6, column=3, padx=33, pady=20)








root.mainloop()



