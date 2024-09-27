#code for creating a wiindow
from tkinter import*

root = Tk() # type: ignore

root.geometry("290x445")
root.title("Calculator")
root.attributes("-alpha",0.9)

a=Label (text="This is a sample code by @kr.anmol1234")
a.pack()
photo= PhotoImage(file="logo.png")
b=Label (image=photo)
b.pack()
root.maxsize(1366,768)
root.minsize(290,445)


root.mainloop()


