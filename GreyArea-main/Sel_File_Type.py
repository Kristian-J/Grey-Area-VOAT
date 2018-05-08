
from tkinter import *


class File_Type:
    def __init__(self):
        self.response = None
        self.tag_list = []
        self.exist = False
        self.tempbutton = None

        self.local = Tk()
        self.get_tags()
        self.local.mainloop()

    def add_tag(self, t, event=NONE):
        global U_input
        tag = U_input.get()
        print(tag)
        if len(tag) == 0:
            return
        self.tag_list.append(tag)
        print(self.tag_list)
        U_input.delete(0, "end")
        self.dis_tags()
        return

    def quit_loop(self, event=NONE):
        self.local.quit()
        return

    def dis_tags(self):
        if self.exist:
            self.frame1.destroy()
            print('destroyed')
        self.frame1=Frame(self.local)
        self.frame1.grid(column=1)
        for i in self.tag_list:
            self.tempbutton = Button(self.frame1, text=i ,width=20)
            self.tempbutton.grid(column=1)
        self.exist = True
        return

    def get_tags(self):

        self.local.title()

        Label(self.local, text="Please specify you're object tags").grid(row=0, column=0, columnspan=2)

        U_input_label = Label(self.local, text="Enter tag")
        U_input_label.grid(row=2, column=0,)

        global U_input
        U_input = Entry(self.local, width=20, )
        U_input.grid(row=2, column=1)

        U_input_enter = Button(self.local, text="Enter")
        U_input_enter.grid(row=2, column=2)
        U_input_enter.bind("<Button-1>", self.add_tag)

        U_input_exit = Button(self.local, text="exit")
        U_input_exit.grid(column=2)
        U_input_exit.bind("<Button-1>", self.quit_loop)





# tag_list = ["jack","flash"]
# root = Tk()
# session = File_Type()
#
# root.mainloop()
#
# print('end', session.tag_list)