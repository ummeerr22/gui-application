from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('500x450')

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Start, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Add a background image to frames
class CustomFrame(Frame):
    def __init__(self, parent, controller, image_path):
        Frame.__init__(self, parent)
        self.background_image = Image.open("images (5).jpeg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        label = ttk.Label(self, image=self.background_photo)
        label.grid( )

# Start frame with a background image
class Start(CustomFrame):
    def __init__(self, parent, controller):
        image_path = "start_background.jpg"
        CustomFrame.__init__(self, parent, controller, image_path)
        
        label = ttk.Label(self, text="Startpage")
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

# Page1 frame with a background image
class Page1(CustomFrame):
    def __init__(self, parent, controller):
        image_path = "page1_background.jpg"
        CustomFrame.__init__(self, parent, controller, image_path)

        label = ttk.Label(self, text="Page 1")
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(Start))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

# Page2 frame with a background image
class Page2(CustomFrame):
    def __init__(self, parent, controller):
        image_path = "page2_background.jpg"
        CustomFrame.__init__(self, parent, controller, image_path)

        label = ttk.Label(self, text="Page 2")
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Startpage", command=lambda: controller.show_frame(Start))
        button2.grid(row=2, column=1, padx=10, pady=10)

# Driver Code
app = App()
app.mainloop()
