from customtkinter import *
import requests
from tkinter import ttk


root = CTk()
root.title("Hogwarts Hub")
root.geometry('800x450')


LARGEFONT = ("futura", 15)


label = CTkLabel(root, text= "Welcome to the App 'PotterHeads'", font= LARGEFONT)
label.grid(column=2, padx=270, pady=15)


def clicked():
    label.configure(text= "next page")

btn = CTkButton(master=root, text="press", command=clicked)
btn.grid(column=2, pady=300)




root.mainloop()