import tkinter as tk
from tkinter import font as tkfont
from tkinter import*
from customtkinter import *

import math as m
import customtkinter as ctk
#the app and geometry
root= ctk.CTk()
root.geometry("380x680")
root.title("Calculator")
root.resizable(False,False)
root.configure(fg_color="#1a1a1a")
BG_COLOR = "#272727"
#frames
frame= ctk.CTkFrame(root, fg_color="#1a1a1a", corner_radius=0)
frame.pack(fill="both", expand=True,padx=12,pady=12)

frame1=ctk.CTkFrame(frame, fg_color=BG_COLOR, corner_radius=12,height=48)
frame1.pack(fill="x",pady=(0,10))

frame2=ctk.CTkFrame(frame, fg_color=BG_COLOR, corner_radius=14)
frame2.pack(fill="x", pady=(0,10))
frame3=ctk.CTkFrame(frame, fg_color=BG_COLOR, corner_radius=10)
frame3.pack(fill="x", pady=(0,10))
frame4=ctk.CTkFrame(frame, fg_color=BG_COLOR, corner_radius=14)
frame4.pack(fill="both",expand=True)


#this is a comment to test git push command 
root.mainloop()

