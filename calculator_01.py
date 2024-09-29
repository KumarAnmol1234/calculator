#code for creating a window
from tkinter import*

root = Tk() # type: ignore

#window setting
root.geometry("290x445")
root.title("Calculator")
root.attributes("-alpha",0.9)
root.maxsize(1366,768)
root.minsize(290,445)




#setting for the labels
border= Frame(root,bg="gray",borderwidth=2)
border.pack(side= TOP,fill=X)
a=Label (border,text="This is a sample code by @kr.anmol1234",bg="gray")
a.pack()
photo= PhotoImage(file="logo.png")
b=Label (image=photo)
b.pack(side= RIGHT,anchor="ne")

#creting buttons
button_label=Frame(root,bg="gray",borderwidth=10)
button_label.pack()
b1=Button(button_label,text="   1   ",fg="red")
b1.pack(side=LEFT,anchor="nw",padx=10)
b2=Button(button_label,text="   2   ",fg="red")
b2.pack(side=LEFT,anchor="n",padx=10)
b3=Button(button_label,text="   3   ",fg="red")
b3.pack(side=LEFT,anchor="nw",padx=10)
b4=Button(button_label,text="   4   ",fg="red")
b4.pack(side=LEFT,anchor="nw",padx=10)

b5=Button(button_label,text="   5   ",fg="red")
b5.pack(side="bottom",anchor="e",padx=10)
b6=Button(button_label,text="   6   ",fg="red")
b6.pack(side=LEFT,anchor="w",padx=10)
b7=Button(button_label,text="   7   ",fg="red")
b7.pack(side=LEFT,anchor="w",padx=10)
b8=Button(button_label,text="   8   ",fg="red")
b8.pack(side=LEFT,anchor="w",padx=10)



root.mainloop()


