from customtkinter import *
from tkinter import ttk

root = CTk()
root.title("Hogwarts Hub")
root.geometry('450x650')

LARGEFONT = ("futura", 15)

label = CTkLabel(root, text="Welcome to the App 'PotterHeads'", font=LARGEFONT)
label.grid(column=2, padx=120, pady=15)

# Create a notebook (tabbed widget)
notebook = ttk.Notebook(root)
notebook.grid(row=1, column=0, columnspan=4, rowspan=4, padx=10, pady=5)

# Create frames for each page
page1 = CTkFrame(notebook)
page2 = CTkFrame(notebook)

# Add frames to the notebook with corresponding tab names
notebook.add(page1, text="Page 1")
notebook.add(page2, text="Page 2")


def clicked():
    label.configure(text="Next Page")


btn = CTkButton(master=root, text="Press", command=clicked)
btn.grid(column=2, pady=300)

# You can add widgets to each page (frame) as needed.

# Example widgets on Page 1
label_page1 = CTkLabel(page1, text="This is Page 1")
label_page1.grid(row=0, column=0, padx=10, pady=10)

# Example widgets on Page 2
label_page2 = CTkLabel(page2, text="This is Page 2")
label_page2.grid(row=0, column=0, padx=10, pady=10)

# Start the main event loop
root.mainloop()
