import tkinter as tk
from tkinter import filedialog, Text
import os

root=tk.Tk()

canvas=tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()

frame=tk.Frame(root, bg="green")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1, rely=0.1)

openFile=tk.Button(root, text="openFile",padx=10,pady=5,fg="black",bg="black")

openFile.pack()

root.mainloop()