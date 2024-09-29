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



b1=Button(button_label,text= "  1  ",fg="red")
b1.grid(row=0,column=0,padx=10,pady=10)
b2=Button(button_label,text= "  2  ",fg="red")
b2.grid(row=0,column=1,padx=10,pady=10)
b3=Button(button_label,text= "  3  ",fg="red")
b3.grid(row=0,column=2,padx=10,pady=10)
b4=Button(button_label,text= "  4  ",fg="red")
b4.grid(row=0,column=3,padx=10,pady=10)
b5=Button(button_label,text= "  5  ",fg="red")
b5.grid(row=1,column=0,padx=10,pady=10)
b6=Button(button_label,text= "  6  ",fg="red")
b6.grid(row=1,column=1,padx=10,pady=10)
b7=Button(button_label,text= "  7  ",fg="red")
b7.grid(row=1,column=2,padx=10,pady=10)
b8=Button(button_label,text= "  8  ",fg="red")
b8.grid(row=1,column=3,padx=10,pady=10)



root.mainloop()


