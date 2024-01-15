from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x400')

frame1 = Frame(root)
frame1.pack()

# Load the image
image = PhotoImage(file="1342799.png")

# Create a label with the image as the background
background_label = Label(frame1, image=image)
background_label.place(relwidth=1, relheight=1)

root.mainloop()
