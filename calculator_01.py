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


#creating writing ar
entry =CTkEntry(root, placeholder_text="enter the numbers")
entry.grid(row=1,column=1,columnspan=3)


#creting buttons



#buttons

b1=CTkButton(root,text="  1  ",width=4,hover_color="gray",text_color="black",anchor="N")
b1.grid(row=3, column=1, padx=33, pady=20,)
b2=CTkButton(root,text="  2  ",width=4,hover_color="gray",text_color="black",anchor="N")
b2.grid(row=3, column=2, padx=33, pady=20,)
b3=CTkButton(root,text="  3  ",width=4,hover_color="gray",text_color="black",anchor="N")
b3.grid(row=3, column=3, padx=33, pady=20,)
b4=CTkButton(root,text="  4  ",width=4,hover_color="gray",text_color="black",anchor="N")
b4.grid(row=4, column=1, padx=33, pady=20,)
b5=CTkButton(root,text="  5  ",width=4,hover_color="gray",text_color="black",anchor="N")
b5.grid(row=4, column=2, padx=33, pady=20,)
b6=CTkButton(root,text="  6  ",width=4,hover_color="gray",text_color="black",anchor="N")
b6.grid(row=4, column=3, padx=33, pady=20,)
b7=CTkButton(root,text="  7  ",width=4,hover_color="gray",text_color="black",anchor="N")
b7.grid(row=5, column=1, padx=33, pady=20,)
b8=CTkButton(root,text="  8  ",width=4,hover_color="gray",text_color="black",anchor="N")
b8.grid(row=5, column=2, padx=33, pady=20,)
b9=CTkButton(root,text="  9  ",width=4,hover_color="gray",text_color="black",anchor="N")
b9.grid(row=5, column=3, padx=33, pady=20,)
b0=CTkButton(root,text="  0  ",width=4,hover_color="gray",text_color="black",anchor="N")
b0.grid(row=6, column=2, padx=33, pady=20,)
add=CTkButton(root,text="  +  ",width=4,hover_color="gray",text_color="black",anchor="N")
add.grid(row=6, column=1, padx=33, pady=20,)
minus=CTkButton(root,text="  -  ",width=4,hover_color="gray",text_color="black",anchor="N")
minus.grid(row=6, column=3, padx=33, pady=20,)
into=CTkButton(root,text="  X  ",width=4,hover_color="gray",text_color="black",anchor="N")
into.grid(row=7, column=1, padx=33, pady=20,)
divide=CTkButton(root,text="  %  ",width=4,hover_color="gray",text_color="black",anchor="N")
divide.grid(row=7, column=2, padx=33, pady=20,)
divide=CTkButton(root,text="  =  ",width=4,hover_color="gray",text_color="black",anchor="N")
divide.grid(row=7, column=3, padx=33, pady=20,)





root.mainloop()