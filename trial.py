import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import test


def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Wheel", "*.whl"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    message=test.whl_install(name)
    self.text.set(message)
    print(message)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo ,PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="pip installer GUI", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Install via pip",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = ttk.Button(self, text="Install from a file",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = ttk.Button(self, text="Install via easy_install",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        self.package = tk.StringVar()
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Install via Pip", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        textBox=ttk.Entry(self,textvariable=self.package)
        textBox.pack()

        buttoncommit=ttk.Button(self,text="Search", command=self.valinput)
        buttoncommit.pack()

        self.text = tk.StringVar()
        self.label2 = tk.Label(self, text="", textvariable=self.text)
        self.label2.pack(side="top", fill="x", pady=10)


        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
    
    def valinput(self):
        message=test.install_pip(self.package.get())
        print(message)
        self.text.set(message)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Install via Whl File", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.text = tk.StringVar()
        self.label2 = ttk.Label(self, text="", textvariable=self.text)
        self.label2.pack(side="top", fill="x", pady=10)

        button_l = ttk.Button(self, text="Browse",
                           command=OpenFile)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button_l.pack()
        button.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        self.package = tk.StringVar()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Install via Easy_Install", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)   
        textBox=ttk.Entry(self,textvariable=self.package)
        textBox.pack()


        buttoncommit=ttk.Button(self,text="Search", command=self.valinput)
        buttoncommit.pack()

        self.text = tk.StringVar()
        self.label2 = ttk.Label(self, text="", textvariable=self.text)
        self.label2.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
    
    def valinput(self):
        inputValue=self.package.get()
        print(inputValue)
        self.text.set(test.install_ei(inputValue))



if __name__ == "__main__":
    app = SampleApp()
    app.title("Package Installer")
    app.mainloop()