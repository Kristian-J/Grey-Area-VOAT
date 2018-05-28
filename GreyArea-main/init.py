# import tkinter as tk
# tk._test()

from tkinter import *
from tkinter import ttk
from Tag_Builder import *
from module_template import *

class Controller:
    def __init__(self):
        # global session
        self.var = None
        self.files=[]
        self.session_tags = None ### for storing the instance of SessionTags
        self.tags=[]
        self.session_files = None ### for storing the instance of SessionFiles
        ### creating the main window ###
        self.root1 = Tk()
        self.root1.title("Welcome")
        self.root1.geometry("1500x800")
        ### setting the structure for the window and component elements ###
        self.tags_frame = Frame(self.root1)
        self.tags_frame.grid(row=3, column=0, rowspan= 4, columnspan = 1, sticky=N)
        self.tf_active = False
        self.disp_frame = Frame(self.root1)
        self.disp_frame.grid(row=0, column=1, rowspan= 7, columnspan = 10,sticky=NE)
        self.df_active = False
        self.controls_frame = Frame(self.root1)
        self.controls_frame.grid(row=7, column=1,  columnspan = 10, sticky=NE)
        self.cf_active = False



        # Menu Bar
        self.menu_frame = Frame(self.root1)
        self.menu_frame.grid(row=1, column=0, rowspan= 2,sticky=N)

        menu = Menu(self.root1)
        self.root1.config(menu=menu)

        file = Menu(menu)
        # file.add_command(label='Open', command=OpenFile)
        # file.add_command(label='Exit', command=lambda: exit())
        file.add_command(label='Exit', command=lambda: self.root1.quit())
        menu.add_cascade(label='File', menu=file)

        button3 = Button(self.menu_frame, width=15, text="Add Tags")
        button3.grid(row=1, column=1, sticky=N)
        button3.bind("<Button-1>", self.get_tags)
        button4 = Button(self.menu_frame, width=15, text="Select File")
        button4.grid(row=2, column=1, sticky=N)
        button4.bind("<Button-1>", self.get_files)

        # self.testcall = Xxxxx(self)
                ### this is an example external funtion/class call
                ### refer to module_template.py
                ### passes self (this instance of Controller)
        # self.root1.mainloop()
        return

    def get_tags(self, event=NONE):
        self.session_tags = SessionTags(self)
        print('these are the current tags', self.tags)
        return
    def get_files(self, event=NONE):
        self.session_files = SessionFiles(self)
        print('these are the current files', self.files)
        return

class GetType():
    def __init__(self):
        print("this it the type control")
        self.response = None

        self.root0 = Tk()
        self.frame = Frame(self.root0)
        self.frame.grid(row = 0, column = 0)
        Label(self.frame, text="Are you working with image or video files today?").grid(row=0, column=0, columnspan=2)
        button1 = Button(self.frame, width=20, height=5, text="Image")
        button1.grid(row=1, column=0, sticky=N)
        button1.bind("<Button-1>", self.ftypeim)
        # button1.bind("<ButtonRelease-1>", self.quit_loop)

        button2 = Button(self.frame, width=20, height=5, text="Video")
        button2.grid(row=1, column=1, sticky=N)
        button2.bind("<Button-1>", self.ftypevid)
        # button2.bind("<Button-1>", self.quit_loop())

        self.root0.mainloop()


    def ftypeim(self, event=NONE):
        self.response = "img"
        print("img?")
        self.quit_loop()
    def ftypevid(self, event=NONE):
        self.response = "vid"
        print("vid?")
        self.quit_loop()

    def quit_loop(self, event=NONE):
        self.frame.destroy()
        self.root0.quit()
        return



f_type = GetType()

primary = Controller()
# session_tags = primary.session_tags
# session_tags = SessionTags(primary)


primary.root1.mainloop()

print (f_type.response, 'session tags: ', primary.session_tags.tag_list, primary.session_tags.response, primary.session_tags.exist, "The End")
try:
    print("selected files are: ", primary.files)
    print("selected tags are: ", primary.tags)
except:
    print("error: data not stored in variable.")





### example code section for file import handling
### https://gist.github.com/Yagisanatode/0d1baad4e3a871587ab1