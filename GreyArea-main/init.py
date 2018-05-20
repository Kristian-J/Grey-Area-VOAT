# import tkinter as tk
# tk._test()

from tkinter import *
from tkinter import ttk
from Sel_File_Type import *
from module_template import *


class Controller:
    def __init__(self):
        # global session
        self.var = None
        self.response = None
        self.session = None

        self.root1 = Tk()
        self.root1.title("Welcome")
        self.get_type()

        self.testcall = Xxxxx(self)
                ### this is an example external funtion/class call
                ### refer to module_template.py
                ### passes self (this instance of Controller)
        # self.root1.mainloop()
        return

    def get_type(self):
        self.frame = Frame(self.root1)
        self.frame.grid()
        Label(self.frame, text="Are you working with image or video files today?").grid(row=0, column=0, columnspan=2)
        button1 = Button(self.frame, width=20, height=5, text="Image")
        button1.grid(row=1, column=0, sticky=N)
        button1.bind("<Button-1>", self.ftypeim)
        button1.bind("<ButtonRelease-1>", self.quit_loop)

        button2 = Button(self.frame, width=20, height=5, text="Video")
        button2.grid(row=1, column=1, sticky=N)
        button2.bind("<Button-1>", self.ftypevid)
        # button2.bind("<Button-1>", self.quit_loop())



    def ftypeim(self, event=NONE):
        self.response = "img"
        print("img?")
        self.quit_loop()
        # self.frame.destroy()
    def ftypevid(self, event=NONE):
        self.response = "vid"
        print("vid?")
        self.quit_loop()

    def quit_loop(self, event=NONE):
        self.frame.destroy()
        self.session = File_Type(self)
        # self.root1.quit()
        return


primary = Controller()
session = primary.session
# session = File_Type(primary)


primary.root1.mainloop()

print (primary.response, 'session tags: ', primary.session.tag_list, primary.session.response, primary.session.exist, "The End")


### example code section for file import handling
### https://gist.github.com/Yagisanatode/0d1baad4e3a871587ab1