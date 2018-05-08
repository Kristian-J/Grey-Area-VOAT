# import tkinter as tk
# tk._test()

from tkinter import *
from tkinter import ttk
from Sel_File_Type import *


class Controller:
    def __init__(self):
        global session
        self.var = None
        self.response = None

        self.root1 = Tk()
        self.root1.title("Welcome")
        self.get_type()

        session = File_Type()

        self.root1.mainloop()



    def get_type(self):
        Label(self.root1, text="Are you working with image or video files today?").grid(row=0, column=0, columnspan=2)
        self.frame = Frame(self.root1)
        self.frame.grid()
        button1 = Button(self.frame, width=20, height=5, text="Image")
        button1.grid(row=1, column=0, sticky=N)
        button1.bind("<Button-1>", self.ftypeim)
        button1.bind("<ButtonRelease-1>", self.quit_loop)

        button2 = Button(self.frame, width=20, height=5, text="Video")
        button2.grid(row=1, column=1, sticky=N)
        button2.bind("<Button-1>", self.ftypevid)
        button2.bind("<ButtonRelease-1>", self.quit_loop)


    def ftypeim(self, event=NONE):
        # global response
        self.response = "img"
        print("img?")
        self.frame.destroy()
    def ftypevid(self, event=NONE):
        # global response
        self.response = "vid"
        print("vid?")

    def quit_loop(self, event=Widget):
        # global root
        self.frame.destroy()
        # self.root1.quit()
        return

# response = None

# root = Tk()
# root.title("Welcome")
#
# Label(root, text="Are you working with image or video files today?").grid(row=0, column=0, columnspan=2)
#
# button1 = Button(root, width=20, height=5, text="Image")
# button1.grid(row=1, column=0, sticky=N)
# button1.bind("<Button-1>", ftypeim)
# button1.bind("<ButtonRelease-1>", quit_loop)
#
# button2 = Button(root, width=20, height=5, text="Video")
# button2.grid(row=1, column=1, sticky=N)
# button2.bind("<Button-1>", ftypevid)
# button2.bind("<ButtonRelease-1>", quit_loop)
#
# root.mainloop()




primary = Controller()
# session = File_Type()
print (primary.response, session.tag_list, session.response, session.exist, "The End")



# session = Controller()

# session.getType()